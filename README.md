# PHOTO ABSTRACT EDITORIAL

## 01. Hero

**Two Editions. One Project. Your Choice.**

An Agent Skill that turns an ordinary photograph into a Photo Abstract Editorial composition: the source photograph remains the factual anchor, while a restrained abstract panel and exact English title create the editorial reading.

![V3 Adaptive same-source hero: sunset horizon photograph with a source-derived abstract panel and exact title](assets/readme/hero/v3-original-source.png)

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md)

[Original Edition](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v1.0.0) · [V3 Adaptive Edition](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v3.0.0-rc2)

This project keeps two real editions available. Neither edition replaces the other; they optimize for different workflows, environments, and kinds of control.

## 02. Language Switcher

- [English](README.md)
- [简体中文](README.zh-CN.md)
- [繁體中文](README.zh-TW.md)

## 03. Quick Navigation

[Choose an edition](#04-choose-your-edition) · [Compare editions](#06-original-vs-v3-comparison) · [Scope and guarantees](#07-scope--limitations--guarantees) · [Real demos](#15-real-demo-gallery) · [Validation](#20-validation) · [Releases](#22-releases)

## 04. Choose Your Edition

| | Original Edition | V3 Adaptive Edition |
|---|---|---|
| Positioning | The preserved original Codex workflow | The adaptive, capability-based V3 workflow |
| Runtime | CODEX ONLY | Codex validated; designed for suitable image-capable Agents/Harnesses |
| Visual behavior | Fixed and restrained | Scene-aware, controllable, and layout-aware |
| Download | [Original release](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v1.0.0) | [Current V3 RC](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v3.0.0-rc2) |

### Original Edition

Choose Original when you want the historical fixed workflow, already use Codex, and prefer the simpler original art-direction contract.

### V3 Adaptive Edition

Choose V3 when you need scene adaptation, four creative controls, automatic layout selection, structured QA, bounded correction, or a consistent multi-image visual family.

## 05. Which Edition Should I Choose?

- Want the original fixed visual behavior? Choose Original Edition.
- Want scene adaptation, controls, layout profiles, or series consistency? Choose V3 Adaptive Edition.
- Using a non-Codex Agent? Original is not supported. V3 may be suitable when the host provides the required image and local-processing capabilities, but additional runtime validation is still pending.
- Want the smallest and most historically faithful package? Choose Original.
- Want a more explicit contract around capabilities and verification? Choose V3.

## 06. Original vs V3 Comparison

| Dimension | Original Edition | V3 Adaptive Edition |
|---|---|---|
| Positioning | Preserved pre-V3 workflow | Adaptive photo-plus-abstraction Skill |
| Runtime environment | Codex only | Codex validated; capability-based compatibility designed |
| Complexity | Smaller, fixed workflow | More inputs, profiles, and verification boundaries |
| Art direction | Warm-ivory panel, muted source-derived motif, optical editorial spacing | Same editorial foundation plus scene-aware art direction and control resolution |
| Source fidelity | Pixel-exact photo region validated in the Original example | Strict Fidelity pixel-exact photo region validated in Codex |
| Creative controls | Manual title, panel, motif, alignment, and font overrides | Abstraction, Creative Freedom, Identity Preservation, Spatial Fidelity, each 0–100 |
| Scene Profiles | None | 7: Pure Portrait, Environmental Portrait, Landscape, Architecture, Street/Crowd, Still Life, Minimal/Light |
| Portrait adaptation | Source-derived unequal vertical anchors when appropriate | Portrait-aware scene profile and identity-preservation resolution |
| Layout system | Lower Editorial predecessor: lower-left or bottom-center | 5 canonical profiles: Lower Editorial, Wide Horizon, Vertical Monument, Centered Archive, Sparse Object |
| QA | Machine validator plus visual QA; Original example has 9 validator checks | Structured 8-dimension QA, machine validator, and explicit HARD FAIL rules |
| Retry | One targeted motif correction; stop after two motif attempts | One targeted correction after a complete attempt; stop on a remaining critical HARD FAIL |
| Series | No Series Style Lock contract | Optional Series Style Lock process |
| Agent compatibility | Codex only | Designed for suitable image-capable Agents/Harnesses; only Codex is currently validated |
| Installation | Historical Original package | V3 Adaptive package and current RC |
| Best use cases | Stable, familiar, Codex-specific original behavior | Different scenes, explicit controls, layout adaptation, and series work |
| Main trade-off | Less adaptive and not portable beyond Codex | More process and capability requirements; external Agent validation is pending |

## 07. Scope / Limitations / Guarantees

### Original Edition

Best suited for one photograph, one text-free motif, and one fixed editorial composition in Codex. It provides deterministic local assembly and the Original validator's source/panel checks. It does not provide the V3 control system, scene profiles, canonical auto-layout, Series Style Lock, or cross-Agent contract. It is not supported outside Codex.

### V3 Adaptive Edition

Best suited for photographs that benefit from explicit scene reasoning, identity and spatial controls, adaptive layouts, or a series-level visual family. V3 does not invent unsupported people, buildings, objects, geography, text, logos, watermarks, swatches, or decorative facts. Image generation can vary across hosts and runs; the current public V3 evidence is Codex-side.

### Guarantee Matrix

| Capability | Original | V3 Strict Fidelity | V3 Native Image Edit | V3 Reference Generation |
|---|---|---|---|---|
| Source-aware behavior | Implemented and Codex-validated | Implemented and Codex-validated | Best effort | Best effort |
| Scene adaptation | Fixed original behavior | Implemented and Codex-evaluated | Art-direction contract only | Art-direction contract only |
| Creative controls | Manual overrides | 4 controls, 0–100 | Host-dependent best effort | Host-dependent best effort |
| Pixel-exact photo region | Validated for Original example | Machine-validated when Strict conditions hold | Not guaranteed | Not guaranteed |
| Exact local typography | Original compositor path | Local typography path | Not guaranteed | Not guaranteed |
| Deterministic composition | Original local compositor | V3 local compositor | Not guaranteed | Not guaranteed |
| Machine validation | Original validator | V3 validator and manifest | Not a Strict output | Not a Strict output |
| Host compatibility | Codex only | Codex validated; suitable capability-based hosts designed for | Capability-dependent | Capability-dependent |

Native Image Edit and Reference Generation must never be described as machine-verified Strict output.

## 08. What Problem Does This Project Solve?

Generic image prompts may redraw the source photograph, lose subject identity, invent unsupported facts, produce inconsistent abstraction levels, or render unreliable typography. A fixed layout may also fit one photograph but not another.

Photo Abstract Editorial separates the factual photograph from the generated abstract motif, makes layout and creative decisions explicit, renders typography locally when Strict Fidelity is available, and adds a quality gate before delivery. Original keeps the first stable workflow available; V3 makes the adaptive decisions more explicit.

## 09. Key Features

### Original Edition

- One source photograph and one sparse text-free motif.
- Source-derived bands, gaps, offsets, and unequal vertical anchors when supported by the source.
- Warm-ivory panel, muted palette, exact English title, and optical spacing.
- Deterministic local composition and JSON manifest.
- Original source/output collision guards and pixel-level photo-region validation.
- Machine validation plus visual QA.

### V3 Adaptive Edition

- Capability-based routing across Strict Fidelity, Native Image Edit, and Reference Generation.
- Four Creative Controls: Abstraction, Creative Freedom, Identity Preservation, Spatial Fidelity.
- Seven Scene Profiles and portrait-aware abstraction.
- Five deterministic Layout Profiles.
- Structured eight-dimension QA and bounded targeted retry.
- Optional Series Style Lock process.
- Portable chroma cleanup, exact local typography, manifest, machine validator, and reproducible package.

## 10. V3 Execution Modes

### Strict Fidelity

When the host has visual understanding, image generation, local file access, Python, Pillow-compatible processing, and a usable serif font, V3 can provide deterministic composition, exact local typography, a manifest, a machine validator, and pixel-exact photographic-region verification when no resizing is requested.

### Native Image Edit

Uses the source as the edit/reference image and follows the same art-direction and QA contract where the host supports it. It is best effort: no pixel-exact, deterministic, exact-local-typography, or machine-verified Strict guarantee is made.

### Reference Generation

Uses the source as the sole factual reference for a model-dependent generation path. It is best effort and does not provide Strict Fidelity guarantees.

## 11. Requirements

### Original Edition

**Codex only.** The Original workflow requires Codex visual inspection, the built-in image-generation path, the Codex workspace/runtime helper used by the historical workflow, Python 3.10+, Pillow, a usable serif font, one photograph, and a transparent motif.

### V3 Strict Fidelity

Visual understanding, image generation, local filesystem access, Python 3.10+, Pillow-compatible processing, a usable serif font, one photograph, and a transparent motif.

### V3 Native Image Edit

Visual understanding plus host image-editing/composition capability. Pixel-exact Strict guarantees are not available.

### V3 Reference Generation

Visual understanding, image generation, and reference-image support. Results are model-dependent and best effort.

## 12. Installation

### Original Edition

Download [photo-abstract-editorial-original.zip](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/download/v1.0.0/photo-abstract-editorial-original.zip), extract the included photo-abstract-editorial folder, and install it in the Codex Skill directory. Original is Codex only.

The repository copy is [dist/photo-abstract-editorial-original.zip](dist/photo-abstract-editorial-original.zip).

### V3 Adaptive Edition

Download [photo-abstract-editorial-skill.zip](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/download/v3.0.0-rc2/photo-abstract-editorial-skill.zip), or ask Codex to install the root Skill from the public repository:

The repository copy is [dist/photo-abstract-editorial-skill.zip](dist/photo-abstract-editorial-skill.zip).

~~~text
Use $skill-installer to install the root photo-abstract-editorial Skill from https://github.com/kwhi6693-web/photo-abstract-editorial.
~~~

The package contains only V3 runtime files. README assets, evaluation files, tests, caches, and temporary outputs are not part of the V3 runtime package.

## 13. Usage

### Original Edition

~~~text
Use $photo-abstract-editorial to turn this photograph into a strict-fidelity photo-and-abstract editorial composition.
~~~

The Original prompt invokes the historical Codex-specific workflow.

### V3 Adaptive Edition — Default

~~~text
Use $photo-abstract-editorial to create an adaptive, source-faithful photo-and-abstract editorial from this image.
~~~

### V3 Adaptive Edition — Controlled

~~~text
Use $photo-abstract-editorial. Set Abstraction to 60, Creative Freedom to 45, Identity Preservation to 80, and Spatial Fidelity to 70. Resolve the scene and layout from the photograph, then run the applicable QA.
~~~

### V3 Adaptive Edition — Series

~~~text
Use $photo-abstract-editorial for this three-image series. Keep a restrained warm-ivory editorial family, but re-analyze each photograph and choose its own motif, layout, and spatial relationships.
~~~

Controls are natural-language workflow inputs in the current Skill contract; they are not claimed to be a numeric compositor API.

## 14. Input → Output

Ordinary source photograph

→ scene facts and source-derived relationships

→ abstract motif, panel, and exact title

→ machine validation and visual QA

→ Photo Abstract Editorial result

## 15. Real Demo Gallery

All V3 images below are actual outputs from the RC evaluation corpus. They are Codex Strict Fidelity results with validator PASS; they are not promotional reconstructions.

| Scene | Edition | Layout | Validation |
|---|---|---|---|
| Pure Portrait | V3 Adaptive | Vertical Monument | Strict PASS |
| Landscape | V3 Adaptive | Wide Horizon | Strict PASS |
| Architecture | V3 Adaptive | Centered Archive | Strict PASS |
| Still Life | V3 Adaptive | Sparse Object | Strict PASS |
| Minimal / Light | V3 Adaptive | Sparse Object | Strict PASS |

| Pure Portrait | Landscape | Architecture |
|---|---|---|
| ![V3 Pure Portrait result](assets/readme/v3/pure-portrait.png) | ![V3 Landscape result](assets/readme/v3/landscape.png) | ![V3 Architecture result](assets/readme/v3/architecture.png) |

| Still Life | Minimal / Light |
|---|---|
| ![V3 Still Life result](assets/readme/v3/still-life.png) | ![V3 Minimal Light result](assets/readme/v3/minimal-light.png) |

The full corpus and manifests are in [assets/evals/v3.0-rc1](assets/evals/v3.0-rc1) and [the RC evaluation report](docs/evals/v3.0-rc1-real-world-evaluation.md).

## 16. Original vs V3 Same-Source Demo

This comparison uses the historical Original README source. The Original result is reused unchanged; the V3 result was generated later from the same source with the current V3 workflow.

| Same source | Original historical result | V3 Adaptive actual result |
|---|---|---|
| ![Historical sunset horizon source](assets/readme/comparisons/original-horizon/source.png) | ![Original historical result](assets/readme/comparisons/original-horizon/original-result.png) | ![V3 same-source result](assets/readme/comparisons/original-horizon/v3-result.png) |

The Original keeps its fixed lower-left editorial behavior. V3 resolves the same long horizon as Wide Horizon and applies the current scene-aware composition. The comparison explains different decisions; it does not claim that one edition is universally better.

## 17. V3 Control Showcase

These three outputs use the same E03 Landscape source and the same Wide Horizon layout. The variants are real Codex orchestration-level control prompts, and all three passed the machine validator.

| Abstraction 30 | Abstraction 60 | Abstraction 80 |
|---|---|---|
| ![Abstraction 30](assets/readme/controls/abstraction-30.png) | ![Abstraction 60](assets/readme/controls/abstraction-60.png) | ![Abstraction 80](assets/readme/controls/abstraction-80.png) |

The current compositor does not expose these values as a numeric command-line argument; the report records them as applied orchestration decisions rather than machine-enforced scores.

## 18. V3 Series Showcase

These three actual outputs were reviewed as a Codex-side series-style evaluation: same warm-ivory panel language, Bodoni typography family, whole-run kerning, restrained whitespace, and source-traceable mark vocabulary, while each image keeps its own scene logic.

**Same visual family. Different source logic.**

| Landscape | Street / Crowd | Minimal / Light |
|---|---|---|
| ![Series landscape](assets/readme/series/landscape.png) | ![Series street crowd](assets/readme/series/street-crowd.png) | ![Series minimal light](assets/readme/series/minimal-light.png) |

This is a real visual PASS review of the documented Series Style Lock contract on Codex outputs. The current runtime does not expose a separate machine flag named Series Style Lock, and this does not constitute independent Agent validation.

## 19. How It Works

### Original Edition

Photograph → Codex visual inspection → text-free motif generation → historical cleanup helper → Original compositor → Original validator → visual QA.

### V3 Adaptive Edition

Photograph → Scene Analysis → Creative Controls → Layout Selection → Art Direction → Generation/Edit → Quality Gate → one targeted correction when needed → Final Editorial.

### V3 Strict Fidelity path

Transparent motif → portable chroma cleanup → deterministic composer → exact local typography → manifest → machine validator.

## 20. Validation

The numbers below are from the current public source and release preparation, not historical estimates.

- Original Edition: 32/32 tests passed in the isolated v1.0.0 worktree.
- Original Edition: its own builder and --check passed; its historical example validator returned ok=true.
- Original package: 9 runtime files; SHA-256 a1a44b1a9cec9ba04b379a7d3a14315701abb14bb93e953003337870772d0a6d.
- V3 Adaptive Edition: 41/41 tests passed on Codex.
- V3 package: 15 runtime files; package build and --check passed.
- V3 RC evaluation: 7 scene results and 5 control variants passed the validator and photo-region pixel-exact checks.
- V3 layouts: all 5 canonical layouts exercised on real source images.
- V3 same-source comparison: validator PASS for the new V3 result.
- V3 package excludes README assets, docs/evals, tests, caches, and temporary outputs.

Built to be checked, not just generated.

## 21. Compatibility

### Original Edition

**CODEX ONLY.** Original is implemented and validated within its Codex-specific runtime contract. It is not supported on Claude, Gemini, Cursor, or other Agents.

### V3 Adaptive Edition

- Validated runtime: Codex.
- Designed for capability-based compatibility: suitable image-capable Agents/Harnesses that provide the required capabilities.
- Independent runtime validation on additional Agents: PENDING.

DESIGNED FOR COMPATIBILITY is not the same as VALIDATED.

## 22. Releases

### Photo Abstract Editorial — Original Edition

- Tag: v1.0.0
- Runtime: Codex only
- Release: [Original Edition release](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v1.0.0)
- Artifact: [photo-abstract-editorial-original.zip](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/download/v1.0.0/photo-abstract-editorial-original.zip)
- Demo: preserved historical README source/result pair
- Audit: [Original Edition feature and provenance audit](docs/releases/original-edition.md)

### Photo Abstract Editorial V3 Adaptive — v3.0.0-rc2

- Tag: v3.0.0-rc2
- Release: [V3 Adaptive prerelease](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v3.0.0-rc2)
- Artifact: [photo-abstract-editorial-skill.zip](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/download/v3.0.0-rc2/photo-abstract-editorial-skill.zip)
- Validation: Codex-side tests and RC evidence PASS
- Limitation: independent additional-Agent runtime validation pending

Formal v3.0.0 is intentionally not released.

## 23. Switching / Upgrade Guide

Stay on Original if you prefer the fixed historical visual behavior, use Codex, and want a smaller workflow.

Try V3 if you need scene adaptation, four creative controls, automatic layouts, structured QA, or series work.

No Original user is required to migrate. The two packages can remain available side by side.

## 24. FAQ

### Can Original run outside Codex?

No. Original is CODEX ONLY.

### Which edition should I download?

Download Original for the historical fixed Codex workflow. Download V3 for adaptive scene logic and explicit controls.

### Does V3 require manually setting controls?

No. The default workflow resolves them from the source. You may provide natural-language values when you want a deliberate bias.

### Why can Native Image Edit and Reference Generation not guarantee pixel-exact output?

Those modes depend on host/model image operations rather than the local deterministic Strict compositor.

### Can both editions remain available?

Yes. That is the purpose of the dual-edition release structure.

### Is V3 validated on Claude, Gemini, or Cursor?

No. Additional Agent runtime validation is pending.

### What does Series Style Lock preserve?

It preserves a visual family such as panel language, palette, typography, whitespace, and mark vocabulary while re-analyzing each source instead of copying coordinates or motifs.

## 25. Technical Details

<details>
<summary>V3 runtime structure</summary>

~~~text
photo-abstract-editorial/
|- SKILL.md
|- agents/openai.yaml
|- references/
|- scripts/compose_editorial.py
|- scripts/remove_chroma_key.py
|- scripts/validate_editorial.py
`- assets/examples/
~~~

</details>

<details>
<summary>Reproducible packages</summary>

Original uses the Original Edition builder from the historical v1.0.0 tree and contains 9 runtime files. V3 uses the current builder and contains 15 runtime files. Both builders exclude development-only material from their runtime archive and verify archive entries against their own source tree.

</details>

<details>
<summary>Manifest and Strict checks</summary>

V3 manifests record source/output hashes, rendered photo-region hash, panel geometry, layout profile, motif region, cleanup details, and typography runs. The validator checks the manifest, dimensions, geometry, panel corners, source hash, output hash, and photo-region pixels.

</details>

## 26. Project Status

- Original Edition: supported, preserved, and available as the historical v1.0.0 release.
- V3 Adaptive Edition: current public release candidate with Codex validation.
- Documentation: three-language dual-edition README and real demo assets.
- Independent additional-Agent runtime validation: pending.
- Formal v3.0.0: not released.

## 27. License

This project and its public releases are licensed under AGPL-3.0. See [LICENSE](LICENSE).
