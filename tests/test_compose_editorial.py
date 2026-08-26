from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image, ImageDraw


REPO_ROOT = Path(__file__).resolve().parents[1]
COMPOSER_PATH = REPO_ROOT / "scripts" / "compose_editorial.py"


def load_composer():
    if not COMPOSER_PATH.is_file():
        raise AssertionError(f"missing production script: {COMPOSER_PATH}")
    spec = importlib.util.spec_from_file_location("compose_editorial", COMPOSER_PATH)
    if spec is None or spec.loader is None:
        raise AssertionError("could not load compose_editorial")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def make_pattern(path: Path, size: tuple[int, int]) -> None:
    width, height = size
    pixels = [
        ((x * 17) % 256, (y * 31) % 256, ((x + y) * 11) % 256)
        for y in range(height)
        for x in range(width)
    ]
    image = Image.new("RGB", size)
    image.putdata(pixels)
    image.save(path)


def make_motif(path: Path) -> None:
    image = Image.new("RGBA", (40, 24), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((2, 4, 37, 19), radius=4, fill=(126, 48, 55, 220))
    image.save(path)


def make_speckled_motif(path: Path) -> None:
    image = Image.new("RGBA", (60, 24), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.rectangle((5, 9, 54, 14), fill=(112, 42, 52, 255))
    draw.rectangle((0, 0, 1, 1), fill=(0, 255, 255, 255))
    draw.rectangle((58, 22, 59, 23), fill=(0, 255, 0, 255))
    image.save(path)


class ComposeEditorialTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        self.source = self.root / "source.png"
        self.motif = self.root / "motif.png"
        self.output = self.root / "result.png"
        make_pattern(self.source, (120, 80))
        make_motif(self.motif)

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def compose(self, **overrides):
        module = load_composer()
        options = module.CompositionOptions(
            title="Measured Horizon",
            title_color="#6B2737",
            **overrides,
        )
        return module.compose(self.source, self.motif, self.output, options)

    def test_default_composition_preserves_every_source_pixel(self) -> None:
        """Catch any implementation that redraws, crops, or mutates the source region."""
        manifest = self.compose()

        with Image.open(self.source) as source, Image.open(self.output) as result:
            self.assertEqual(result.size[0], source.size[0])
            actual_photo = result.convert("RGB").crop((0, 0, source.width, source.height))
            self.assertEqual(actual_photo.tobytes(), source.convert("RGB").tobytes())
        self.assertTrue(manifest["photo_region"]["pixel_exact"])

    def test_auto_panel_height_matches_orientation_contract(self) -> None:
        """Catch a regression to a mechanical half-and-half canvas."""
        module = load_composer()
        cases = [
            ((120, 80), 64),
            ((100, 100), 70),
            ((80, 120), 66),
        ]
        for index, (size, expected_panel_height) in enumerate(cases):
            with self.subTest(size=size):
                source = self.root / f"source-{index}.png"
                output = self.root / f"result-{index}.png"
                make_pattern(source, size)
                options = module.CompositionOptions(title="Axis")
                manifest = module.compose(source, self.motif, output, options)
                self.assertEqual(manifest["panel"]["height"], expected_panel_height)
                with Image.open(output) as image:
                    self.assertEqual(image.height, size[1] + expected_panel_height)

    def test_panel_corners_are_exact_uniform_ivory(self) -> None:
        """Catch gradients, texture, or motif/text bleeding into the panel boundary."""
        manifest = self.compose()
        photo_height = manifest["photo_region"]["height"]
        with Image.open(self.output) as image:
            rgb = image.convert("RGB")
            corners = [
                rgb.getpixel((0, photo_height)),
                rgb.getpixel((rgb.width - 1, photo_height)),
                rgb.getpixel((0, rgb.height - 1)),
                rgb.getpixel((rgb.width - 1, rgb.height - 1)),
            ]
        self.assertEqual(corners, [(232, 225, 213)] * 4)

    def test_lower_left_grid_aligns_motif_and_title_anchors(self) -> None:
        """Catch the motif drifting back to an unrelated centered grid."""
        manifest = self.compose()
        self.assertEqual(manifest["layout_profile"], "lower-editorial")
        self.assertEqual(manifest["layout_grid"]["inset"], 8)
        self.assertEqual(manifest["motif_region"]["x"], 8)
        self.assertEqual(manifest["typography"]["title_anchor_x"], 9)
        self.assertEqual(manifest["typography"]["bottom_inset"], 14)

        centered_output = self.root / "centered.png"
        module = load_composer()
        options = module.CompositionOptions(title="Measured Horizon", motif_center_x=0.75)
        centered = module.compose(self.source, self.motif, centered_output, options)
        region = centered["motif_region"]
        self.assertNotEqual(region["x"], 8)
        self.assertAlmostEqual(region["x"] + region["width"] / 2, 90, delta=1)

    def test_v3_layout_profiles_keep_motif_and_typography_inside_the_panel(self) -> None:
        """Catch a new profile placing visual content outside the deterministic panel geometry."""
        module = load_composer()
        profiles = (
            "lower-editorial",
            "wide-horizon",
            "vertical-monument",
            "centered-archive",
            "sparse-object",
        )
        for profile in profiles:
            with self.subTest(profile=profile):
                output = self.root / f"{profile}.png"
                manifest = module.compose(
                    self.source,
                    self.motif,
                    output,
                    module.CompositionOptions(title="Measured Horizon", layout=profile),
                )
                panel_y = manifest["panel"]["y"]
                panel_bottom = panel_y + manifest["panel"]["height"]
                motif = manifest["motif_region"]
                title = manifest["typography"]["title_region"]
                self.assertEqual(manifest["layout_profile"], profile)
                self.assertGreaterEqual(motif["x"], 0)
                self.assertGreaterEqual(motif["y"], panel_y)
                self.assertLessEqual(motif["x"] + motif["width"], manifest["output"]["size"][0])
                self.assertLessEqual(motif["y"] + motif["height"], panel_bottom)
                self.assertGreaterEqual(title["x"], 0)
                self.assertGreaterEqual(title["y"], panel_y)
                self.assertLessEqual(title["x"] + title["width"], manifest["output"]["size"][0])
                self.assertLessEqual(title["y"] + title["height"], panel_bottom)

    def test_layout_selection_is_deterministic_from_scene_facts(self) -> None:
        """Catch random or subject-blind layout selection in the local routing helper."""
        module = load_composer()
        cases = [
            ({"scene_profile": "landscape", "dominant_axis": "horizontal"}, "wide-horizon"),
            ({"scene_profile": "pure-portrait", "dominant_axis": "vertical"}, "vertical-monument"),
            ({"scene_profile": "architecture", "subject_location": "center"}, "centered-archive"),
            ({"scene_profile": "still-life", "negative_space": "generous"}, "sparse-object"),
            ({"scene_profile": "street-crowd", "dominant_axis": "mixed"}, "lower-editorial"),
        ]
        for facts, expected in cases:
            with self.subTest(facts=facts):
                self.assertEqual(module.select_layout_profile(**facts), expected)

    def test_legacy_layout_names_remain_supported(self) -> None:
        """Catch a V3 profile migration that breaks existing lower-left and bottom-center callers."""
        module = load_composer()
        for layout in ("lower-left", "bottom-center"):
            with self.subTest(layout=layout):
                output = self.root / f"legacy-{layout}.png"
                manifest = module.compose(
                    self.source,
                    self.motif,
                    output,
                    module.CompositionOptions(title="Measured Horizon", layout=layout),
                )
                self.assertIn(manifest["layout_profile"], {"lower-editorial", "centered-archive"})

    def test_isolated_alpha_components_are_removed_before_compositing(self) -> None:
        """Catch chroma-key specks surviving as cyan or green dots on the panel."""
        speckled = self.root / "speckled.png"
        output = self.root / "cleaned.png"
        make_speckled_motif(speckled)
        module = load_composer()
        manifest = module.compose(
            self.source,
            speckled,
            output,
            module.CompositionOptions(title="Measured Horizon"),
        )

        cleanup = manifest["motif"]["cleanup"]
        self.assertGreaterEqual(cleanup["removed_components"], 2)
        self.assertGreater(cleanup["removed_pixels"], 0)
        with Image.open(output) as result:
            panel = result.convert("RGB").crop((0, 80, result.width, result.height))
            cyan_or_green = [
                pixel
                for pixel in panel.get_flattened_data()
                if pixel[1] > 150 and pixel[0] < 100 and (pixel[2] > 130 or pixel[2] < 100)
            ]
        self.assertEqual(cyan_or_green, [])

    def test_manifest_records_exact_title_and_hashes(self) -> None:
        """Catch generated or lossy title handling and unverifiable outputs."""
        manifest = self.compose(subtitle="A study in distance")
        manifest_path = self.output.with_suffix(self.output.suffix + ".manifest.json")
        self.assertTrue(manifest_path.is_file())
        disk_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        self.assertEqual(disk_manifest, manifest)
        self.assertEqual(manifest["typography"]["title"], "Measured Horizon")
        self.assertEqual(manifest["typography"]["subtitle"], "A study in distance")
        self.assertEqual(len(manifest["source"]["sha256"]), 64)
        self.assertEqual(len(manifest["output"]["sha256"]), 64)

    def test_title_accent_uses_smaller_italic_whole_word_run(self) -> None:
        """Catch a connector being rendered with the same rigid face as the main title."""
        source = self.root / "accent-source.png"
        output = self.root / "accent-result.png"
        Image.new("RGB", (400, 240), (31, 28, 30)).save(source)
        module = load_composer()
        manifest = module.compose(
            source,
            self.motif,
            output,
            module.CompositionOptions(title="Measured at Horizon", title_accent="at"),
        )

        typography = manifest["typography"]
        runs = typography["title_runs"]
        self.assertEqual("".join(run["text"] for run in runs), "Measured at Horizon")
        self.assertEqual([run["style"] for run in runs], ["primary", "accent", "primary"])
        self.assertLess(runs[1]["font_size"], runs[0]["font_size"])
        self.assertTrue(runs[1]["font_file"].lower().endswith(("i.ttf", "italic.ttf")))
        self.assertEqual(typography["kerning_mode"], "whole-run")

    def test_title_accent_must_be_one_complete_word_occurrence(self) -> None:
        """Catch ambiguous or mid-word accent styling that changes unintended letters."""
        module = load_composer()
        cases = [
            ("Measured Horizon", "at"),
            ("at at", "at"),
            ("Afterglow", "After"),
            ("at", "at"),
        ]
        for title, accent in cases:
            with self.subTest(title=title, accent=accent):
                options = module.CompositionOptions(title=title, title_accent=accent)
                with self.assertRaises(ValueError):
                    module.compose(self.source, self.motif, self.output, options)

    def test_typography_is_restrained_and_stays_inside_the_panel(self) -> None:
        """Catch oversized or misplaced title blocks that overpower the composition."""
        source = self.root / "large-source.png"
        output = self.root / "large-result.png"
        Image.new("RGB", (400, 240), (31, 28, 30)).save(source)
        module = load_composer()
        manifest = module.compose(
            source,
            self.motif,
            output,
            module.CompositionOptions(title="Measured Horizon"),
        )
        panel = manifest["panel"]
        typography = manifest["typography"]
        self.assertIn("title_region", typography)
        self.assertIn("title_font_size", typography)
        title_region = typography["title_region"]
        self.assertLessEqual(typography["title_font_size"], 16)
        self.assertEqual(typography["kerning_mode"], "whole-run")
        self.assertNotIn("title_tracking_px", typography)
        self.assertEqual(typography["title_anchor_x"], 33)
        self.assertEqual(typography["bottom_inset"], 46)
        self.assertGreaterEqual(title_region["y"], panel["y"])
        self.assertLessEqual(title_region["y"] + title_region["height"], manifest["output"]["size"][1])
        self.assertLessEqual(title_region["width"], round(manifest["output"]["size"][0] * 0.85))

    def test_empty_or_multiline_title_is_rejected(self) -> None:
        """Catch silent delivery without a title or with injected extra lines."""
        module = load_composer()
        for title in ("", "Line one\nLine two"):
            with self.subTest(title=title):
                options = module.CompositionOptions(title=title)
                with self.assertRaises(ValueError):
                    module.compose(self.source, self.motif, self.output, options)

    def test_nonpositive_explicit_panel_height_is_rejected(self) -> None:
        """Catch an explicit zero height being silently replaced by the automatic default."""
        module = load_composer()
        options = module.CompositionOptions(title="Measured Horizon", panel_height=0)
        with self.assertRaises(ValueError):
            module.compose(self.source, self.motif, self.output, options)

    def test_missing_inputs_are_rejected_before_output(self) -> None:
        """Catch partial compositions created from missing source or motif files."""
        module = load_composer()
        options = module.CompositionOptions(title="Measured Horizon")
        with self.assertRaises(FileNotFoundError):
            module.compose(self.root / "missing.png", self.motif, self.output, options)
        with self.assertRaises(FileNotFoundError):
            module.compose(self.source, self.root / "missing-motif.png", self.output, options)

    def test_output_cannot_replace_an_input_image(self) -> None:
        """Catch an output collision destroying the source photograph or motif."""
        module = load_composer()
        options = module.CompositionOptions(title="Measured Horizon")
        for input_path in (self.source, self.motif):
            with self.subTest(input_path=input_path.name):
                original_bytes = input_path.read_bytes()
                with self.assertRaisesRegex(ValueError, "input image"):
                    module.compose(self.source, self.motif, input_path, options)
                self.assertEqual(input_path.read_bytes(), original_bytes)

    def test_existing_output_is_not_overwritten(self) -> None:
        """Catch reruns silently replacing an existing user-visible result."""
        module = load_composer()
        options = module.CompositionOptions(title="Measured Horizon")
        original_bytes = b"existing-result"
        self.output.write_bytes(original_bytes)

        with self.assertRaises(FileExistsError):
            module.compose(self.source, self.motif, self.output, options)

        self.assertEqual(self.output.read_bytes(), original_bytes)


if __name__ == "__main__":
    unittest.main()
