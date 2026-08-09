---
name: photo-abstract-editorial
description: Use when one photograph must become a vertical photo-plus-abstraction editorial, visual memory panel, archival poster, or abstract diptych while the photographic region remains verifiably unchanged.
---

# Photo Abstract Editorial

Create one verified composition from one photograph. Generate only the motif; assemble photo, panel, and typography deterministically.

**REQUIRED SUB-SKILL:** Use imagegen for motif generation. Never ask imagegen to generate the finished composite or its typography.

## Contract

- **Invariants:** one readable photo; full source retained by default; no unrelated content or generated text; machine and visual validation required.
- **Defaults:** shortened warm-ivory panel, lower-left optical grid, muted ink palette, one English title, no subtitle, high-contrast serif with native whole-run kerning.
- **Overrides:** accept panel, motif, text, alignment, and font choices. Reject source redrawing or invented content.

## Workflow

1. Require one photograph; ask if missing. Inspect local input with `view_image`.
2. Read [references/art-direction.md](references/art-direction.md). Identify three to six source facts; choose panel ratio, mark family, muted palette, and exact title.
3. Label the source **reference image**, not edit target. Generate a sparse motif on flat chroma key: two to four bands and one dark structure. If decisive vertical structure appears, add one primary and one subordinate irregular vertical stroke, unequal in height and width; otherwise use negative gaps or band offsets. Use muted source colors. Forbid literal infrastructure, recognizable tracing, dots, photo, text, swatch, logo, frame, shadow, and texture.
4. Save the motif source. Use imagegen's installed `remove_chroma_key.py`; validate alpha, corners, palette, edges, and no chroma specks. CLI/model fallback requires user approval.
5. Resolve absolute Python via `codex_app__load_workspace_dependencies`. Run compositor `--help`, then pass source, transparent motif, a new PNG output path, and exact title. Optionally pass `--title-accent` for one short connector (`at`); the compositor renders it smaller and italic while keeping the remaining title in optically placed whole-word runs. The compositor rejects input-path collisions and existing output or manifest files; choose another path instead of overwriting.
6. Run `scripts/validate_editorial.py` against the source, output, and generated `.manifest.json`. Continue only when its JSON reports `"ok": true` and the process exits zero.
7. Inspect with `view_image`: intact photo; abstraction before recollection; horizontal motif remains dominant; any vertical anchors are source-derived, unequal, and subordinate; connected but non-equal optical margins; natural kerning and clear title hierarchy; flat panel; exact title; no extra text, watermark, fringe, speck, or invention.
8. On failure, make one targeted motif correction and repeat. Stop after two motif attempts.
9. Return only the image and saved path.

## Quick reference

| Need | Use |
|---|---|
| Visual rules | `references/art-direction.md` |
| Deterministic assembly | `scripts/compose_editorial.py --help` |
| Delivery gate | `scripts/validate_editorial.py --help` |
| Validated example | [references/example-pair.md](references/example-pair.md) |

## Common mistakes

- One-shot generation cannot prove photo preservation or exact typography.
- A miniature trace is not abstraction; unrelated anchors are not a grid.
- Equal-height vertical marks look diagrammatic; use one primary and one subordinate anchor only when the source supports them.
- Uniform per-character tracking and mathematically equal margins often look rigid; use native word shaping and optical offsets.
- Script success alone is insufficient: validator and visual QA must pass.
- Examples prove structure, not a reusable palette or template.
