from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image, ImageDraw


REPO_ROOT = Path(__file__).resolve().parents[1]
CLEANUP_PATH = REPO_ROOT / "scripts" / "remove_chroma_key.py"


def load_cleanup():
    if not CLEANUP_PATH.is_file():
        raise AssertionError(f"missing production script: {CLEANUP_PATH}")
    spec = importlib.util.spec_from_file_location("remove_chroma_key", CLEANUP_PATH)
    if spec is None or spec.loader is None:
        raise AssertionError("could not load remove_chroma_key")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class RemoveChromaKeyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        self.source = self.root / "motif-source.png"
        self.output = self.root / "motif-transparent.png"
        image = Image.new("RGBA", (32, 20), (0, 255, 255, 255))
        draw = ImageDraw.Draw(image)
        draw.rectangle((7, 6, 24, 13), fill=(124, 47, 57, 255))
        draw.point((1, 1), fill=(0, 255, 255, 255))
        draw.rectangle((25, 5, 26, 6), fill=(0, 245, 245, 255))
        image.save(self.source)

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def test_cleanup_removes_chroma_and_small_components_without_overwriting_input(self) -> None:
        """Catch a portable cleanup that leaves opaque chroma or mutates the motif source."""
        module = load_cleanup()
        original = self.source.read_bytes()
        report = module.clean_image(
            self.source,
            self.output,
            chroma_color="#00FFFF",
            tolerance=12,
            edge_softness=24,
            min_component_area=8,
        )

        self.assertEqual(self.source.read_bytes(), original)
        self.assertTrue(self.output.is_file())
        with Image.open(self.output) as opened:
            cleaned = opened.convert("RGBA")
        self.assertEqual(cleaned.getpixel((0, 0))[3], 0)
        self.assertEqual(cleaned.getpixel((1, 1))[3], 0)
        self.assertEqual(cleaned.getpixel((15, 9))[3], 255)
        self.assertEqual(cleaned.getpixel((25, 5))[3], 0)
        self.assertGreaterEqual(report["removed_pixels"], 1)
        self.assertEqual(report["output_mode"], "RGBA")

    def test_cleanup_reports_machine_readable_failure_for_bad_input(self) -> None:
        """Catch a CLI failure escaping as a traceback instead of structured JSON."""
        completed = subprocess.run(
            [
                sys.executable,
                str(CLEANUP_PATH),
                "--input",
                str(self.root / "missing.png"),
                "--output",
                str(self.output),
                "--color",
                "#00FFFF",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 1)
        self.assertEqual(completed.stderr, "")
        payload = json.loads(completed.stdout)
        self.assertFalse(payload["ok"])
        self.assertEqual(payload["error"], "input_not_found")

    def test_cleanup_rejects_existing_output_and_input_collision(self) -> None:
        """Catch a cleanup rerun that overwrites user files or destroys its input."""
        module = load_cleanup()
        self.output.write_bytes(b"existing")
        with self.assertRaises(FileExistsError):
            module.clean_image(self.source, self.output)
        with self.assertRaises(ValueError):
            module.clean_image(self.source, self.source)


if __name__ == "__main__":
    unittest.main()
