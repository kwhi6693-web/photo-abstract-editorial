#!/usr/bin/env python3
"""Deterministically assemble a source photo, abstract motif, and exact title."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import tempfile
from collections import deque
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from PIL import Image, ImageColor, ImageDraw, ImageFont, ImageOps


MANIFEST_VERSION = 1
DEFAULT_PANEL_COLOR = "#E8E1D5"
DEFAULT_TITLE_COLOR = "#34343A"


@dataclass(frozen=True)
class CompositionOptions:
    title: str
    title_accent: str | None = None
    subtitle: str | None = None
    panel_color: str = DEFAULT_PANEL_COLOR
    title_color: str = DEFAULT_TITLE_COLOR
    subtitle_color: str | None = None
    layout: str = "lower-left"
    font_path: str | Path | None = None
    accent_font_path: str | Path | None = None
    subtitle_font_path: str | Path | None = None
    target_width: int | None = None
    panel_height: int | None = None
    motif_width_ratio: float = 0.54
    motif_center_x: float | None = None
    motif_top_ratio: float = 0.16
    margin_ratio: float = 0.07
    title_size_ratio: float = 0.041
    title_optical_offset_ratio: float = 0.012
    title_bottom_inset_ratio: float = 0.115
    accent_scale: float = 0.70


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def image_pixel_sha256(image: Image.Image) -> str:
    normalized = image.convert("RGB")
    digest = hashlib.sha256()
    digest.update(f"{normalized.width}x{normalized.height}:RGB\n".encode("ascii"))
    digest.update(normalized.tobytes())
    return digest.hexdigest()


def auto_panel_height(width: int, height: int) -> int:
    aspect = width / height
    if aspect >= 1.2:
        factor = 0.80
    elif aspect <= 0.8:
        factor = 0.55
    else:
        factor = 0.70
    return max(1, round(height * factor))


def parse_color(value: str, field: str) -> tuple[int, int, int]:
    try:
        parsed = ImageColor.getrgb(value)
    except ValueError as exc:
        raise ValueError(f"invalid {field}: {value!r}") from exc
    if len(parsed) != 3:
        raise ValueError(f"{field} must be an opaque RGB color")
    return parsed


def validate_single_line(value: str | None, field: str, required: bool) -> str | None:
    if value is None:
        if required:
            raise ValueError(f"{field} is required")
        return None
    cleaned = value.strip()
    if required and not cleaned:
        raise ValueError(f"{field} is required")
    if not cleaned:
        return None
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError(f"{field} must be a single line")
    return cleaned


def discover_font(explicit: str | Path | None, italic: bool = False) -> Path:
    if explicit is not None:
        candidate = Path(explicit).expanduser()
        if not candidate.is_file():
            raise FileNotFoundError(f"font not found: {candidate}")
        return candidate

    windows = Path(os.environ.get("WINDIR", "C:/Windows")) / "Fonts"
    candidates = (
        [windows / "BOD_I.TTF", windows / "GARAIT.TTF", windows / "georgiai.ttf", windows / "timesi.ttf", windows / "cambriai.ttf"]
        if italic
        else [windows / "BOD_R.TTF", windows / "BASKVILL.TTF", windows / "GARA.TTF", windows / "georgia.ttf", windows / "times.ttf", windows / "cambria.ttc"]
    )
    candidates.extend(
        [
            Path("/System/Library/Fonts/Supplemental/Bodoni 72 Smallcaps Book.ttf" if italic else "/System/Library/Fonts/Supplemental/Bodoni 72.ttc"),
            Path("/System/Library/Fonts/Supplemental/Baskerville.ttc"),
            Path("/System/Library/Fonts/Supplemental/Times New Roman Italic.ttf" if italic else "/System/Library/Fonts/Supplemental/Times New Roman.ttf"),
            Path("/usr/share/fonts/truetype/ebgaramond/EBGaramond12-Italic.ttf" if italic else "/usr/share/fonts/truetype/ebgaramond/EBGaramond12-Regular.ttf"),
            Path("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf" if italic else "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"),
            Path("/usr/share/fonts/truetype/liberation2/LiberationSerif-Italic.ttf" if italic else "/usr/share/fonts/truetype/liberation2/LiberationSerif-Regular.ttf"),
        ]
    )
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    raise FileNotFoundError("no usable serif font found; pass --font explicitly")


def fit_font(font_path: Path, text: str, preferred_size: int, max_width: int) -> ImageFont.FreeTypeFont:
    probe = Image.new("RGB", (1, 1))
    draw = ImageDraw.Draw(probe)
    size = max(8, preferred_size)
    while size >= 8:
        font = ImageFont.truetype(str(font_path), size=size)
        left, _top, right, _bottom = draw.textbbox((0, 0), text, font=font)
        if right - left <= max_width:
            return font
        size -= 1
    raise ValueError("text cannot fit the panel at a readable size")


def split_title_runs(title: str, accent: str | None) -> list[tuple[str, str]]:
    if accent is None:
        return [(title, "primary")]

    starts: list[int] = []
    offset = 0
    while True:
        start = title.find(accent, offset)
        if start < 0:
            break
        end = start + len(accent)
        left_boundary = start == 0 or not title[start - 1].isalnum()
        right_boundary = end == len(title) or not title[end].isalnum()
        if left_boundary and right_boundary:
            starts.append(start)
        offset = start + 1
    if len(starts) != 1:
        raise ValueError("title_accent must occur exactly once as a complete word or phrase")

    start = starts[0]
    end = start + len(accent)
    runs = [
        (title[:start], "primary"),
        (title[start:end], "accent"),
        (title[end:], "primary"),
    ]
    filtered_runs = [(text, style) for text, style in runs if text]
    if not any(style == "primary" and text.strip() for text, style in filtered_runs):
        raise ValueError("title_accent cannot cover the entire title")
    return filtered_runs


def measure_title_runs(
    draw: ImageDraw.ImageDraw,
    runs: list[tuple[str, str, ImageFont.FreeTypeFont, Path]],
) -> tuple[int, int, int]:
    width = round(sum(float(draw.textlength(text, font=font)) for text, _style, font, _path in runs))
    boxes = [draw.textbbox((0, 0), text, font=font, anchor="ls") for text, _style, font, _path in runs]
    top = min(box[1] for box in boxes)
    bottom = max(box[3] for box in boxes)
    return width, top, bottom


def fit_title_runs(
    primary_path: Path,
    accent_path: Path,
    run_specs: list[tuple[str, str]],
    preferred_size: int,
    max_width: int,
    accent_scale: float,
) -> tuple[list[tuple[str, str, ImageFont.FreeTypeFont, Path]], int, int, int]:
    probe = Image.new("RGB", (1, 1))
    draw = ImageDraw.Draw(probe)
    size = max(8, preferred_size)
    while size >= 8:
        primary_font = ImageFont.truetype(str(primary_path), size=size)
        accent_font = ImageFont.truetype(str(accent_path), size=max(8, round(size * accent_scale)))
        runs = [
            (text, style, accent_font if style == "accent" else primary_font, accent_path if style == "accent" else primary_path)
            for text, style in run_specs
        ]
        width, top, bottom = measure_title_runs(draw, runs)
        if width <= max_width:
            return runs, width, top, bottom
        size -= 1
    raise ValueError("text cannot fit the panel at a readable size")


def draw_title_runs(
    draw: ImageDraw.ImageDraw,
    position: tuple[int, int],
    runs: list[tuple[str, str, ImageFont.FreeTypeFont, Path]],
    fill: tuple[int, int, int],
) -> None:
    cursor_x, baseline = position
    for text, _style, font, _path in runs:
        draw.text((cursor_x, baseline), text, font=font, fill=fill, anchor="ls")
        cursor_x += float(draw.textlength(text, font=font))


def remove_small_alpha_components(
    image: Image.Image,
    min_area: int,
    alpha_threshold: int = 32,
) -> tuple[Image.Image, dict[str, int]]:
    cleaned = image.convert("RGBA").copy()
    alpha = cleaned.getchannel("A")
    pixels = alpha.load()
    width, height = alpha.size
    visited = bytearray(width * height)
    removed_components = 0
    removed_pixels = 0

    for y in range(height):
        for x in range(width):
            index = y * width + x
            if visited[index]:
                continue
            visited[index] = 1
            if pixels[x, y] < alpha_threshold:
                if pixels[x, y] != 0:
                    pixels[x, y] = 0
                    removed_pixels += 1
                continue

            component: list[tuple[int, int]] = []
            queue: deque[tuple[int, int]] = deque([(x, y)])
            while queue:
                current_x, current_y = queue.popleft()
                component.append((current_x, current_y))
                for neighbor_y in range(max(0, current_y - 1), min(height, current_y + 2)):
                    for neighbor_x in range(max(0, current_x - 1), min(width, current_x + 2)):
                        neighbor_index = neighbor_y * width + neighbor_x
                        if visited[neighbor_index]:
                            continue
                        visited[neighbor_index] = 1
                        if pixels[neighbor_x, neighbor_y] >= alpha_threshold:
                            queue.append((neighbor_x, neighbor_y))
                        elif pixels[neighbor_x, neighbor_y] != 0:
                            pixels[neighbor_x, neighbor_y] = 0
                            removed_pixels += 1

            if len(component) < min_area:
                removed_components += 1
                removed_pixels += len(component)
                for component_x, component_y in component:
                    pixels[component_x, component_y] = 0

    cleaned.putalpha(alpha)
    return cleaned, {
        "min_component_area": min_area,
        "removed_components": removed_components,
        "removed_pixels": removed_pixels,
    }


def atomic_save_image(image: Image.Image, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    handle = tempfile.NamedTemporaryFile(
        prefix=f".{destination.stem}.", suffix=destination.suffix, dir=destination.parent, delete=False
    )
    temp_path = Path(handle.name)
    handle.close()
    try:
        image.save(temp_path, format="PNG")
        os.replace(temp_path, destination)
    finally:
        if temp_path.exists():
            temp_path.unlink()


def atomic_write_json(payload: dict[str, Any], destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    handle = tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        newline="\n",
        prefix=f".{destination.stem}.",
        suffix=destination.suffix,
        dir=destination.parent,
        delete=False,
    )
    temp_path = Path(handle.name)
    try:
        json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
        handle.close()
        os.replace(temp_path, destination)
    finally:
        if not handle.closed:
            handle.close()
        if temp_path.exists():
            temp_path.unlink()


def paths_refer_to_same_file(left: Path, right: Path) -> bool:
    left_resolved = left.resolve()
    right_resolved = right.resolve()
    if left_resolved == right_resolved:
        return True
    try:
        return left.exists() and right.exists() and left.samefile(right)
    except OSError as error:
        raise ValueError(f"cannot compare file identity: {left} and {right}: {error}") from error


def validate_destination_paths(
    source_path: Path,
    motif_path: Path,
    output_path: Path,
    manifest_path: Path,
) -> None:
    for destination, label in (
        (output_path, "output"),
        (manifest_path, "manifest"),
    ):
        for input_path in (source_path, motif_path):
            if paths_refer_to_same_file(destination, input_path):
                raise ValueError(f"{label} path must not replace an input image: {input_path}")
        if destination.exists():
            raise FileExistsError(f"refusing to overwrite existing {label}: {destination}")


def compose(
    source_path: str | Path,
    motif_path: str | Path,
    output_path: str | Path,
    options: CompositionOptions,
) -> dict[str, Any]:
    source_path = Path(source_path)
    motif_path = Path(motif_path)
    output_path = Path(output_path)
    if not source_path.is_file():
        raise FileNotFoundError(f"source image not found: {source_path}")
    if not motif_path.is_file():
        raise FileNotFoundError(f"motif image not found: {motif_path}")
    if output_path.suffix.lower() != ".png":
        raise ValueError("output must use the .png extension")
    manifest_path = output_path.with_suffix(output_path.suffix + ".manifest.json")
    validate_destination_paths(source_path, motif_path, output_path, manifest_path)

    title = validate_single_line(options.title, "title", required=True)
    title_accent = validate_single_line(options.title_accent, "title_accent", required=False)
    subtitle = validate_single_line(options.subtitle, "subtitle", required=False)
    title_run_specs = split_title_runs(title, title_accent)
    panel_rgb = parse_color(options.panel_color, "panel_color")
    title_rgb = parse_color(options.title_color, "title_color")
    subtitle_rgb = parse_color(options.subtitle_color or options.title_color, "subtitle_color")
    if options.layout not in {"lower-left", "bottom-center"}:
        raise ValueError("layout must be 'lower-left' or 'bottom-center'")
    if not 0.15 <= options.motif_width_ratio <= 0.75:
        raise ValueError("motif_width_ratio must be between 0.15 and 0.75")
    if options.motif_center_x is not None and not 0.0 <= options.motif_center_x <= 1.0:
        raise ValueError("motif_center_x must be between 0 and 1")
    if not 0.0 <= options.motif_top_ratio <= 0.5:
        raise ValueError("motif_top_ratio must be between 0 and 0.5")
    if not 0.03 <= options.margin_ratio <= 0.15:
        raise ValueError("margin_ratio must be between 0.03 and 0.15")
    if not 0.02 <= options.title_size_ratio <= 0.08:
        raise ValueError("title_size_ratio must be between 0.02 and 0.08")
    if not 0.0 <= options.title_optical_offset_ratio <= 0.05:
        raise ValueError("title_optical_offset_ratio must be between 0 and 0.05")
    if not 0.04 <= options.title_bottom_inset_ratio <= 0.2:
        raise ValueError("title_bottom_inset_ratio must be between 0.04 and 0.2")
    if not 0.5 <= options.accent_scale <= 1.0:
        raise ValueError("accent_scale must be between 0.5 and 1.0")

    with Image.open(source_path) as opened_source:
        source = ImageOps.exif_transpose(opened_source).convert("RGB")
    original_visual_size = source.size
    if options.target_width is not None:
        if options.target_width < 64:
            raise ValueError("target_width must be at least 64 pixels")
        target_height = max(1, round(source.height * options.target_width / source.width))
        if (options.target_width, target_height) != source.size:
            source = source.resize((options.target_width, target_height), Image.Resampling.LANCZOS)

    panel_height = (
        options.panel_height
        if options.panel_height is not None
        else auto_panel_height(source.width, source.height)
    )
    if panel_height < 64:
        raise ValueError("panel_height must be at least 64 pixels")
    canvas = Image.new("RGB", (source.width, source.height + panel_height), panel_rgb)
    canvas.paste(source, (0, 0))
    margin = max(4, round(source.width * options.margin_ratio))

    with Image.open(motif_path) as opened_motif:
        motif = opened_motif.convert("RGBA")
    motif, initial_cleanup = remove_small_alpha_components(
        motif,
        min_area=max(8, round(motif.width * motif.height * 0.00005)),
    )
    alpha_bbox = motif.getchannel("A").getbbox()
    if alpha_bbox is None:
        raise ValueError("motif image is fully transparent")
    motif = motif.crop(alpha_bbox)

    motif_width = max(1, round(source.width * options.motif_width_ratio))
    motif_height = max(1, round(motif.height * motif_width / motif.width))
    max_motif_height = max(1, round(panel_height * 0.38))
    if motif_height > max_motif_height:
        motif_height = max_motif_height
        motif_width = max(1, round(motif.width * motif_height / motif.height))
    motif = motif.resize((motif_width, motif_height), Image.Resampling.LANCZOS)
    motif, resized_cleanup = remove_small_alpha_components(
        motif,
        min_area=max(8, round(motif.width * motif.height * 0.0025)),
    )
    if motif.getchannel("A").getbbox() is None:
        raise ValueError("motif image is fully transparent after cleanup")
    if options.motif_center_x is not None:
        motif_x = round(source.width * options.motif_center_x - motif_width / 2)
    elif options.layout == "lower-left":
        motif_x = margin
    else:
        motif_x = round((source.width - motif_width) / 2)
    motif_x = min(max(0, motif_x), source.width - motif_width)
    motif_y = source.height + round(panel_height * options.motif_top_ratio)
    motif_y = min(motif_y, source.height + panel_height - motif_height)
    canvas.paste(motif, (motif_x, motif_y), motif)

    main_font_path = discover_font(options.font_path, italic=False)
    accent_font_path = (
        discover_font(options.accent_font_path, italic=True) if title_accent else main_font_path
    )
    subtitle_font_path = discover_font(options.subtitle_font_path, italic=True) if subtitle else None
    draw = ImageDraw.Draw(canvas)
    title_optical_offset = max(0, round(source.width * options.title_optical_offset_ratio))
    bottom_inset = max(4, round(source.width * options.title_bottom_inset_ratio))
    title_x = margin + title_optical_offset if options.layout == "lower-left" else 0
    max_text_width = source.width - title_x - margin if options.layout == "lower-left" else source.width - 2 * margin
    title_runs, title_width, title_top, title_bottom = fit_title_runs(
        main_font_path,
        accent_font_path,
        title_run_specs,
        round(source.width * options.title_size_ratio),
        max_text_width,
        options.accent_scale,
    )
    main_font = next(font for _text, style, font, _path in title_runs if style == "primary")
    subtitle_font = (
        fit_font(subtitle_font_path, subtitle, round(panel_height * 0.038), max_text_width)
        if subtitle and subtitle_font_path
        else None
    )

    title_height = title_bottom - title_top
    subtitle_width = subtitle_height = 0
    if subtitle and subtitle_font:
        subtitle_box = draw.textbbox((0, 0), subtitle, font=subtitle_font)
        subtitle_width = subtitle_box[2] - subtitle_box[0]
        subtitle_height = subtitle_box[3] - subtitle_box[1]
    gap = max(2, round(panel_height * 0.018)) if subtitle else 0
    block_height = title_height + gap + subtitle_height
    text_y = canvas.height - bottom_inset - block_height
    if text_y < source.height:
        raise ValueError("typography does not fit inside the panel")
    if options.layout == "bottom-center":
        title_x = round((source.width - title_width) / 2)
        subtitle_x = round((source.width - subtitle_width) / 2)
    else:
        subtitle_x = title_x
    draw_title_runs(
        draw,
        (title_x, text_y - title_top),
        title_runs,
        title_rgb,
    )
    if subtitle and subtitle_font:
        subtitle_y = text_y + title_height + gap
        draw.text((subtitle_x, subtitle_y - subtitle_box[1]), subtitle, font=subtitle_font, fill=subtitle_rgb)

    atomic_save_image(canvas, output_path)
    manifest: dict[str, Any] = {
        "manifest_version": MANIFEST_VERSION,
        "source": {
            "file_name": source_path.name,
            "sha256": sha256_file(source_path),
            "visual_size": list(original_visual_size),
            "rendered_pixel_sha256": image_pixel_sha256(source),
        },
        "motif": {
            "file_name": motif_path.name,
            "sha256": sha256_file(motif_path),
            "cleanup": {
                "removed_components": initial_cleanup["removed_components"] + resized_cleanup["removed_components"],
                "removed_pixels": initial_cleanup["removed_pixels"] + resized_cleanup["removed_pixels"],
                "initial_min_component_area": initial_cleanup["min_component_area"],
                "resized_min_component_area": resized_cleanup["min_component_area"],
            },
        },
        "output": {
            "file_name": output_path.name,
            "sha256": sha256_file(output_path),
            "size": list(canvas.size),
        },
        "photo_region": {
            "x": 0,
            "y": 0,
            "width": source.width,
            "height": source.height,
            "pixel_sha256": image_pixel_sha256(source),
            "pixel_exact": options.target_width is None or options.target_width == original_visual_size[0],
        },
        "panel": {
            "y": source.height,
            "height": panel_height,
            "color": options.panel_color.upper(),
        },
        "layout_grid": {
            "inset": margin,
            "inset_ratio": options.margin_ratio,
        },
        "motif_region": {
            "x": motif_x,
            "y": motif_y,
            "width": motif_width,
            "height": motif_height,
        },
        "typography": {
            "title": title,
            "subtitle": subtitle,
            "layout": options.layout,
            "font_file": main_font_path.name,
            "accent_font_file": accent_font_path.name if title_accent else None,
            "subtitle_font_file": subtitle_font_path.name if subtitle_font_path else None,
            "title_font_size": main_font.size,
            "title_accent": title_accent,
            "title_runs": [
                {
                    "text": run_text,
                    "style": run_style,
                    "font_file": run_path.name,
                    "font_size": run_font.size,
                }
                for run_text, run_style, run_font, run_path in title_runs
            ],
            "kerning_mode": "whole-run",
            "title_anchor_x": title_x,
            "title_optical_offset": title_optical_offset if options.layout == "lower-left" else 0,
            "bottom_inset": bottom_inset,
            "subtitle_font_size": subtitle_font.size if subtitle_font else None,
            "title_region": {
                "x": title_x,
                "y": text_y,
                "width": title_width,
                "height": title_height,
            },
            "subtitle_region": (
                {
                    "x": subtitle_x + subtitle_box[0],
                    "y": text_y + title_height + gap,
                    "width": subtitle_width,
                    "height": subtitle_height,
                }
                if subtitle and subtitle_font
                else None
            ),
            "title_color": options.title_color.upper(),
            "subtitle_color": (options.subtitle_color or options.title_color).upper(),
        },
        "options": {
            **asdict(options),
            "font_path": str(options.font_path) if options.font_path else None,
            "accent_font_path": str(options.accent_font_path) if options.accent_font_path else None,
            "subtitle_font_path": str(options.subtitle_font_path) if options.subtitle_font_path else None,
        },
    }
    atomic_write_json(manifest, manifest_path)
    return manifest


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--motif", required=True, type=Path, help="Transparent PNG motif")
    parser.add_argument("--output", required=True, type=Path, help="Output .png path")
    parser.add_argument("--title", required=True)
    parser.add_argument("--title-accent")
    parser.add_argument("--subtitle")
    parser.add_argument("--panel-color", default=DEFAULT_PANEL_COLOR)
    parser.add_argument("--title-color", default=DEFAULT_TITLE_COLOR)
    parser.add_argument("--subtitle-color")
    parser.add_argument("--layout", choices=("lower-left", "bottom-center"), default="lower-left")
    parser.add_argument("--font", dest="font_path", type=Path)
    parser.add_argument("--accent-font", dest="accent_font_path", type=Path)
    parser.add_argument("--subtitle-font", dest="subtitle_font_path", type=Path)
    parser.add_argument("--target-width", type=int)
    parser.add_argument("--panel-height", type=int)
    parser.add_argument("--motif-width-ratio", type=float, default=0.54)
    parser.add_argument("--motif-center-x", type=float)
    parser.add_argument("--motif-top-ratio", type=float, default=0.16)
    parser.add_argument("--title-size-ratio", type=float, default=0.041)
    parser.add_argument("--title-optical-offset-ratio", type=float, default=0.012)
    parser.add_argument("--title-bottom-inset-ratio", type=float, default=0.115)
    parser.add_argument("--accent-scale", type=float, default=0.70)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    options = CompositionOptions(
        title=args.title,
        title_accent=args.title_accent,
        subtitle=args.subtitle,
        panel_color=args.panel_color,
        title_color=args.title_color,
        subtitle_color=args.subtitle_color,
        layout=args.layout,
        font_path=args.font_path,
        accent_font_path=args.accent_font_path,
        subtitle_font_path=args.subtitle_font_path,
        target_width=args.target_width,
        panel_height=args.panel_height,
        motif_width_ratio=args.motif_width_ratio,
        motif_center_x=args.motif_center_x,
        motif_top_ratio=args.motif_top_ratio,
        title_size_ratio=args.title_size_ratio,
        title_optical_offset_ratio=args.title_optical_offset_ratio,
        title_bottom_inset_ratio=args.title_bottom_inset_ratio,
        accent_scale=args.accent_scale,
    )
    manifest = compose(args.source, args.motif, args.output, options)
    print(json.dumps(manifest, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
