# Validated Example Pair

## Source

![A dark landscape photograph with a narrow ember-colored horizon](../assets/examples/source-horizon.png)

This evaluation source was losslessly extracted from the photographic region of a legacy repository composite. It is included to demonstrate the strict workflow, not as a camera-original provenance claim.

## Result

![The source photograph above a shortened warm-ivory panel with a sparse left-aligned band motif and an optically spaced mixed-style serif title](../assets/examples/result-horizon.png)

The built-in image-generation path produced only the text-free band motif: a muted old-gold and oxblood palette, retained negative gaps, and two unequal vertical anchors derived from decisive structures in the source. The taller left anchor carries identity while the thinner right anchor acts as a quiet echo; both remain subordinate to the long bands and omit crossarms, wires, and literal infrastructure detail. `compose_editorial.py` removed isolated alpha components, placed the full source photograph, a uniform `#E8E1D5` panel, the transparent motif, and the exact title `Emberline at Dusk`. Bodoni whole-run shaping supplies natural kerning, while the single connector `at` uses a smaller matching italic and the title sits on an optical rather than mathematically equal margin. `validate_editorial.py` confirmed the source and output hashes, output geometry, panel corners, and exact equality of every decoded pixel in the photographic region.

Do not reuse this subject, palette, title, or layout for another photograph. A new result must derive its decisions from its own source image.
