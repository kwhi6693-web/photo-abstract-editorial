from __future__ import annotations

import importlib.util
import json
import re
import subprocess
import sys
import tempfile
import unittest
from zipfile import ZipFile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
TEXT_RUNTIME_SUFFIXES = {".json", ".md", ".py", ".yaml", ".yml"}


def canonical_runtime_bytes(path: Path) -> bytes:
    data = path.read_bytes()
    if path.suffix.lower() in TEXT_RUNTIME_SUFFIXES:
        return data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return data


def load_package_builder():
    builder_path = REPO_ROOT / "tools" / "build_skill_package.py"
    spec = importlib.util.spec_from_file_location("build_skill_package", builder_path)
    if spec is None or spec.loader is None:
        raise AssertionError("could not load build_skill_package")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class SkillPackageTests(unittest.TestCase):
    def test_public_readme_is_bilingual_and_documents_github_install(self) -> None:
        """Catch publishing a README that omits either audience or the reusable install path."""
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("[中文](#中文)", readme)
        self.assertIn("[English](#english)", readme)
        self.assertIn("kwhi6693-web/photo-abstract-editorial", readme)
        self.assertIn("dist/photo-abstract-editorial-skill.zip", readme)
        self.assertIn("公开仓库", readme)
        self.assertIn("Public repository", readme)

    def test_release_archive_contains_current_nine_runtime_files(self) -> None:
        """Catch a public download that is stale, incomplete, or contains development files."""
        archive = REPO_ROOT / "dist" / "photo-abstract-editorial-skill.zip"
        self.assertTrue(archive.is_file())
        expected = {
            "photo-abstract-editorial/SKILL.md",
            "photo-abstract-editorial/agents/openai.yaml",
            "photo-abstract-editorial/assets/examples/source-horizon.png",
            "photo-abstract-editorial/assets/examples/result-horizon.png",
            "photo-abstract-editorial/assets/examples/result-horizon.png.manifest.json",
            "photo-abstract-editorial/references/art-direction.md",
            "photo-abstract-editorial/references/example-pair.md",
            "photo-abstract-editorial/scripts/compose_editorial.py",
            "photo-abstract-editorial/scripts/validate_editorial.py",
        }
        with ZipFile(archive) as handle:
            actual = {name for name in handle.namelist() if not name.endswith("/")}
            self.assertEqual(actual, expected)
            for archive_name in sorted(expected):
                with self.subTest(archive_name=archive_name):
                    relative_path = archive_name.removeprefix("photo-abstract-editorial/")
                    self.assertEqual(
                        handle.read(archive_name),
                        canonical_runtime_bytes(REPO_ROOT / relative_path),
                    )

    def test_package_builder_verifies_current_archive(self) -> None:
        """Catch release packaging that cannot be reproduced and checked deterministically."""
        builder = REPO_ROOT / "tools" / "build_skill_package.py"
        self.assertTrue(builder.is_file())
        completed = subprocess.run(
            [sys.executable, str(builder), "--check"],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr or completed.stdout)

    def test_package_verifier_reports_a_corrupt_archive(self) -> None:
        """Catch a damaged public download escaping as an unhandled traceback."""
        builder = load_package_builder()
        with tempfile.TemporaryDirectory() as temporary_directory:
            archive = Path(temporary_directory) / "corrupt.zip"
            archive.write_bytes(b"not-a-zip")
            errors = builder.verify_archive(archive)
        self.assertEqual(len(errors), 1)
        self.assertIn("archive cannot be read", errors[0])

    def test_public_repo_ignores_local_build_workspace(self) -> None:
        """Catch generated evaluation files being accidentally published with the skill."""
        ignore_path = REPO_ROOT / ".gitignore"
        self.assertTrue(ignore_path.is_file())
        ignored = ignore_path.read_text(encoding="utf-8").splitlines()
        self.assertIn("work/", ignored)
        self.assertIn("__pycache__/", ignored)

    def test_skill_is_concise_and_discoverable(self) -> None:
        """Catch bloated instructions or metadata that no longer triggers correctly."""
        text = (REPO_ROOT / "SKILL.md").read_text(encoding="utf-8")
        parts = text.split("---", 2)
        self.assertEqual(len(parts), 3)
        frontmatter, body = parts[1], parts[2]
        self.assertRegex(frontmatter, r"(?m)^name: photo-abstract-editorial$")
        self.assertRegex(frontmatter, r"(?m)^description: Use when ")
        self.assertLessEqual(len(body.split()), 500)

    def test_ui_default_prompt_invokes_the_skill(self) -> None:
        """Catch a skill chip that inserts a generic prompt and skips the workflow."""
        metadata = (REPO_ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn("$photo-abstract-editorial", metadata)

    def test_runtime_references_are_single_source_and_complete(self) -> None:
        """Catch translation drift or packaging without the promised example."""
        references = REPO_ROOT / "references"
        self.assertTrue((references / "art-direction.md").is_file())
        self.assertTrue((references / "example-pair.md").is_file())
        self.assertFalse((references / "photo-abstract-editorial-prompt.zh-CN.md").exists())
        self.assertFalse((references / "photo-abstract-editorial-prompt.en.md").exists())
        self.assertLessEqual(len((references / "art-direction.md").read_text(encoding="utf-8").splitlines()), 100)

    def test_markdown_links_from_skill_exist(self) -> None:
        """Catch renamed or omitted runtime references before packaging."""
        skill = (REPO_ROOT / "SKILL.md").read_text(encoding="utf-8")
        targets = re.findall(r"\[[^]]+\]\(([^)]+)\)", skill)
        self.assertGreaterEqual(len(targets), 2)
        for target in targets:
            with self.subTest(target=target):
                self.assertTrue((REPO_ROOT / target).is_file())

    def test_runtime_scripts_expose_cli_help(self) -> None:
        """Catch packaged scripts that cannot be invoked by an agent."""
        for name in ("compose_editorial.py", "validate_editorial.py"):
            with self.subTest(name=name):
                completed = subprocess.run(
                    [sys.executable, str(REPO_ROOT / "scripts" / name), "--help"],
                    check=False,
                    capture_output=True,
                    text=True,
                )
                self.assertEqual(completed.returncode, 0, completed.stderr)
                self.assertIn("usage:", completed.stdout.lower())

    def test_example_demonstrates_the_v4_layout_contract(self) -> None:
        """Catch losing the restrained vertical anchors or the accepted optical layout."""
        manifest_path = REPO_ROOT / "assets" / "examples" / "result-horizon.png.manifest.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        art_direction = (REPO_ROOT / "references" / "art-direction.md").read_text(encoding="utf-8")
        skill = (REPO_ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertEqual(manifest["motif"]["file_name"], "motif-horizon-v4.png")
        self.assertIn("one primary and one subordinate vertical anchor", art_direction)
        self.assertIn("one primary and one subordinate irregular vertical stroke", skill)
        self.assertEqual(manifest["output"]["size"], [1023, 1296])
        self.assertEqual(manifest["panel"], {"color": "#E8E1D5", "height": 576, "y": 720})
        self.assertEqual(manifest["layout_grid"]["inset"], 72)
        self.assertEqual(manifest["motif_region"]["x"], 72)
        self.assertEqual(manifest["typography"]["title_anchor_x"], 84)
        self.assertEqual(manifest["typography"]["bottom_inset"], 118)
        self.assertEqual(manifest["typography"]["title_font_size"], 42)
        self.assertEqual(manifest["typography"]["kerning_mode"], "whole-run")
        runs = manifest["typography"]["title_runs"]
        self.assertEqual("".join(run["text"] for run in runs), "Emberline at Dusk")
        self.assertEqual([run["style"] for run in runs], ["primary", "accent", "primary"])
        self.assertEqual(runs[1]["font_size"], 29)
        self.assertGreaterEqual(manifest["motif"]["cleanup"]["removed_pixels"], 1)


if __name__ == "__main__":
    unittest.main()
