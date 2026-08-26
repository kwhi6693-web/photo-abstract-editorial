#!/usr/bin/env python3
"""Build or verify the deterministic installable Skill archive."""

from __future__ import annotations

import argparse
import os
from pathlib import Path, PurePosixPath
import tempfile
from zipfile import ZIP_DEFLATED, BadZipFile, ZipFile, ZipInfo


REPO_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_NAME = "photo-abstract-editorial"
ARCHIVE_PATH = REPO_ROOT / "dist" / "photo-abstract-editorial-skill.zip"
RUNTIME_FILES = (
    "SKILL.md",
    "agents/openai.yaml",
    "assets/examples/source-horizon.png",
    "assets/examples/result-horizon.png",
    "assets/examples/result-horizon.png.manifest.json",
    "references/art-direction.md",
    "references/control-system.md",
    "references/example-pair.md",
    "references/layout-profiles.md",
    "references/quality-check.md",
    "references/scene-profiles.md",
    "references/series-style.md",
    "scripts/compose_editorial.py",
    "scripts/remove_chroma_key.py",
    "scripts/validate_editorial.py",
)
TEXT_RUNTIME_SUFFIXES = {".json", ".md", ".py", ".yaml", ".yml"}


def archive_name(relative_path: str) -> str:
    return str(PurePosixPath(PACKAGE_NAME) / PurePosixPath(relative_path))


def runtime_bytes(relative_path: str) -> bytes:
    source_path = REPO_ROOT / relative_path
    data = source_path.read_bytes()
    if source_path.suffix.lower() in TEXT_RUNTIME_SUFFIXES:
        return data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return data


def verify_archive(archive_path: Path = ARCHIVE_PATH) -> list[str]:
    errors: list[str] = []
    if not archive_path.is_file():
        return [f"archive is missing: {archive_path}"]

    expected_names = {archive_name(relative_path) for relative_path in RUNTIME_FILES}
    try:
        with ZipFile(archive_path) as archive:
            entries = [entry for entry in archive.infolist() if not entry.is_dir()]
            actual_names = [entry.filename for entry in entries]
            if len(actual_names) != len(set(actual_names)):
                errors.append("archive contains duplicate file names")
            unexpected = sorted(set(actual_names) - expected_names)
            missing = sorted(expected_names - set(actual_names))
            if unexpected:
                errors.append(f"archive contains unexpected files: {', '.join(unexpected)}")
            if missing:
                errors.append(f"archive is missing files: {', '.join(missing)}")

            for relative_path in RUNTIME_FILES:
                name = archive_name(relative_path)
                source_path = REPO_ROOT / relative_path
                if not source_path.is_file():
                    errors.append(f"runtime source is missing: {source_path}")
                    continue
                if name in actual_names and archive.read(name) != runtime_bytes(relative_path):
                    errors.append(f"archive entry is stale: {name}")
    except (BadZipFile, OSError, ValueError) as error:
        errors.append(f"archive cannot be read: {type(error).__name__}: {error}")
    return errors


def build_archive(archive_path: Path = ARCHIVE_PATH) -> None:
    for relative_path in RUNTIME_FILES:
        source_path = REPO_ROOT / relative_path
        if not source_path.is_file():
            raise FileNotFoundError(f"runtime source is missing: {source_path}")

    archive_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        dir=archive_path.parent,
        prefix=f".{archive_path.stem}.",
        suffix=".tmp",
        delete=False,
    ) as temporary_file:
        temporary_path = Path(temporary_file.name)

    try:
        with ZipFile(
            temporary_path,
            mode="w",
            compression=ZIP_DEFLATED,
            compresslevel=9,
        ) as archive:
            for relative_path in RUNTIME_FILES:
                info = ZipInfo(
                    filename=archive_name(relative_path),
                    date_time=(1980, 1, 1, 0, 0, 0),
                )
                info.compress_type = ZIP_DEFLATED
                info.create_system = 3
                info.external_attr = (0o100644 & 0xFFFF) << 16
                archive.writestr(
                    info,
                    runtime_bytes(relative_path),
                    compress_type=ZIP_DEFLATED,
                    compresslevel=9,
                )
        os.replace(temporary_path, archive_path)
    finally:
        temporary_path.unlink(missing_ok=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify the current archive without modifying it",
    )
    args = parser.parse_args(argv)

    if not args.check:
        build_archive()
    errors = verify_archive()
    if errors:
        for error in errors:
            print(error)
        return 1
    action = "verified" if args.check else "built"
    print(f"Package {action}: {ARCHIVE_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
