#!/usr/bin/env python3
"""Validate formal runtime archives, extraction, and bundled smoke behavior."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path, PurePosixPath
import subprocess
import sys
import tempfile
from zipfile import BadZipFile, ZipFile


REPO_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_NAME = "photo-abstract-editorial"
TEXT_SUFFIXES = {".json", ".md", ".py", ".yaml", ".yml"}


@dataclass(frozen=True)
class PackageContract:
    name: str
    archive: str
    runtime_files: tuple[str, ...]
    expected_sha256: str
    source_synced: bool


V3_RUNTIME_FILES = (
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
ORIGINAL_RUNTIME_FILES = (
    "SKILL.md",
    "agents/openai.yaml",
    "assets/examples/source-horizon.png",
    "assets/examples/result-horizon.png",
    "assets/examples/result-horizon.png.manifest.json",
    "references/art-direction.md",
    "references/example-pair.md",
    "scripts/compose_editorial.py",
    "scripts/validate_editorial.py",
)
PACKAGE_CONTRACTS = (
    PackageContract(
        name="V3 Adaptive",
        archive="dist/photo-abstract-editorial-skill.zip",
        runtime_files=V3_RUNTIME_FILES,
        expected_sha256="0d2c41604526a8d0f25495986a36b237950e48535f20e215298cba169ffb6649",
        source_synced=True,
    ),
    PackageContract(
        name="Original",
        archive="dist/photo-abstract-editorial-original.zip",
        runtime_files=ORIGINAL_RUNTIME_FILES,
        expected_sha256="a1a44b1a9cec9ba04b379a7d3a14315701abb14bb93e953003337870772d0a6d",
        source_synced=False,
    ),
)


def archive_name(relative_path: str) -> str:
    return str(PurePosixPath(PACKAGE_NAME) / PurePosixPath(relative_path))


def canonical_bytes(path: Path) -> bytes:
    data = path.read_bytes()
    if path.suffix.lower() in TEXT_SUFFIXES:
        return data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return data


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _check_archive_entries(
    repo_root: Path,
    archive_path: Path,
    contract: PackageContract,
) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    actual_names: list[str] = []
    expected_names = {archive_name(relative) for relative in contract.runtime_files}
    try:
        with ZipFile(archive_path) as archive:
            entries = [entry for entry in archive.infolist() if not entry.is_dir()]
            actual_names = [entry.filename for entry in entries]
            if len(actual_names) != len(set(actual_names)):
                errors.append(f"{contract.name}: archive contains duplicate file names")
            unexpected = sorted(set(actual_names) - expected_names)
            missing = sorted(expected_names - set(actual_names))
            if unexpected:
                errors.append(f"{contract.name}: archive contains unexpected files: {', '.join(unexpected)}")
            if missing:
                errors.append(f"{contract.name}: archive is missing files: {', '.join(missing)}")
            for relative in contract.runtime_files:
                name = archive_name(relative)
                if name in actual_names and contract.source_synced:
                    source = repo_root / relative
                    if not source.is_file():
                        errors.append(f"{contract.name}: source file is missing: {source}")
                    elif archive.read(name) != canonical_bytes(source):
                        errors.append(f"{contract.name}: archive entry is stale: {name}")
    except (BadZipFile, OSError, ValueError) as error:
        errors.append(f"{contract.name}: archive cannot be read: {type(error).__name__}: {error}")
    return errors, actual_names


def _run_smoke(package_root: Path, contract: PackageContract) -> list[str]:
    errors: list[str] = []
    for script in ("compose_editorial.py", "validate_editorial.py"):
        completed = subprocess.run(
            [sys.executable, f"scripts/{script}", "--help"],
            cwd=package_root,
            capture_output=True,
            text=True,
            check=False,
            timeout=20,
        )
        if completed.returncode != 0:
            detail = (completed.stderr or completed.stdout).strip().splitlines()[-1:]
            errors.append(f"{contract.name}: bundled {script} --help failed: {' '.join(detail)}")

    source = package_root / "assets" / "examples" / "source-horizon.png"
    result = package_root / "assets" / "examples" / "result-horizon.png"
    manifest = package_root / "assets" / "examples" / "result-horizon.png.manifest.json"
    validator = subprocess.run(
        [
            sys.executable,
            "scripts/validate_editorial.py",
            "--source",
            str(source.relative_to(package_root)),
            "--output",
            str(result.relative_to(package_root)),
            "--manifest",
            str(manifest.relative_to(package_root)),
        ],
        cwd=package_root,
        capture_output=True,
        text=True,
        check=False,
        timeout=30,
    )
    try:
        validator_verdict = json.loads(validator.stdout)
    except json.JSONDecodeError:
        validator_verdict = {}
    if validator.returncode != 0 or validator_verdict.get("ok") is not True:
        detail = (validator.stderr or validator.stdout).strip().replace("\n", " ")
        errors.append(f"{contract.name}: bundled validator failed: {detail}")

    import_smoke = subprocess.run(
        [
            sys.executable,
            "-c",
            "from PIL import Image; from scripts import compose_editorial, validate_editorial; "
            "assert Image.open('assets/examples/source-horizon.png').size",
        ],
        cwd=package_root,
        capture_output=True,
        text=True,
        check=False,
        timeout=20,
    )
    if import_smoke.returncode != 0:
        detail = (import_smoke.stderr or import_smoke.stdout).strip().replace("\n", " ")
        errors.append(f"{contract.name}: bundled import smoke failed: {detail}")
    return errors


def _extract_and_check(archive_path: Path, contract: PackageContract, run_smoke: bool) -> list[str]:
    errors: list[str] = []
    with tempfile.TemporaryDirectory(prefix="photo-abstract-editorial-package-") as temporary_directory:
        extraction_root = Path(temporary_directory)
        try:
            with ZipFile(archive_path) as archive:
                archive.extractall(extraction_root)
        except (BadZipFile, OSError, ValueError) as error:
            return [f"{contract.name}: clean extraction failed: {type(error).__name__}: {error}"]

        package_root = extraction_root / PACKAGE_NAME
        for relative in contract.runtime_files:
            if not (package_root / relative).is_file():
                errors.append(f"{contract.name}: extracted runtime file is missing: {relative}")
        if run_smoke and not errors:
            errors.extend(_run_smoke(package_root, contract))
    return errors


def check_package_parity(repo_root: Path = REPO_ROOT, run_smoke: bool = True) -> list[str]:
    """Return errors for source/archive drift or failed clean-package smoke tests."""
    repo_root = Path(repo_root).resolve()
    errors: list[str] = []
    for contract in PACKAGE_CONTRACTS:
        archive_path = repo_root / contract.archive
        if not archive_path.is_file():
            errors.append(f"{contract.name}: runtime archive is missing: {archive_path}")
            continue

        if sha256_file(archive_path) != contract.expected_sha256:
            errors.append(
                f"{contract.name}: archive digest changed; expected {contract.expected_sha256}, "
                f"detected {sha256_file(archive_path)}"
            )
        contract_errors, _actual_names = _check_archive_entries(repo_root, archive_path, contract)
        errors.extend(contract_errors)
        if not contract_errors:
            errors.extend(_extract_and_check(archive_path, contract, run_smoke))
    return errors


def main(argv: list[str] | None = None) -> int:
    del argv
    errors = check_package_parity()
    if errors:
        print("PACKAGE PARITY: FAIL")
        for error in errors:
            print(error)
        return 1
    print("PACKAGE PARITY: PASS")
    for contract in PACKAGE_CONTRACTS:
        print(f"{contract.name}: {contract.archive} ({contract.expected_sha256})")
    print("Clean extraction, bundled import smoke, and bundled validator: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
