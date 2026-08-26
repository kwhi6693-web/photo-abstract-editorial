# Original Edition

The Original Edition is the preserved pre-V3 workflow for users who want the project's first complete Codex-specific behavior. It remains a supported user-selectable edition; it is not deprecated or obsolete.

## Historical identity

- Source commit: 063de8b
- Historical tag: v1.0.0
- Runtime boundary: Codex only
- Public demo: the source and result pair in the original README, preserved byte-for-byte at assets/examples/source-horizon.png and assets/examples/result-horizon.png.

The tag is a real historical project tag. It is not a reconstructed or backdated SemVer history.

## Audited feature set

- One photograph becomes one vertical photo-plus-abstraction editorial composition.
- Codex visual inspection and built-in image generation create a text-free transparent motif; the source photograph remains the reference image and is not redrawn as the final photo region.
- The Original art direction uses a shortened warm-ivory panel, a lower-left optical grid by default, a muted source-derived palette, one exact English title, and a high-contrast serif.
- Decisive vertical structures may become one primary and one subordinate unequal vertical anchor; other source relationships remain abstract bands, gaps, and offsets.
- The Original compositor supports lower-left and bottom-center layouts, optional title accent, optional subtitle, panel/color/font overrides, bounded motif sizing, and collision-safe output paths.
- The Original validator records and checks manifest version, source/output hashes, output geometry, panel corners, photo-region geometry, and decoded photo-region pixel equality.
- The Original workflow requires visual QA after machine validation and permits one targeted motif correction, stopping after two motif attempts.

## Deliberate boundaries

The Original Edition does not include V3 Adaptive capabilities such as four Creative Controls, seven Scene Profiles, five canonical Layout Profiles, Series Style Lock, capability-based mode routing, portable chroma cleanup, or V3's expanded structured QA contract. It has a simpler fixed workflow and a narrower runtime contract.

It is not supported outside Codex. Users who need a suitable non-Codex image-capable Agent/Harness should evaluate the V3 Adaptive Edition instead, subject to the V3 compatibility boundary.

## Verification and package

The original source tree was checked in an isolated worktree at the historical tag:

- Original regression suite: 32/32 tests passed.
- Original builder: build and --check passed.
- Historical README example validator: ok=true with all 9 Original checks passing.
- Original runtime package: 9 files, built by the Original Edition's own tools/build_skill_package.py.
- Published artifact: photo-abstract-editorial-original.zip.

The current repository also retains the original generic asset from the historical release for backward compatibility. The clearly named Original artifact is the recommended download for this edition.
