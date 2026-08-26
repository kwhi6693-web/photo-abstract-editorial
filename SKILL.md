---
name: photo-abstract-editorial
description: Use when one or more photographs must become adaptive photo-plus-abstraction editorial compositions while source facts, spatial relationships, and strict photo preservation remain controlled.
---

# Photo Abstract Editorial

Create a lightweight editorial composition from a supplied photograph. The photograph remains the sole factual source; generated content is an abstract motif, never a replacement for the final photo region or exact title.

## Capability routing

Choose the highest-fidelity mode the host can actually execute:

- **Strict Fidelity:** host visual-understanding capability, host image-generation capability, local filesystem access, local Python/script execution, Pillow-compatible image processing, and a usable serif font. This mode deterministically assembles photo, panel, motif, and typography, then runs machine validation.
- **Native Image Edit:** host visual-understanding capability plus host image-editing/composition capability, without the complete local Strict toolchain. Use the source as the edit/reference image and disclose that pixel-exact, deterministic, machine-verified photo preservation is unavailable.
- **Reference Generation:** host visual-understanding capability, host image-generation capability, and reference-image support. Use the source as the sole factual reference, perform best-effort fidelity, and disclose the same Strict guarantees are unavailable.

If visual understanding or every image-generation/editing capability is absent, stop rather than fabricate a result.

## Workflow

1. Validate the required image input and inspect the source.
2. Classify the scene and resolve the four controls in [control-system.md](references/control-system.md) using [scene-profiles.md](references/scene-profiles.md).
3. Select a layout from [layout-profiles.md](references/layout-profiles.md) using scene facts, orientation, dominant axis, subject location, center of gravity, and negative space. Omitted layout falls back to Lower Editorial.
4. Read [art-direction.md](references/art-direction.md). Generate or edit only what the selected mode permits; keep the motif sparse, traceable, text-free, and source-derived. When the source supports a decisive vertical structure, use one primary and one subordinate irregular vertical stroke, unequal in height and width.
5. In Strict Fidelity, run [remove_chroma_key.py](scripts/remove_chroma_key.py), [compose_editorial.py](scripts/compose_editorial.py), and [validate_editorial.py](scripts/validate_editorial.py). Never overwrite source, motif, output, or manifest.
6. Run the structured eight-dimension QA in [quality-check.md](references/quality-check.md). Strict machine validation is necessary but not sufficient; visual/editorial QA is also required.
7. Apply at most one targeted correction. Re-run the relevant generation/composition, machine validation, and QA; stop after the second attempt if a critical HARD FAIL remains.
8. For an explicitly requested multi-image series only, load [series-style.md](references/series-style.md) and lock the visual family while re-analyzing each new source.

The [validated example pair](references/example-pair.md) demonstrates package structure and regression expectations; do not copy its subject, palette, title, or coordinates.

Return the final artifact, saved path, selected mode, and concise QA result. Do not claim Strict guarantees for Native Image Edit or Reference Generation.
