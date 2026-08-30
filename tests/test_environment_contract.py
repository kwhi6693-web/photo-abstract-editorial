from __future__ import annotations

from pathlib import Path
import tempfile
import unittest

from scripts import doctor
from tools import check_dependency_contract, check_package_parity, check_repository_hygiene


REPO_ROOT = Path(__file__).resolve().parents[1]


class DependencyContractTests(unittest.TestCase):
    def test_current_repository_has_a_complete_dependency_contract(self) -> None:
        errors = check_dependency_contract.check_dependency_contract(REPO_ROOT)
        self.assertEqual(errors, [])
        runtime, _ = check_dependency_contract.read_declared_distributions(REPO_ROOT / "requirements.txt")
        development, _ = check_dependency_contract.read_declared_distributions(REPO_ROOT / "requirements-dev.txt")
        self.assertIn("pillow", runtime)
        self.assertNotIn("pytest", runtime)
        self.assertIn("pytest", development)

    def test_undeclared_import_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "scripts").mkdir()
            (root / "tests").mkdir()
            (root / "tools").mkdir()
            (root / "requirements.txt").write_text("Pillow==12.3.0\n", encoding="utf-8")
            (root / "requirements-dev.txt").write_text(
                "-r requirements.txt\npytest==9.1.1\n",
                encoding="utf-8",
            )
            (root / "scripts" / "example.py").write_text(
                "import undeclared_image_library\n",
                encoding="utf-8",
            )

            errors = check_dependency_contract.check_dependency_contract(root)

        self.assertTrue(any("undeclared_image_library" in error for error in errors))

    def test_runtime_import_must_be_declared_in_runtime_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "scripts").mkdir()
            (root / "tests").mkdir()
            (root / "tools").mkdir()
            (root / "requirements.txt").write_text("\n", encoding="utf-8")
            (root / "requirements-dev.txt").write_text(
                "-r requirements.txt\nPillow==12.3.0\npytest==9.1.1\n",
                encoding="utf-8",
            )
            (root / "scripts" / "example.py").write_text(
                "from PIL import Image\n",
                encoding="utf-8",
            )

            errors = check_dependency_contract.check_dependency_contract(root)

        self.assertTrue(any("runtime manifest" in error for error in errors))


class PackageParityTests(unittest.TestCase):
    def test_current_runtime_artifacts_match_their_contracts(self) -> None:
        errors = check_package_parity.check_package_parity(REPO_ROOT, run_smoke=False)
        self.assertEqual(errors, [])


class DoctorContractTests(unittest.TestCase):
    def test_failure_report_is_actionable(self) -> None:
        result = doctor.CheckResult(
            name="Pillow",
            status="FAIL",
            detail="Pillow could not be imported",
            what_failed="Pillow import",
            why="the runtime dependency is unavailable",
            required="Pillow==12.3.0",
            detected="ModuleNotFoundError",
            how_to_fix="python -m pip install -r requirements.txt",
        )

        rendered = doctor.render_check(result)

        for label in ("WHAT FAILED", "WHY", "REQUIRED", "DETECTED", "HOW TO FIX"):
            with self.subTest(label=label):
                self.assertIn(label, rendered)


class RepositoryHygieneTests(unittest.TestCase):
    def test_gitignore_covers_local_environment_debris(self) -> None:
        ignored = (REPO_ROOT / ".gitignore").read_text(encoding="utf-8").splitlines()
        for entry in (".venv/", "venv/", "__pycache__/", "*.pyc", ".pytest_cache/", "coverage/", "htmlcov/"):
            with self.subTest(entry=entry):
                self.assertIn(entry, ignored)

    def test_secret_and_private_path_patterns_are_rejected(self) -> None:
        self.assertTrue(check_repository_hygiene.contains_sensitive_content("ghp_" + "A" * 36))
        private_path = "C:" + "\\" + "Users" + "\\" + "private" + "\\" + "repo"
        self.assertTrue(check_repository_hygiene.contains_sensitive_content(private_path))
        self.assertFalse(check_repository_hygiene.contains_sensitive_content("Pillow==12.3.0"))


if __name__ == "__main__":
    unittest.main()
