#!/usr/bin/env python3
"""Deterministically convert a configured chroma background into clean alpha."""

from __future__ import annotations

import argparse
import json
import math
import os
import tempfile
from collections import deque
from pathlib import Path
from typing import Any

from PIL import Image, ImageColor


def parse_color(value: str) -> tuple[int, int, int]:
    try:
        parsed = ImageColor.getrgb(value)
    except ValueError as exc:
        raise ValueError(f"invalid chroma color: {value!r}") from exc
    if len(parsed) != 3:
        raise ValueError("chroma color must be an opaque RGB color")
    return parsed


def paths_refer_to_same_file(left: Path, right: Path) -> bool:
    if left.resolve() == right.resolve():
        return True
    try:
        return left.exists() and right.exists() and left.samefile(right)
    except OSError as error:
        raise ValueError(f"cannot compare input and output paths: {error}") from error


def remove_small_alpha_components(
    image: Image.Image,
    min_area: int,
    alpha_threshold: int = 32,
) -> tuple[Image.Image, int, int]:
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
    return cleaned, removed_components, removed_pixels


def _neutralize_fringe(
    rgb: tuple[int, int, int],
    chroma: tuple[int, int, int],
    visibility: float,
) -> tuple[int, int, int]:
    """Reduce the chroma cast on semi-transparent edge pixels deterministically."""
    luma = round((rgb[0] + rgb[1] + rgb[2]) / 3)
    blend = max(0.0, min(1.0, 1.0 - visibility))
    return tuple(round(channel * (1.0 - blend) + luma * blend) for channel in rgb)


def clean_rgba(
    image: Image.Image,
    chroma_color: tuple[int, int, int],
    tolerance: int,
    edge_softness: int,
    min_component_area: int,
) -> tuple[Image.Image, dict[str, int]]:
    if tolerance < 0:
        raise ValueError("tolerance must be non-negative")
    if edge_softness < 0:
        raise ValueError("edge_softness must be non-negative")
    if min_component_area < 1:
        raise ValueError("min_component_area must be at least 1")

    cleaned = image.convert("RGBA").copy()
    pixels = cleaned.load()
    removed_chroma_pixels = 0
    fringe_pixels = 0
    threshold = tolerance + edge_softness

    for y in range(cleaned.height):
        for x in range(cleaned.width):
            red, green, blue, alpha = pixels[x, y]
            distance = math.sqrt(
                (red - chroma_color[0]) ** 2
                + (green - chroma_color[1]) ** 2
                + (blue - chroma_color[2]) ** 2
            )
            if distance <= tolerance:
                pixels[x, y] = (0, 0, 0, 0)
                removed_chroma_pixels += 1
                continue
            if edge_softness and distance <= threshold:
                visibility = (distance - tolerance) / edge_softness
                next_alpha = min(alpha, max(0, round(255 * visibility)))
                pixels[x, y] = (*_neutralize_fringe((red, green, blue), chroma_color, visibility), next_alpha)
                fringe_pixels += 1

    cleaned, removed_components, removed_component_pixels = remove_small_alpha_components(
        cleaned,
        min_area=min_component_area,
    )
    return cleaned, {
        "removed_chroma_pixels": removed_chroma_pixels,
        "fringe_pixels": fringe_pixels,
        "removed_components": removed_components,
        "removed_component_pixels": removed_component_pixels,
        "removed_pixels": removed_chroma_pixels + removed_component_pixels,
    }


def atomic_save(image: Image.Image, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    handle = tempfile.NamedTemporaryFile(
        prefix=f".{destination.stem}.",
        suffix=destination.suffix,
        dir=destination.parent,
        delete=False,
    )
    temporary_path = Path(handle.name)
    handle.close()
    try:
        image.save(temporary_path, format="PNG")
        os.replace(temporary_path, destination)
    finally:
        temporary_path.unlink(missing_ok=True)


def clean_image(
    input_path: str | Path,
    output_path: str | Path,
    chroma_color: str = "#00FFFF",
    tolerance: int = 32,
    edge_softness: int = 16,
    min_component_area: int = 8,
) -> dict[str, Any]:
    input_path = Path(input_path)
    output_path = Path(output_path)
    if not input_path.is_file():
        raise FileNotFoundError(f"input image not found: {input_path}")
    if output_path.suffix.lower() != ".png":
        raise ValueError("output must use the .png extension")
    if paths_refer_to_same_file(input_path, output_path):
        raise ValueError("input and output must be different files")
    if output_path.exists():
        raise FileExistsError(f"refusing to overwrite existing output: {output_path}")

    chroma_rgb = parse_color(chroma_color)
    with Image.open(input_path) as opened:
        image = opened.convert("RGBA")
    cleaned, report = clean_rgba(
        image,
        chroma_rgb,
        tolerance=tolerance,
        edge_softness=edge_softness,
        min_component_area=min_component_area,
    )
    atomic_save(cleaned, output_path)
    return {
        "ok": True,
        "input_file": input_path.name,
        "output_file": output_path.name,
        "output_mode": "RGBA",
        "chroma_color": chroma_color.upper(),
        "tolerance": tolerance,
        "edge_softness": edge_softness,
        "min_component_area": min_component_area,
        **report,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--color", default="#00FFFF", help="Configured chroma color")
    parser.add_argument("--tolerance", type=int, default=32)
    parser.add_argument("--edge-softness", type=int, default=16)
    parser.add_argument("--min-component-area", type=int, default=8)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        report = clean_image(
            args.input,
            args.output,
            chroma_color=args.color,
            tolerance=args.tolerance,
            edge_softness=args.edge_softness,
            min_component_area=args.min_component_area,
        )
    except FileNotFoundError as error:
        code = "input_not_found" if str(error).startswith("input image not found") else "file_not_found"
        report = {"ok": False, "error": code, "detail": str(error)}
    except FileExistsError as error:
        report = {"ok": False, "error": "output_exists", "detail": str(error)}
    except ValueError as error:
        report = {"ok": False, "error": "invalid_input", "detail": str(error)}
    except Exception as error:  # pragma: no cover - final machine-readable safety net
        report = {"ok": False, "error": "cleanup_exception", "detail": f"{type(error).__name__}: {error}"}
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
