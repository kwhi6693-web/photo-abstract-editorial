#!/usr/bin/env python3
"""Fail when Python imports are not declared by the repository dependency manifests."""

from __future__ import annotations

import ast
from pathlib import Path
import re
import sys


REPO_ROOT = Path(__file__).resolve().parents[1]
RUNTIME_MANIFEST = "requirements.txt"
DEVELOPMENT_MANIFEST = "requirements-dev.txt"
IMPORT_DISTRIBUTION_OVERRIDES = {"PIL": "Pillow"}
SKIPPED_DIRECTORY_NAMES = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    "coverage",
    "htmlcov",
}


def normalise_distribution(name: str) -> str:
    """Normalise a PyPI distribution name using PEP 503's comparison form."""
    return re.sub(r"[-_.]+", "-", name).lower()


def _requirement_include(line: str) -> str | None:
    match = re.match(r"^(?:-r|--requirement)(?:\s+|=)(.+)$", line, flags=re.IGNORECASE)
    return match.group(1).strip() if match else None


def _requirement_name(line: str) -> str | None:
    if line.startswith("-"):
        return None
    match = re.match(r"^([A-Za-z0-9][A-Za-z0-9_.-]*)(?:\[[^]]+\])?\s*(?:[<>=!~].*)?$", line)
    return match.group(1) if match else None


def read_declared_distributions(manifest: Path, seen: set[Path] | None = None) -> tuple[set[str], list[str]]:
    """Read a requirements file and its local ``-r`` includes."""
    seen = set() if seen is None else seen
    manifest = manifest.resolve()
    if manifest in seen:
        return set(), [f"dependency manifest include cycle: {manifest}"]
    if not manifest.is_file():
        return set(), [f"dependency manifest is missing: {manifest}"]

    seen.add(manifest)
    declared: set[str] = set()
    errors: list[str] = []
    for line_number, raw_line in enumerate(manifest.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw_line.split("#", 1)[0].strip()
        if not line:
            continue
        include = _requirement_include(line)
        if include is not None:
            include_path = (manifest.parent / include).resolve()
            included, include_errors = read_declared_distributions(include_path, seen)
            declared.update(included)
            errors.extend(include_errors)
            continue
        name = _requirement_name(line)
        if name is None:
            errors.append(
                f"{manifest}:{line_number}: unsupported dependency declaration: {raw_line.strip()}"
            )
            continue
        declared.add(normalise_distribution(name))
    return declared, errors


def iter_python_files(repo_root: Path) -> list[Path]:
    files: list[Path] = []
    for path in sorted(repo_root.rglob("*.py")):
        if any(part in SKIPPED_DIRECTORY_NAMES for part in path.relative_to(repo_root).parts):
            continue
        files.append(path)
    return files


def _local_top_level_modules(repo_root: Path) -> set[str]:
    modules = {path.name for path in repo_root.iterdir() if path.is_dir()}
    modules.update(path.stem for path in repo_root.glob("*.py"))
    for path in iter_python_files(repo_root):
        relative = path.relative_to(repo_root)
        if relative.parts:
            modules.add(relative.parts[0])
    return modules


def _stdlib_top_level_modules() -> set[str]:
    names = getattr(sys, "stdlib_module_names", ())
    return set(names) | {"__future__"}


def _imports_from(path: Path) -> list[tuple[str, int]]:
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except (OSError, SyntaxError) as error:
        raise ValueError(f"cannot parse Python file: {path}: {error}") from error

    imports: list[tuple[str, int]] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend((alias.name.split(".", 1)[0], node.lineno) for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
            imports.append((node.module.split(".", 1)[0], node.lineno))
    return imports


def _diagnostic(
    *,
    path: Path,
    line_number: int,
    imported: str,
    distribution: str,
    scope: str,
) -> str:
    return (
        f"{path}:{line_number}: undeclared third-party import '{imported}' "
        f"(distribution '{distribution}')\n"
        f"WHAT FAILED: {imported} is imported without a declared {scope} dependency\n"
        "WHY: a fresh environment would fail before the workflow can run\n"
        f"REQUIRED: declare '{distribution}' in the {scope} manifest\n"
        f"DETECTED: {path}:{line_number}\n"
        f"HOW TO FIX: add the pinned distribution to requirements.txt or requirements-dev.txt, then rerun this check"
    )


def check_dependency_contract(repo_root: Path = REPO_ROOT) -> list[str]:
    """Return actionable errors for missing or mis-scoped dependencies."""
    repo_root = Path(repo_root).resolve()
    runtime, runtime_errors = read_declared_distributions(repo_root / RUNTIME_MANIFEST)
    development, development_errors = read_declared_distributions(repo_root / DEVELOPMENT_MANIFEST)
    errors = [*runtime_errors, *development_errors]
    if runtime_errors or development_errors:
        return errors

    stdlib = _stdlib_top_level_modules()
    local_modules = _local_top_level_modules(repo_root)
    for path in iter_python_files(repo_root):
        relative = path.relative_to(repo_root)
        is_runtime = relative.parts[:1] == ("scripts",)
        declared = runtime if is_runtime else development
        scope = "runtime manifest" if is_runtime else "development manifest"
        try:
            imports = _imports_from(path)
        except ValueError as error:
            errors.append(str(error))
            continue
        for imported, line_number in imports:
            if imported in stdlib or imported in local_modules:
                continue
            distribution = IMPORT_DISTRIBUTION_OVERRIDES.get(imported, imported)
            if normalise_distribution(distribution) not in declared:
                errors.append(
                    _diagnostic(
                        path=relative,
                        line_number=line_number,
                        imported=imported,
                        distribution=distribution,
                        scope=scope,
                    )
                )
    return errors


def main(argv: list[str] | None = None) -> int:
    del argv
    errors = check_dependency_contract()
    if errors:
        print("DEPENDENCY CONTRACT: FAIL")
        for error in errors:
            print(error)
        return 1

    runtime, _ = read_declared_distributions(REPO_ROOT / RUNTIME_MANIFEST)
    development, _ = read_declared_distributions(REPO_ROOT / DEVELOPMENT_MANIFEST)
    print("DEPENDENCY CONTRACT: PASS")
    print(f"Runtime distributions: {', '.join(sorted(runtime))}")
    print(f"Development distributions: {', '.join(sorted(development))}")
    print("Third-party import mapping: PIL -> Pillow")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
