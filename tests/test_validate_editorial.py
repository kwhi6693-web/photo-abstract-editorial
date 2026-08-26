from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image

from tests.test_compose_editorial import load_composer, make_motif, make_pattern


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = REPO_ROOT / "scripts" / "validate_editorial.py"


def load_validator():
    if not VALIDATOR_PATH.is_file():
        raise AssertionError(f"missing production script: {VALIDATOR_PATH}")
    spec = importlib.util.spec_from_file_location("validate_editorial", VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise AssertionError("could not load validate_editorial")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


class ValidateEditorialTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        self.source = self.root / "source.png"
        self.other_source = self.root / "other-source.png"
        self.motif = self.root / "motif.png"
        self.output = self.root / "result.png"
        make_pattern(self.source, (120, 80))
        make_pattern(self.other_source, (121, 80))
        make_motif(self.motif)
        composer = load_composer()
        options = composer.CompositionOptions(title="Measured Horizon")
        self.manifest = composer.compose(self.source, self.motif, self.output, options)
        self.manifest_path = self.output.with_suffix(self.output.suffix + ".manifest.json")

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def test_valid_round_trip_passes_every_check(self) -> None:
        """Catch a validator that rejects output produced by the approved composer."""
        validator = load_validator()
        verdict = validator.validate(self.source, self.output, self.manifest_path)
        self.assertTrue(verdict["ok"])
        self.assertEqual(verdict["errors"], [])
        self.assertTrue(all(verdict["checks"].values()))

    def test_tampered_photo_region_is_rejected(self) -> None:
        """Catch delivery after even one photographic pixel changes."""
        validator = load_validator()
        with Image.open(self.output) as opened:
            image = opened.convert("RGB")
        image.putpixel((0, 0), (255, 255, 255))
        image.save(self.output)

        verdict = validator.validate(self.source, self.output, self.manifest_path)

        self.assertFalse(verdict["ok"])
        self.assertIn("photo_region_pixels", verdict["errors"])

    def test_stale_output_hash_is_rejected(self) -> None:
        """Catch a manifest copied from a different or older composition."""
        validator = load_validator()
        payload = json.loads(self.manifest_path.read_text(encoding="utf-8"))
        payload["output"]["sha256"] = "0" * 64
        self.manifest_path.write_text(json.dumps(payload), encoding="utf-8")

        verdict = validator.validate(self.source, self.output, self.manifest_path)

        self.assertFalse(verdict["ok"])
        self.assertIn("output_sha256", verdict["errors"])

    def test_wrong_source_is_rejected(self) -> None:
        """Catch validating a composition against the wrong uploaded photograph."""
        validator = load_validator()
        verdict = validator.validate(self.other_source, self.output, self.manifest_path)
        self.assertFalse(verdict["ok"])
        self.assertIn("source_sha256", verdict["errors"])

    def test_modified_panel_corner_is_rejected_even_with_fresh_output_hash(self) -> None:
        """Catch non-uniform backgrounds independently of stale-hash detection."""
        validator = load_validator()
        with Image.open(self.output) as opened:
            image = opened.convert("RGB")
        panel_y = self.manifest["panel"]["y"]
        image.putpixel((0, panel_y), (1, 2, 3))
        image.save(self.output)
        payload = json.loads(self.manifest_path.read_text(encoding="utf-8"))
        payload["output"]["sha256"] = sha256_file(self.output)
        self.manifest_path.write_text(json.dumps(payload), encoding="utf-8")

        verdict = validator.validate(self.source, self.output, self.manifest_path)

        self.assertFalse(verdict["ok"])
        self.assertIn("panel_corner_color", verdict["errors"])

    def test_declared_motif_outside_panel_is_rejected(self) -> None:
        """Catch a manifest that claims a layout region outside the deterministic panel."""
        validator = load_validator()
        payload = json.loads(self.manifest_path.read_text(encoding="utf-8"))
        payload["motif_region"]["y"] = payload["panel"]["y"] - 1
        self.manifest_path.write_text(json.dumps(payload), encoding="utf-8")

        verdict = validator.validate(self.source, self.output, self.manifest_path)

        self.assertFalse(verdict["ok"])
        self.assertIn("motif_region_geometry", verdict["errors"])

    def test_cli_exit_code_and_json_match_verdict(self) -> None:
        """Catch a CLI that prints success but returns the wrong process status."""
        completed = subprocess.run(
            [
                sys.executable,
                str(VALIDATOR_PATH),
                "--source",
                str(self.source),
                "--output",
                str(self.output),
                "--manifest",
                str(self.manifest_path),
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertTrue(json.loads(completed.stdout)["ok"])

    def test_cli_reports_machine_readable_failure_for_malformed_manifest(self) -> None:
        """Catch invalid delivery metadata escaping as a traceback instead of JSON."""
        self.manifest_path.write_text('{"source": []}', encoding="utf-8")

        completed = subprocess.run(
            [
                sys.executable,
                str(VALIDATOR_PATH),
                "--source",
                str(self.source),
                "--output",
                str(self.output),
                "--manifest",
                str(self.manifest_path),
            ],
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertEqual(completed.returncode, 1)
        verdict = json.loads(completed.stdout)
        self.assertFalse(verdict["ok"])
        self.assertEqual(verdict["errors"], ["validation_exception"])
        self.assertIn("AttributeError", verdict["detail"])
        self.assertEqual(completed.stderr, "")


if __name__ == "__main__":
    unittest.main()
