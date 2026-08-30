#!/usr/bin/env python3
"""Check tracked repository files for secrets, private paths, and local debris."""

from __future__ import annotations

from pathlib import Path
import re
import subprocess


REPO_ROOT = Path(__file__).resolve().parents[1]
SKIPPED_TEXT_SUFFIXES = {".png", ".jpg", ".jpeg", ".zip", ".gif", ".webp", ".ico", ".ttf", ".ttc"}
FORBIDDEN_DIRECTORY_NAMES = {
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    "coverage",
    "htmlcov",
    ".idea",
    ".vscode",
}
FORBIDDEN_FILE_NAMES = {".ds_store", "thumbs.db", ".coverage"}
SENSITIVE_PATTERNS = (
    re.compile(r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----"),
    re.compile(r"\bghp_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._-]{20,}"),
    re.compile(
        r"(?i)\b(?:password|passwd|api[_-]?key|access[_-]?token)\s*[:=]\s*['\"]?[^\s'\"]{12,}"
    ),
)
PRIVATE_PATH_PATTERNS = (
    re.compile(r"(?i)(?:^|[\s(\[\"'=])(?:[a-z]:[\\/]Users[\\/][^\s)\]\\\"']+)"),
    re.compile(r"(?i)(?:^|[\s(\[\"'=])(?:[a-z]:[\\/]Documents[\\/][^\s)\]\\\"']+)"),
    re.compile(r"(?i)(?:^|[\s(\[\"'=])/(?:Users|home)/[^\s)\]\\\"']+"),
)


def contains_sensitive_content(text: str) -> bool:
    return any(pattern.search(text) for pattern in (*SENSITIVE_PATTERNS, *PRIVATE_PATH_PATTERNS))


def _tracked_files(repo_root: Path) -> list[str]:
    completed = subprocess.run(
        ["git", "-C", str(repo_root), "ls-files", "-z"],
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        detail = completed.stderr.decode(errors="replace").strip()
        raise RuntimeError(f"git ls-files failed: {detail}")
    return [item for item in completed.stdout.decode("utf-8").split("\0") if item]


def _path_error(relative: str) -> str | None:
    path = Path(relative)
    parts = {part.lower() for part in path.parts}
    if parts & FORBIDDEN_DIRECTORY_NAMES:
        return f"tracked local/development directory: {relative}"
    name = path.name.lower()
    if name in FORBIDDEN_FILE_NAMES:
        return f"tracked OS/local file: {relative}"
    if name.endswith((".pyc", ".pyo", ".tmp", ".temp")) or name.endswith(".coverage"):
        return f"tracked generated file: {relative}"
    return None


def audit_repository(repo_root: Path = REPO_ROOT, tracked_files: list[str] | None = None) -> list[str]:
    """Return hygiene errors for the tracked repository state."""
    repo_root = Path(repo_root).resolve()
    tracked_files = _tracked_files(repo_root) if tracked_files is None else tracked_files
    errors: list[str] = []
    for relative in tracked_files:
        path_error = _path_error(relative)
        if path_error:
            errors.append(path_error)
            continue
        path = repo_root / relative
        if path.suffix.lower() in SKIPPED_TEXT_SUFFIXES or not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        if contains_sensitive_content(text):
            errors.append(f"sensitive content or private path detected: {relative}")
    return errors


def main(argv: list[str] | None = None) -> int:
    del argv
    try:
        errors = audit_repository()
    except RuntimeError as error:
        print(f"REPOSITORY HYGIENE: FAIL\n{error}")
        return 1
    if errors:
        print("REPOSITORY HYGIENE: FAIL")
        for error in errors:
            print(error)
        return 1
    print("REPOSITORY HYGIENE: PASS")
    print("Tracked files contain no detected secrets, private user paths, or local debris.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
