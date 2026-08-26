# Structured Visual Quality Check

Run this check after composition and after any targeted correction. Record one status per dimension: `PASS`, `SOFT FAIL`, or `HARD FAIL`.

| Dimension | PASS means |
|---|---|
| Source Fidelity | The source is the sole factual source; Strict Mode machine validation passes and no photo-region change is present. |
| Abstraction Match | The motif is abstract before recollection and matches the resolved Abstraction/Freedom controls. |
| Subject Identity | Required portrait, landmark, or object cues remain at the resolved Identity Preservation level. |
| Spatial Traceability | Important positions, scale, overlap, axes, intervals, and gravity remain traceable to the source. |
| Unsupported Content | No invented person, building, object, text, logo, watermark, swatch, or decorative fact appears. |
| Composition | Photo, flat panel, motif, whitespace, and title form a coherent editorial hierarchy; layout geometry is legal. |
| Typography | The exact title is present, locally rendered in Strict Mode, legible, restrained, and fully inside the panel. |
| Editorial Coherence | Mark families, palette, whitespace, panel language, and tone feel intentional and consistent. |

## Failure policy

`HARD FAIL` blocks delivery. In Strict Mode, any machine validator failure is a Source Fidelity `HARD FAIL`. A `SOFT FAIL` may be corrected only when a targeted change is clear and source-traceable.

Apply at most one targeted correction after the first complete attempt. Re-run machine validation and the full visual checklist after that correction. If a critical `HARD FAIL` remains on the second attempt, stop and report the failure; never present it as a successful result.

Native Image Edit and Reference Generation may use the same checklist, but must disclose that they cannot guarantee pixel-exact source preservation, deterministic photo preservation, or machine-verified Strict Mode output.
