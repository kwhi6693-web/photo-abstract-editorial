# PHOTO ABSTRACT EDITORIAL

## 01. Hero

**一个项目，两种版本，由你选择。**

这是一个将普通照片转化为 Photo Abstract Editorial 的 Agent Skill：原照片始终是事实锚点，克制的抽象面板与精确英文标题共同形成编辑作品。

![V3 Adaptive 同源 Hero：日落地平线照片、源图派生抽象面板与精确标题](assets/readme/hero/v3-original-source.png)

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md)

[Original Edition](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v1.0.0) · [V3 Adaptive Edition](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v3.0.0-rc2)

本项目同时保留两个真实版本。它们不是互相替代的关系，而是针对不同工作流、环境和控制需求进行优化。

## 02. Language Switcher

- [English](README.md)
- [简体中文](README.zh-CN.md)
- [繁體中文](README.zh-TW.md)

## 03. Quick Navigation

[选择版本](#04-选择版本) · [版本对比](#06-original-vs-v3-对比) · [范围与保证](#07-范围限制与保证) · [真实 Demo](#15-真实-demo-画廊) · [验证](#20-验证) · [Release](#22-releases)

## 04. 选择版本

| | Original Edition | V3 Adaptive Edition |
|---|---|---|
| 定位 | 保留的原始 Codex 工作流 | 自适应、capability-based 的 V3 工作流 |
| Runtime | 仅支持 CODEX | Codex 已验证；面向具备所需能力的 image-capable Agents/Harnesses 设计 |
| 视觉行为 | 固定、克制 | 场景感知、可控制、版式感知 |
| 下载 | [Original Release](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v1.0.0) | [当前 V3 RC](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v3.0.0-rc2) |

### Original Edition

如果你希望使用历史固定工作流、已经使用 Codex，并偏好更简单的原始 art-direction contract，请选择 Original。

### V3 Adaptive Edition

如果你需要场景适配、四轴控制、自动版式选择、结构化 QA、有边界的修正，或一致的多图视觉家族，请选择 V3。

## 05. 该选择哪个版本？

- 想要原始固定视觉行为？选择 Original Edition。
- 需要场景适配、控制、版式 profile 或系列一致性？选择 V3 Adaptive Edition。
- 正在使用非 Codex Agent？Original 不支持。若宿主具备所需图像和本地处理能力，V3 可能适用，但额外 Agent runtime validation 仍待完成。
- 想要最小且最忠实于历史的安装包？选择 Original。
- 想要更明确的 capability 与 verification contract？选择 V3。

## 06. Original vs V3 对比

| 维度 | Original Edition | V3 Adaptive Edition |
|---|---|---|
| 定位 | V3 之前保留的工作流 | 自适应 photo-plus-abstraction Skill |
| Runtime 环境 | 仅 Codex | Codex 已验证；按 capability-based compatibility 设计 |
| 复杂度 | 更小、更固定 | 更多输入、profile 和 verification boundary |
| Art direction | 暖象牙色面板、源图派生 muted motif、光学编辑间距 | 保留编辑基础，并增加场景感知 art direction 与 control resolution |
| Source fidelity | Original 示例已验证 pixel-exact 摄影区域 | Codex Strict Fidelity 已验证 pixel-exact 摄影区域 |
| Creative controls | 手动标题、面板、motif、对齐和字体 override | Abstraction、Creative Freedom、Identity Preservation、Spatial Fidelity，各 0–100 |
| Scene Profiles | 无 | 7 个：Pure Portrait、Environmental Portrait、Landscape、Architecture、Street/Crowd、Still Life、Minimal/Light |
| Portrait adaptation | 在适合时使用源图派生的不等高竖向锚点 | portrait-aware scene profile 与 identity-preservation resolution |
| Layout system | Lower Editorial 前身：lower-left 或 bottom-center | 5 个 canonical profile：Lower Editorial、Wide Horizon、Vertical Monument、Centered Archive、Sparse Object |
| QA | machine validator + visual QA；Original 示例有 9 项 validator checks | 结构化 8 维 QA、machine validator 和明确的 HARD FAIL 规则 |
| Retry | 一次 targeted motif correction；最多两次 motif attempt | 完整尝试后最多一次 targeted correction；关键 HARD FAIL 仍存在时停止 |
| Series | 没有 Series Style Lock contract | 可选 Series Style Lock 流程 |
| Agent compatibility | 仅 Codex | 面向具备能力的 image-capable Agents/Harnesses 设计；当前只有 Codex 已验证 |
| Installation | 历史 Original package | V3 Adaptive package 与当前 RC |
| 适用场景 | 稳定、熟悉、Codex-specific 的原始行为 | 不同场景、明确控制、版式适配和系列工作 |
| 主要取舍 | 自适应较少，不能脱离 Codex | 流程和能力要求更多；额外 Agent validation 待完成 |

## 07. 范围、限制与保证

### Original Edition

适合在 Codex 中用一张照片、一个无文字 motif 和一个固定编辑版式完成一次作品。它提供确定性本地合成与 Original validator 的 source/panel 检查，但不提供 V3 control system、scene profiles、canonical auto-layout、Series Style Lock 或 cross-Agent contract。它不支持 Codex 之外的宿主。

### V3 Adaptive Edition

适合需要明确场景推理、身份与空间控制、自适应版式或系列视觉家族的照片。V3 不应凭空生成没有来源的人物、建筑、物体、地理、文字、logo、水印、色卡或装饰事实。不同宿主和运行的图像生成可能变化；当前公开 V3 证据来自 Codex。

### Guarantee Matrix

| 能力 | Original | V3 Strict Fidelity | V3 Native Image Edit | V3 Reference Generation |
|---|---|---|---|---|
| Source-aware behavior | 已实现，并在 Codex 验证 | 已实现，并在 Codex 验证 | best effort | best effort |
| Scene adaptation | 原始固定行为 | 已实现，并在 Codex 评测 | 仅 art-direction contract | 仅 art-direction contract |
| Creative controls | 手动 override | 4 个 control，0–100 | 取决于宿主的 best effort | 取决于宿主的 best effort |
| Pixel-exact photo region | Original 示例已验证 | Strict 条件满足时 machine-validated | 不保证 | 不保证 |
| Exact local typography | Original compositor path | local typography path | 不保证 | 不保证 |
| Deterministic composition | Original local compositor | V3 local compositor | 不保证 | 不保证 |
| Machine validation | Original validator | V3 validator 与 manifest | 不属于 Strict output | 不属于 Strict output |
| Host compatibility | 仅 Codex | Codex 已验证；面向 suitable capability-based hosts 设计 | 取决于能力 | 取决于能力 |

Native Image Edit 与 Reference Generation 不能被描述为 machine-verified Strict output。

## 08. 这个项目解决什么问题？

通用图像 prompt 可能重绘原照片、丢失主体身份、编造没有来源的事实、让抽象程度不一致，或生成不可靠的 typography。固定版式也可能适合一张照片，却不适合另一张。

Photo Abstract Editorial 将事实照片与生成的抽象 motif 分开，让版式和创意决策明确化，在具备 Strict Fidelity 时使用本地 typography，并在交付前加入 quality gate。Original 保留第一版稳定工作流；V3 让自适应决策更加明确。

## 09. 主要能力

### Original Edition

- 一张源照片与一个稀疏无文字 motif。
- 源图派生的色带、间隙、偏移，以及在来源支持时使用的不等高竖向锚点。
- 暖象牙色面板、muted palette、精确英文标题和光学间距。
- 确定性本地合成与 JSON manifest。
- Original source/output collision guards 与 pixel-level photo-region validation。
- Machine validation 与 visual QA。

### V3 Adaptive Edition

- 在 Strict Fidelity、Native Image Edit、Reference Generation 之间进行 capability-based routing。
- 四个 Creative Controls：Abstraction、Creative Freedom、Identity Preservation、Spatial Fidelity。
- 7 个 Scene Profiles 与 portrait-aware abstraction。
- 5 个确定性 Layout Profiles。
- 结构化 8 维 QA 与有边界的 targeted retry。
- 可选 Series Style Lock 流程。
- portable chroma cleanup、exact local typography、manifest、machine validator 和 reproducible package。

## 10. V3 Execution Modes

### Strict Fidelity

当宿主具备视觉理解、图像生成、本地文件访问、Python、Pillow-compatible processing 和可用衬线字体时，V3 可以提供 deterministic composition、exact local typography、manifest、machine validator，以及在不缩放时对摄影区域进行 pixel-exact verification。

### Native Image Edit

以源图作为 edit/reference image，在宿主支持时沿用相同的 art-direction 和 QA contract。这是 best effort，不保证 pixel-exact、deterministic、exact-local-typography 或 machine-verified Strict。

### Reference Generation

以源图作为唯一事实参考，执行 model-dependent generation path。这是 best effort，不提供 Strict Fidelity 保证。

## 11. Requirements

### Original Edition

**仅 Codex。** Original workflow 需要 Codex visual inspection、内置 image-generation path、历史工作流使用的 Codex workspace/runtime helper、Python 3.10+、Pillow、可用衬线字体、一张照片和透明 motif。

### V3 Strict Fidelity

需要视觉理解、图像生成、本地文件系统访问、Python 3.10+、Pillow-compatible processing、可用衬线字体、一张照片和透明 motif。

### V3 Native Image Edit

需要视觉理解与宿主的 image-editing/composition capability；不提供 pixel-exact Strict guarantee。

### V3 Reference Generation

需要视觉理解、图像生成和 reference-image support；结果依赖模型且为 best effort。

## 12. Installation

### Original Edition

下载 [photo-abstract-editorial-original.zip](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/download/v1.0.0/photo-abstract-editorial-original.zip)，解压其中的 photo-abstract-editorial 文件夹，并安装到 Codex Skill 目录。Original 仅支持 Codex。

仓库中的副本是 [dist/photo-abstract-editorial-original.zip](dist/photo-abstract-editorial-original.zip)。

### V3 Adaptive Edition

下载 [photo-abstract-editorial-skill.zip](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/download/v3.0.0-rc2/photo-abstract-editorial-skill.zip)，或直接让 Codex 从公开仓库安装根目录 Skill：

仓库中的副本是 [dist/photo-abstract-editorial-skill.zip](dist/photo-abstract-editorial-skill.zip)。

~~~text
Use $skill-installer to install the root photo-abstract-editorial Skill from https://github.com/kwhi6693-web/photo-abstract-editorial.
~~~

该 package 只包含 V3 runtime 文件。README assets、evaluation files、tests、cache 和临时输出不进入 V3 runtime package。

## 13. Usage

### Original Edition

~~~text
Use $photo-abstract-editorial to turn this photograph into a strict-fidelity photo-and-abstract editorial composition.
~~~

Original prompt 会调用历史 Codex-specific workflow。

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

当前 Skill contract 中的 control 是自然语言工作流输入，不声称是 numeric compositor API。

## 14. Input → Output

普通源照片

→ 场景事实与源图派生关系

→ 抽象 motif、面板与精确标题

→ machine validation 与 visual QA

→ Photo Abstract Editorial 成品

## 15. 真实 Demo 画廊

下面的 V3 图片全部来自 RC evaluation corpus，是实际 Codex Strict Fidelity 输出并通过 validator；不是宣传用重构图。

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

完整 corpus 与 manifests 见 [assets/evals/v3.0-rc1](assets/evals/v3.0-rc1) 和 [RC evaluation report](docs/evals/v3.0-rc1-real-world-evaluation.md)。

## 16. Original vs V3 同源 Demo

本对比使用 Original README 中的历史 source。Original result 原样复用；V3 result 则在之后使用当前 V3 workflow 从同一 source 真实生成。

| 同一 source | Original 历史 result | V3 Adaptive 实际 result |
|---|---|---|
| ![历史日落地平线 source](assets/readme/comparisons/original-horizon/source.png) | ![Original 历史 result](assets/readme/comparisons/original-horizon/original-result.png) | ![V3 同源 result](assets/readme/comparisons/original-horizon/v3-result.png) |

Original 保留固定的 lower-left 编辑行为。V3 将同一长地平线解析为 Wide Horizon，并应用当前 scene-aware composition。这个对比解释的是不同决策，不表示某个版本无条件更好。

## 17. V3 Control Showcase

下面三个输出使用同一 E03 Landscape source 和同一 Wide Horizon layout。它们是真实 Codex orchestration-level control prompt 的结果，并全部通过 machine validator。

| Abstraction 30 | Abstraction 60 | Abstraction 80 |
|---|---|---|
| ![Abstraction 30](assets/readme/controls/abstraction-30.png) | ![Abstraction 60](assets/readme/controls/abstraction-60.png) | ![Abstraction 80](assets/readme/controls/abstraction-80.png) |

当前 compositor 没有将这些值暴露为 numeric command-line argument；报告把它们记录为 orchestration decisions，而不是 machine-enforced scores。

## 18. V3 Series Showcase

下面三个实际输出接受了 Codex-side series-style evaluation：共享暖象牙色面板语言、Bodoni typography family、whole-run kerning、克制留白与源图可追溯的 mark vocabulary，同时保留各自的 scene logic。

**同一视觉家族，不同源图逻辑。**

| Landscape | Street / Crowd | Minimal / Light |
|---|---|---|
| ![Series landscape](assets/readme/series/landscape.png) | ![Series street crowd](assets/readme/series/street-crowd.png) | ![Series minimal light](assets/readme/series/minimal-light.png) |

这是对文档化 Series Style Lock contract 的真实 Codex visual PASS review。当前 runtime 没有名为 Series Style Lock 的独立 machine flag，这也不构成独立 Agent validation。

## 19. How It Works

### Original Edition

Photograph → Codex visual inspection → 无文字 motif generation → 历史 cleanup helper → Original compositor → Original validator → visual QA。

### V3 Adaptive Edition

Photograph → Scene Analysis → Creative Controls → Layout Selection → Art Direction → Generation/Edit → Quality Gate → 必要时一次 targeted correction → Final Editorial。

### V3 Strict Fidelity path

透明 motif → portable chroma cleanup → deterministic composer → exact local typography → manifest → machine validator。

## 20. 验证

以下数字来自当前公开 source 与本轮 release preparation，不是历史估算。

- Original Edition：隔离的 v1.0.0 worktree 中 32/32 tests 通过。
- Original Edition：自身 builder 与 --check 通过；历史 example validator 返回 ok=true。
- Original package：9 个 runtime files；SHA-256 为 a1a44b1a9cec9ba04b379a7d3a14315701abb14bb93e953003337870772d0a6d。
- V3 Adaptive Edition：Codex 上 41/41 tests 通过。
- V3 package：15 个 runtime files；package build 与 --check 通过。
- V3 RC evaluation：7 个 scene results 与 5 个 control variants 通过 validator 和 photo-region pixel-exact checks。
- V3 layouts：5 个 canonical layouts 全部在真实 source 上运行过。
- V3 同源对比：新的 V3 result validator PASS。
- V3 package 排除 README assets、docs/evals、tests、cache 和临时输出。

Built to be checked, not just generated.

## 21. Compatibility

### Original Edition

**仅 CODEX。** Original 在其 Codex-specific runtime contract 内完成实现和验证。不支持 Claude、Gemini、Cursor 或其他 Agent。

### V3 Adaptive Edition

- Validated runtime：Codex。
- Designed for capability-based compatibility：具备所需能力的 suitable image-capable Agents/Harnesses。
- Independent runtime validation on additional Agents：PENDING。

DESIGNED FOR COMPATIBILITY 不等于 VALIDATED。

## 22. Releases

### Photo Abstract Editorial — Original Edition

- Tag：v1.0.0
- Runtime：Codex only
- Release：[Original Edition release](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v1.0.0)
- Artifact：[photo-abstract-editorial-original.zip](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/download/v1.0.0/photo-abstract-editorial-original.zip)
- Demo：保留历史 README source/result pair
- Audit：[Original Edition 功能与 provenance 审计](docs/releases/original-edition.md)

### Photo Abstract Editorial V3 Adaptive — v3.0.0-rc2

- Tag：v3.0.0-rc2
- Release：[V3 Adaptive prerelease](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v3.0.0-rc2)
- Artifact：[photo-abstract-editorial-skill.zip](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/download/v3.0.0-rc2/photo-abstract-editorial-skill.zip)
- Validation：Codex-side tests 与 RC evidence PASS
- Limitation：独立 additional-Agent runtime validation 待完成

正式 v3.0.0 有意不发布。

## 23. Switching / Upgrade Guide

如果你偏好固定的历史视觉行为、使用 Codex 并希望更小的 workflow，可以继续使用 Original。

如果你需要 scene adaptation、四轴 creative controls、自动版式、结构化 QA 或 series work，可以尝试 V3。

Original 用户不需要迁移；两个 package 可以并行保留。

## 24. FAQ

### Original 可以在 Codex 之外运行吗？

不可以。Original 是 CODEX ONLY。

### 应该下载哪个版本？

想要历史固定 Codex workflow 就下载 Original；想要自适应场景逻辑与显式控制就下载 V3。

### V3 必须手动设置 controls 吗？

不需要。默认 workflow 会从 source 解析它们；你也可以在需要明确倾向时提供自然语言数值。

### 为什么 Native Image Edit 与 Reference Generation 不能保证 pixel-exact？

因为它们依赖宿主或模型的图像操作，而不是本地确定性 Strict compositor。

### 两个版本可以同时保留吗？

可以。这正是 dual-edition release structure 的目的。

### V3 已在 Claude、Gemini 或 Cursor 上验证了吗？

没有。额外 Agent runtime validation 待完成。

### Series Style Lock 实际保留什么？

它保留面板语言、palette、typography、whitespace 和 mark vocabulary 等视觉家族，同时重新分析每张 source，而不是复制坐标或 motif。

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

Original 使用历史 v1.0.0 tree 中的 Original Edition builder，包含 9 个 runtime files。V3 使用当前 builder，包含 15 个 runtime files。两个 builder 都会排除 development-only 内容，并根据各自 source tree 验证 archive entries。

</details>

<details>
<summary>Manifest 与 Strict checks</summary>

V3 manifest 记录 source/output hashes、rendered photo-region hash、panel geometry、layout profile、motif region、cleanup details 和 typography runs。validator 检查 manifest、尺寸、geometry、panel corners、source hash、output hash 与 photo-region pixels。

</details>

## 26. Project Status

- Original Edition：支持、保留，并作为历史 v1.0.0 release 提供。
- V3 Adaptive Edition：当前公开 release candidate，已完成 Codex validation。
- Documentation：三语言 dual-edition README 与真实 Demo assets。
- Independent additional-Agent runtime validation：待完成。
- 正式 v3.0.0：未发布。

## 27. License

本项目及其公开 releases 使用 AGPL-3.0。参见 [LICENSE](LICENSE)。
