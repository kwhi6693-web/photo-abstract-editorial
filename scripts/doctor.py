#!/usr/bin/env python3
"""Read-only local environment preflight for Photo Abstract Editorial."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import importlib
import importlib.util
from pathlib import Path
import platform
import subprocess
import sys
import tempfile


REPO_ROOT = Path(__file__).resolve().parents[1]
SUPPORTED_PYTHON = ((3, 10), (3, 11), (3, 12), (3, 13))
REQUIRED_IMPORTS = (
    "PIL",
    "PIL.Image",
    "PIL.ImageColor",
    "PIL.ImageDraw",
    "PIL.ImageFont",
    "PIL.ImageOps",
)
RUNTIME_PROJECT_FILES = (
    "SKILL.md",
    "README.md",
    "README.zh-CN.md",
    "README.zh-TW.md",
    "requirements.txt",
    "agents/openai.yaml",
    "references/art-direction.md",
    "references/control-system.md",
    "references/example-pair.md",
    "references/layout-profiles.md",
    "references/quality-check.md",
    "references/scene-profiles.md",
    "references/series-style.md",
    "scripts/compose_editorial.py",
    "scripts/doctor.py",
    "scripts/remove_chroma_key.py",
    "scripts/validate_editorial.py",
)


@dataclass(frozen=True)
class CheckResult:
    name: str
    status: str
    detail: str
    what_failed: str | None = None
    why: str | None = None
    required: str | None = None
    detected: str | None = None
    how_to_fix: str | None = None


def _pass(name: str, detail: str) -> CheckResult:
    return CheckResult(name=name, status="PASS", detail=detail)


def _not_detectable(name: str, detail: str) -> CheckResult:
    return CheckResult(name=name, status="NOT DETECTABLE", detail=detail)


def _fail(
    name: str,
    *,
    detail: str,
    what_failed: str,
    why: str,
    required: str,
    detected: str,
    how_to_fix: str,
) -> CheckResult:
    return CheckResult(
        name=name,
        status="FAIL",
        detail=detail,
        what_failed=what_failed,
        why=why,
        required=required,
        detected=detected,
        how_to_fix=how_to_fix,
    )


def render_check(result: CheckResult) -> str:
    line = f"{result.name}: {result.status}"
    if result.detail:
        line += f" — {result.detail}"
    if result.status == "FAIL":
        fields = (
            ("WHAT FAILED", result.what_failed),
            ("WHY", result.why),
            ("REQUIRED", result.required),
            ("DETECTED", result.detected),
            ("HOW TO FIX", result.how_to_fix),
        )
        line += "\n" + "\n".join(f"{label}: {value}" for label, value in fields if value)
    return line


def _check_platform() -> CheckResult:
    current = platform.system()
    supported = {"Windows": "Windows", "Linux": "Ubuntu/Linux", "Darwin": "macOS"}
    if current in supported:
        return _pass("OS/platform", f"{supported[current]} · {platform.machine()}")
    return _fail(
        "OS/platform",
        detail=f"unsupported platform {current!r}",
        what_failed="host platform support",
        why="the local filesystem and font contract is only verified on Windows, Linux, and macOS",
        required="Windows, Ubuntu/Linux, or macOS",
        detected=f"{current} · {platform.machine()}",
        how_to_fix="run this workflow on a supported platform or use a host capability mode",
    )


def _check_python() -> CheckResult:
    current = (sys.version_info.major, sys.version_info.minor)
    version = platform.python_version()
    if current in SUPPORTED_PYTHON:
        supported = ", ".join(f"{major}.{minor}" for major, minor in SUPPORTED_PYTHON)
        return _pass("Python", f"{version} · tested minors: {supported}")
    supported = ", ".join(f"{major}.{minor}" for major, minor in SUPPORTED_PYTHON)
    return _fail(
        "Python",
        detail=f"{version} is outside the tested support contract",
        what_failed="Python support status",
        why="the repository has not verified this Python minor version",
        required=f"one of: {supported}",
        detected=version,
        how_to_fix="install and activate one of the tested Python versions, then rerun python scripts/doctor.py",
    )


def _load_pillow() -> tuple[CheckResult, object | None]:
    try:
        pillow = importlib.import_module("PIL")
    except Exception as error:  # pragma: no cover - depends on the caller's environment
        return (
            _fail(
                "Pillow",
                detail="Pillow could not be imported",
                what_failed="Pillow import",
                why="the local compositor and validator require the runtime image dependency",
                required="Pillow==12.3.0 from requirements.txt",
                detected=f"{type(error).__name__}: {error}",
                how_to_fix="python -m pip install -r requirements.txt",
            ),
            None,
        )
    return _pass("Pillow", str(getattr(pillow, "__version__", "version unavailable"))), pillow


def _check_required_imports() -> CheckResult:
    missing: list[str] = []
    for module_name in REQUIRED_IMPORTS:
        try:
            importlib.import_module(module_name)
        except Exception as error:  # pragma: no cover - depends on the caller's environment
            missing.append(f"{module_name} ({type(error).__name__}: {error})")
    if not missing:
        return _pass("Required imports", ", ".join(REQUIRED_IMPORTS))
    return _fail(
        "Required imports",
        detail="one or more required imports are unavailable",
        what_failed="required Python imports",
        why="a clean runtime environment cannot load the image pipeline",
        required=", ".join(REQUIRED_IMPORTS),
        detected="; ".join(missing),
        how_to_fix="python -m pip install -r requirements.txt",
    )


def _check_temp_directory() -> CheckResult:
    try:
        with tempfile.TemporaryDirectory(prefix="photo-abstract-editorial-doctor-") as temporary_directory:
            probe = Path(temporary_directory) / "write-probe.txt"
            probe.write_text("environment contract\n", encoding="utf-8")
            if probe.read_text(encoding="utf-8") != "environment contract\n":
                raise OSError("temporary file read-back mismatch")
    except Exception as error:  # pragma: no cover - depends on the host filesystem
        return _fail(
            "Temporary directory",
            detail="temporary write/read failed",
            what_failed="temporary directory access",
            why="the compositor and tests need a writable, clean temporary workspace",
            required="a writable system temporary directory",
            detected=f"{type(error).__name__}: {error}",
            how_to_fix="check the system temporary directory permissions and rerun this doctor",
        )
    return _pass("Temporary directory", "write/read/cleanup PASS")


def _check_image_codecs() -> CheckResult:
    try:
        from PIL import Image

        with tempfile.TemporaryDirectory(prefix="photo-abstract-editorial-image-") as temporary_directory:
            root = Path(temporary_directory)
            rgb_path = root / "rgb.png"
            rgba_path = root / "rgba.png"
            Image.new("RGB", (7, 5), (24, 48, 72)).save(rgb_path, format="PNG")
            Image.new("RGBA", (7, 5), (24, 48, 72, 123)).save(rgba_path, format="PNG")
            with Image.open(rgb_path) as rgb:
                rgb.load()
                rgb_ok = rgb.mode == "RGB" and rgb.size == (7, 5)
            with Image.open(rgba_path) as rgba:
                rgba.load()
                alpha_ok = rgba.mode == "RGBA" and rgba.getpixel((0, 0))[3] == 123
    except Exception as error:  # pragma: no cover - depends on the caller's environment
        return _fail(
            "Image codecs",
            detail="PNG open/save or transparency probe failed",
            what_failed="Pillow image codec capability",
            why="the runtime must preserve ordinary RGB images and transparent motifs",
            required="RGB PNG and RGBA PNG read/write support",
            detected=f"{type(error).__name__}: {error}",
            how_to_fix="python -m pip install -r requirements.txt, then rerun python scripts/doctor.py",
        )
    if not (rgb_ok and alpha_ok):
        return _fail(
            "Image codecs",
            detail="PNG read-back did not preserve expected mode, size, or alpha",
            what_failed="PNG codec round-trip",
            why="the image pipeline relies on deterministic RGB/RGBA behavior",
            required="RGB and RGBA PNG round-trip",
            detected=f"rgb_ok={rgb_ok}, alpha_ok={alpha_ok}",
            how_to_fix="reinstall the pinned Pillow runtime and rerun python scripts/doctor.py",
        )
    return _pass("Image codecs", "RGB PNG and RGBA transparency round-trip PASS")


def _check_project_files(repo_root: Path, development: bool) -> CheckResult:
    required = list(RUNTIME_PROJECT_FILES)
    if development:
        required.append("requirements-dev.txt")
    missing = [relative for relative in required if not (repo_root / relative).is_file()]
    if missing:
        return _fail(
            "Project files",
            detail="required repository files are missing",
            what_failed="project file contract",
            why="the workflow cannot run or be audited from this checkout",
            required="the runtime and documented project files",
            detected=", ".join(missing),
            how_to_fix="restore the missing files from the repository, then rerun python scripts/doctor.py",
        )
    return _pass("Project files", f"{len(required)} required files present")


def _run_read_only_command(command: list[str], cwd: Path, timeout: int) -> tuple[bool, str]:
    try:
        completed = subprocess.run(
            command,
            cwd=cwd,
            capture_output=True,
            text=True,
            check=False,
            timeout=timeout,
        )
    except Exception as error:  # pragma: no cover - depends on the host process
        return False, f"{type(error).__name__}: {error}"
    detail = (completed.stderr or completed.stdout).strip().replace("\n", " ")
    return completed.returncode == 0, detail


def _check_validator(repo_root: Path) -> CheckResult:
    validator = repo_root / "scripts" / "validate_editorial.py"
    if not validator.is_file():
        return _fail(
            "Validator",
            detail="validator script is missing",
            what_failed="validator executable",
            why="the repository cannot verify generated output",
            required="scripts/validate_editorial.py",
            detected=str(validator),
            how_to_fix="restore scripts/validate_editorial.py, then rerun python scripts/doctor.py",
        )
    ok, detail = _run_read_only_command([sys.executable, str(validator), "--help"], repo_root, 20)
    if ok:
        return _pass("Validator", "scripts/validate_editorial.py --help PASS")
    return _fail(
        "Validator",
        detail="validator could not start",
        what_failed="validator executable",
        why="the machine validation entry point is not runnable in this environment",
        required="python scripts/validate_editorial.py --help returns exit code 0",
        detected=detail or "non-zero exit code",
        how_to_fix="python -m pip install -r requirements.txt, then rerun python scripts/doctor.py",
    )


def _check_serif_font(repo_root: Path) -> CheckResult:
    composer = repo_root / "scripts" / "compose_editorial.py"
    if not composer.is_file():
        return _not_detectable("Serif font", "composer is missing")
    try:
        spec = importlib.util.spec_from_file_location("photo_abstract_editorial_doctor_composer", composer)
        if spec is None or spec.loader is None:
            raise ImportError("could not load compose_editorial.py")
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        font_path = module.discover_font(None)
        if not Path(font_path).is_file():
            raise FileNotFoundError(str(font_path))
        from PIL import ImageFont

        ImageFont.truetype(str(font_path), size=16)
    except Exception as error:  # pragma: no cover - depends on host fonts and Pillow
        return _fail(
            "Serif font",
            detail="no usable serif font was discovered",
            what_failed="serif font lookup",
            why="Strict Fidelity local typography requires a host-installed serif font",
            required="a usable serif font or an explicit --font path",
            detected=f"{type(error).__name__}: {error}",
            how_to_fix="install a system serif font or pass --font explicitly to the compositor",
        )
    return _pass("Serif font", str(font_path))


def _check_pytest() -> CheckResult:
    try:
        pytest = importlib.import_module("pytest")
        return _pass("pytest", str(getattr(pytest, "__version__", "version unavailable")))
    except Exception as error:  # pragma: no cover - depends on the caller's environment
        return _fail(
            "pytest",
            detail="pytest could not be imported in development mode",
            what_failed="pytest development dependency",
            why="the repository test command cannot be reproduced from a fresh development environment",
            required="pytest==9.1.1 from requirements-dev.txt",
            detected=f"{type(error).__name__}: {error}",
            how_to_fix="python -m pip install -r requirements-dev.txt",
        )


def _check_dependency_contract(repo_root: Path) -> CheckResult:
    checker = repo_root / "tools" / "check_dependency_contract.py"
    if not checker.is_file():
        return _not_detectable("Dependency contract", "checker is not present in this checkout")
    ok, detail = _run_read_only_command([sys.executable, str(checker)], repo_root, 20)
    if ok:
        return _pass("Dependency contract", "all Python imports map to declared manifests")
    return _fail(
        "Dependency contract",
        detail="undeclared import or manifest error detected",
        what_failed="dependency/import consistency",
        why="a fresh environment would not have a declared dependency needed by the repository",
        required="python tools/check_dependency_contract.py exits 0",
        detected=detail or "non-zero exit code",
        how_to_fix="update the correct requirements manifest, then rerun the dependency checker",
    )


def _check_package_structure(repo_root: Path, strict: bool) -> CheckResult:
    checker = repo_root / "tools" / "check_package_parity.py"
    dist = repo_root / "dist"
    if not checker.is_file() or not dist.is_dir():
        if strict:
            return _fail(
                "Package structure",
                detail="package parity cannot be checked",
                what_failed="runtime artifact structure",
                why="the strict environment gate requires the formal runtime archives and parity checker",
                required="dist/ and tools/check_package_parity.py",
                detected=f"checker={checker.is_file()}, dist={dist.is_dir()}",
                how_to_fix="restore the formal dist archives and rerun python scripts/doctor.py --strict-packages",
            )
        return _not_detectable("Package structure", "dist/ or package parity checker is not present")
    ok, detail = _run_read_only_command([sys.executable, str(checker)], repo_root, 90)
    if ok:
        return _pass("Package structure", "formal runtime archives pass parity and clean extraction smoke")
    return _fail(
        "Package structure",
        detail="runtime archive parity or extraction smoke failed",
        what_failed="runtime package structure",
        why="a release archive may be stale, incomplete, or not runnable after extraction",
        required="python tools/check_package_parity.py exits 0",
        detected=detail or "non-zero exit code",
        how_to_fix="rebuild the current package, inspect its exact entries, and rerun the package parity check",
    )


def run_checks(
    repo_root: Path = REPO_ROOT,
    *,
    development: bool = False,
    strict_packages: bool = False,
) -> list[CheckResult]:
    repo_root = Path(repo_root).resolve()
    pillow_result, _pillow = _load_pillow()
    results = [
        _check_platform(),
        _check_python(),
        pillow_result,
        _check_required_imports(),
        _check_temp_directory(),
        _check_image_codecs(),
        _check_project_files(repo_root, development),
        _check_validator(repo_root),
        _check_serif_font(repo_root),
        _check_dependency_contract(repo_root),
        _check_package_structure(repo_root, strict_packages),
    ]
    if development:
        results.append(_check_pytest())
    return results


def overall_pass(results: list[CheckResult]) -> bool:
    return all(result.status != "FAIL" for result in results)


def render_report(results: list[CheckResult]) -> str:
    lines = [
        f"LOCAL ENVIRONMENT: {'PASS' if overall_pass(results) else 'FAIL'}",
        *[render_check(result) for result in results],
        "HOST CAPABILITIES:",
        "Visual understanding: NOT DETECTABLE — host capability, not a pip dependency",
        "Image generation: REQUIRED FOR Strict Fidelity — host capability, not a pip dependency",
        "Native image editing: OPTIONAL / REQUIRED BY MODE — host capability, not a pip dependency",
        "Filesystem access: PASS — local filesystem is available to this process",
    ]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--development",
        action="store_true",
        help="also check requirements-dev.txt and import pytest",
    )
    parser.add_argument(
        "--strict-packages",
        action="store_true",
        help="fail when formal runtime archives cannot be checked",
    )
    args = parser.parse_args(argv)
    results = run_checks(
        development=args.development,
        strict_packages=args.strict_packages,
    )
    print("Environment Contract: " + ("PASS" if overall_pass(results) else "FAIL"))
    print(render_report(results))
    if not overall_pass(results):
        print("FAIL: see the actionable WHAT FAILED / WHY / REQUIRED / DETECTED / HOW TO FIX details above")
    return 0 if overall_pass(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
