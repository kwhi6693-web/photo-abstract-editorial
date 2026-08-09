#!/usr/bin/env python3
"""Validate a deterministic photo-abstract editorial composition."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from PIL import Image, ImageColor, ImageOps


EXPECTED_MANIFEST_VERSION = 1


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


def _load_manifest(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise FileNotFoundError(f"manifest not found: {path}")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("manifest root must be an object")
    return payload


def _expected_source_image(source_path: Path, manifest: dict[str, Any]) -> Image.Image:
    with Image.open(source_path) as opened:
        source = ImageOps.exif_transpose(opened).convert("RGB")
    target_width = manifest.get("options", {}).get("target_width")
    if target_width is not None:
        if not isinstance(target_width, int) or target_width < 1:
            raise ValueError("manifest target_width is invalid")
        target_height = max(1, round(source.height * target_width / source.width))
        if (target_width, target_height) != source.size:
            source = source.resize((target_width, target_height), Image.Resampling.LANCZOS)
    return source


def validate(
    source_path: str | Path,
    output_path: str | Path,
    manifest_path: str | Path,
) -> dict[str, Any]:
    source_path = Path(source_path)
    output_path = Path(output_path)
    manifest_path = Path(manifest_path)
    if not source_path.is_file():
        raise FileNotFoundError(f"source image not found: {source_path}")
    if not output_path.is_file():
        raise FileNotFoundError(f"output image not found: {output_path}")

    manifest = _load_manifest(manifest_path)
    checks: dict[str, bool] = {}
    errors: list[str] = []

    def record(name: str, passed: bool) -> None:
        checks[name] = bool(passed)
        if not passed:
            errors.append(name)

    record("manifest_version", manifest.get("manifest_version") == EXPECTED_MANIFEST_VERSION)
    record("source_sha256", manifest.get("source", {}).get("sha256") == sha256_file(source_path))
    record("output_sha256", manifest.get("output", {}).get("sha256") == sha256_file(output_path))

    expected_source = _expected_source_image(source_path, manifest)
    with Image.open(output_path) as opened:
        output = opened.convert("RGB")

    declared_output_size = manifest.get("output", {}).get("size")
    record("output_size", declared_output_size == [output.width, output.height])

    photo = manifest.get("photo_region", {})
    photo_geometry_ok = (
        photo.get("x") == 0
        and photo.get("y") == 0
        and photo.get("width") == expected_source.width
        and photo.get("height") == expected_source.height
        and output.width == expected_source.width
        and output.height >= expected_source.height
    )
    record("photo_region_geometry", photo_geometry_ok)
    if photo_geometry_ok:
        actual_photo = output.crop((0, 0, expected_source.width, expected_source.height))
        record("photo_region_pixels", actual_photo.tobytes() == expected_source.tobytes())
        record(
            "photo_region_hash",
            photo.get("pixel_sha256") == image_pixel_sha256(expected_source),
        )
    else:
        record("photo_region_pixels", False)
        record("photo_region_hash", False)

    panel = manifest.get("panel", {})
    panel_y = panel.get("y")
    panel_height = panel.get("height")
    panel_geometry_ok = (
        isinstance(panel_y, int)
        and isinstance(panel_height, int)
        and panel_y == expected_source.height
        and panel_height > 0
        and panel_y + panel_height == output.height
    )
    record("panel_geometry", panel_geometry_ok)
    if panel_geometry_ok:
        try:
            panel_color = ImageColor.getrgb(str(panel.get("color")))
        except ValueError:
            panel_color = None
        corner_pixels = [
            output.getpixel((0, panel_y)),
            output.getpixel((output.width - 1, panel_y)),
            output.getpixel((0, output.height - 1)),
            output.getpixel((output.width - 1, output.height - 1)),
        ]
        record("panel_corner_color", panel_color is not None and corner_pixels == [panel_color] * 4)
    else:
        record("panel_corner_color", False)

    return {
        "ok": not errors,
        "checks": checks,
        "errors": errors,
        "source_file": source_path.name,
        "output_file": output_path.name,
        "manifest_file": manifest_path.name,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--manifest", required=True, type=Path)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        verdict = validate(args.source, args.output, args.manifest)
    except Exception as error:
        verdict = {
            "ok": False,
            "checks": {},
            "errors": ["validation_exception"],
            "detail": f"{type(error).__name__}: {error}",
            "source_file": args.source.name,
            "output_file": args.output.name,
            "manifest_file": args.manifest.name,
        }
    print(json.dumps(verdict, ensure_ascii=False, sort_keys=True))
    return 0 if verdict["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
