# V3.0 RC1 Evaluation Corpus

This directory contains the reproducible local corpus and rendered evidence used for the V3.0 RC1 Codex-side evaluation.

## Provenance

- Seven source images were generated with the built-in image-generation capability for this evaluation. They are fictional, ordinary-photography scenes created for testing; no user photographs, web downloads, stock assets, or copyrighted reference images were used.
- Seven motif inputs were generated as transparent-background abstract marks from the same scene facts. Each motif was passed through the repository chroma-cleanup script before composition.
- The generated-image originals remain outside the repository in the Codex generated-images store. The repository copies here are the exact inputs used by the recorded compositions.
- All composition, cleanup, validation, and report generation was run locally by Codex on the RC1 evaluation branch.

## Scene corpus

| Case | Scene profile | Source prompt intent | Motif prompt intent | Final layout | Result |
|---|---|---|---|---|---|
| E01 | pure-portrait | Quiet natural-light head-and-shoulders portrait of a fictional adult woman | Small charcoal and umber shoulder/axis mark; no face, text, or literal portrait | vertical-monument | result.png |
| E02 | environmental-portrait | Fictional adult man in an olive jacket and helmet at a concrete harbor wall | Horizontal harbor-edge and figure-relation mark; no literal person or text | vertical-monument | result.png |
| E03 | landscape | Coastal salt marsh at dusk with a long horizon and path | Broad lateral marsh, water, horizon, and path relationships | wide-horizon | result.png |
| E04 | architecture | Generic vertical stone bell tower in quiet daylight | Narrow vertical stone/arch cue; no literal building rendering or text | centered-archive | result.png |
| E05 | street-crowd | Anonymous rainy crosswalk crowd with umbrellas; no readable signage | Repeating pedestrian and umbrella rhythm; no faces, text, or logos | lower-editorial | result.png |
| E06 | still-life | Ceramic cup and one pear on linen | Small planar cup/pear relation; no literal object drawing or text | sparse-object | result.png |
| E07 | minimal-light | Empty plaster room with a chair and diagonal window light | Sparse diagonal light/room relationship; no literal furniture drawing or text | sparse-object | result.png |

Each scene directory contains source.png, motif-generated.png, motif-clean.png, result.png, and the compositor manifest. E03 also retains result-attempt-1.png and its manifest to document the one targeted retry correction.

## Control corpus

The control variants use the E03 landscape source and the same wide-horizon compositor geometry. They exercise the orchestration-level control prompts rather than a compositor command-line control schema:

- abstraction-30, abstraction-60, abstraction-80: conservative, balanced, and strongly relational motif prompts.
- freedom-low, freedom-high: conservative source-traceable and bolder mark-grouping prompts.

Every control result has a machine-validated manifest. The control values are recorded in the evaluation report as applied prompt decisions; they are not claimed to be numeric values enforced by the runtime.

## Reproduction

From the repository root, use the bundled Python dependency environment and run the cleanup, compositor, and validator scripts documented in the report. The generated result manifests record source hashes, rendered photo-region hashes, layout geometry, typography runs, and motif-cleanup details.
