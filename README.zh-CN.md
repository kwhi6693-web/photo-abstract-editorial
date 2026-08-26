# 🎨 Photo Abstract Editorial

将一张照片转化为「原始摄影区域 + 抽象记忆面板 + 诗意英文标题」的摄影抽象编辑作品。

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md)

[![Original](https://img.shields.io/badge/Original-Codex%20only-7a5c4f?style=flat-square)](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v1.0.0) [![V3 Adaptive](https://img.shields.io/badge/V3%20Adaptive-v3.0.0-c45a2f?style=flat-square)](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v3.0.0) [![Agent Skill](https://img.shields.io/badge/Type-Agent%20Skill-3f4856?style=flat-square)](https://github.com/kwhi6693-web/photo-abstract-editorial) [![Codex](https://img.shields.io/badge/Validated-Codex-6e5a76?style=flat-square)](https://github.com/kwhi6693-web/photo-abstract-editorial#-compatibility) [![License](https://img.shields.io/badge/License-AGPL--3.0-4c4c4c?style=flat-square)](LICENSE)

本项目保留原照片的事实性，用克制的抽象面板承载视觉记忆，并在具备 Strict Fidelity 时本地渲染编辑标题。

**一个项目，两种版本，由你选择。**

## 🧭 选择你的版本

| | Original Edition | V3 Adaptive Edition |
|---|---|---|
| 定位 | 保留的原始 Codex 工作流 | 自适应、基于能力的 V3 工作流 |
| 运行环境 | 仅支持 CODEX | Codex 与已测试的 DeepSeek Harness 能力路径已验证；面向具备所需图像能力的 Agents/Harnesses 设计 |
| 视觉行为 | 固定、克制 | 场景感知、可控制、版式感知 |
| 下载 | [Original 发布页](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v1.0.0) | [V3 Adaptive 正式版](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v3.0.0) |

### Original Edition

如果你希望使用历史固定工作流、已经使用 Codex，并偏好更简单的原始艺术指导约束，请选择 Original。

### V3 Adaptive Edition

如果你需要场景适配、四轴控制、自动版式选择、结构化 QA、有边界的修正，或一致的多图视觉家族，请选择 V3。

## 🧭 该选择哪个版本？

- 想要原始固定视觉行为？选择 Original Edition。
- 需要场景适配、控制、版式配置或系列一致性？选择 V3 Adaptive Edition。
- 正在使用非 Codex Agent？Original 不支持。若宿主具备所需图像和本地处理能力，V3 可能适用；已测试的 DeepSeek Harness 能力路径已独立验证，但这不代表每个 Agent 都提供相同的原生工具。
- 想要最小且最忠实于历史的安装包？选择 Original。
- 想要更明确的能力与验证约束？选择 V3。

## 🔍 原始版与 V3 自适应版对比

| 维度 | Original Edition | V3 Adaptive Edition |
|---|---|---|
| 定位 | V3 之前保留的工作流 | 自适应 photo-plus-abstraction Skill |
| 运行环境 | 仅 Codex | Codex 与已测试的 DeepSeek Harness 能力路径已验证；按基于能力的兼容性设计 |
| 复杂度 | 更小、更固定 | 更多输入、配置和验证边界 |
| 艺术指导 | 暖象牙色面板、源图派生的克制母题、光学编辑间距 | 保留编辑基础，并增加场景感知艺术指导与控制分辨率 |
| 源图保真度 | Original 示例已验证 pixel-exact 摄影区域 | Codex 与已测试的 DeepSeek Harness 路径均已验证 Strict Fidelity pixel-exact 摄影区域 |
| 创意控制 | 手动标题、面板、母题、对齐和字体覆盖 | Abstraction、Creative Freedom、Identity Preservation、Spatial Fidelity，各 0–100 |
| 场景配置 | 无 | 7 个：Pure Portrait、Environmental Portrait、Landscape、Architecture、Street/Crowd、Still Life、Minimal/Light |
| 肖像适配 | 在适合时使用源图派生的不等高竖向锚点 | 肖像感知场景配置与身份保留解析度 |
| 版式系统 | Lower Editorial 前身：lower-left 或 bottom-center | 5 个规范配置：Lower Editorial、Wide Horizon、Vertical Monument、Centered Archive、Sparse Object |
| QA | 机器验证器 + 视觉 QA；Original 示例有 9 项验证器检查 | 结构化 8 维 QA、机器验证器和明确的 HARD FAIL 规则 |
| 重试 | 一次针对性母题修正；最多两次母题尝试 | 完整尝试后最多一次针对性修正；关键 HARD FAIL 仍存在时停止 |
| 系列 | 没有 Series Style Lock 约束 | 可选 Series Style Lock 流程 |
| Agent 兼容性 | 仅 Codex | Codex 与已测试的 DeepSeek Harness 能力路径已验证；其他宿主仍取决于能力 |
| 安装方式 | 历史 Original 安装包 | V3 Adaptive 安装包与当前正式稳定版 |
| 适用场景 | 稳定、熟悉、Codex-specific 的原始行为 | 不同场景、明确控制、版式适配和系列工作 |
| 主要取舍 | 自适应较少，不能脱离 Codex | 流程和能力要求更多；各宿主的原生工具仍有差异 |

## 🎯 适用范围、限制与能力保证

### Original Edition

适合在 Codex 中用一张照片、一个无文字母题和一个固定编辑版式完成一次作品。它提供确定性本地合成与 Original 验证器的源图/面板检查，但不提供 V3 控制项系统、场景配置、规范自动版式、Series Style Lock 或跨 Agent 约束。它不支持 Codex 之外的宿主。

### V3 Adaptive Edition

适合需要明确场景推理、身份与空间控制、自适应版式或系列视觉家族的照片。V3 不应凭空生成没有来源的人物、建筑、物体、地理、文字、logo、水印、色卡或装饰事实。不同宿主和运行的图像生成可能变化；当前公开证据包括 Codex Strict Fidelity 与已独立测试的 DeepSeek Harness 能力路径。

### 能力保证矩阵

| 能力 | Original | V3 Strict Fidelity | V3 Native Image Edit | V3 Reference Generation |
|---|---|---|---|---|
| 源图感知行为 | 已实现，并在 Codex 验证 | 已实现，并在 Codex 与已测试的 DeepSeek Harness 路径验证 | 尽力而为 | 尽力而为 |
| 场景适配 | 原始固定行为 | 已实现，并在 Codex 评测 | 仅提供艺术指导约束 | 仅提供艺术指导约束 |
| 创意控制 | 手动覆盖 | 4 个控制项，0–100 | 取决于宿主，属于尽力而为 | 取决于宿主，属于尽力而为 |
| 像素精确摄影区域 | Original 示例已验证 | Strict 条件满足时经机器验证 | 不保证 | 不保证 |
| 本地精确排版 | Original 合成器路径 | 本地排版路径 | 不保证 | 不保证 |
| 确定性合成 | Original 本地合成器 | V3 本地合成器 | 不保证 | 不保证 |
| 机器验证 | Original 验证器 | V3 验证器与 manifest | 不属于 Strict 成片 | 不属于 Strict 成片 |
| 宿主兼容性 | 仅 Codex | Codex 与已测试的 DeepSeek Harness 路径已验证；面向具备相应能力的宿主设计 | 取决于能力 | 取决于能力 |

Native Image Edit 与 Reference Generation 不能被描述为机器验证的 Strict 成片。

## 💡 这个项目解决什么问题？

通用图像提示词可能重绘原照片、丢失主体身份、编造没有来源的事实、让抽象程度不一致，或生成不可靠的排版。固定版式也可能适合一张照片，却不适合另一张。

Photo Abstract Editorial 将事实照片与生成的抽象母题分开，让版式和创意决策明确化，在具备 Strict Fidelity 时使用本地排版，并在交付前加入质量门禁。Original 保留第一版稳定工作流；V3 让自适应决策更加明确。

## ✨ 主要功能

### Original Edition

- 一张源照片与一个稀疏无文字母题。
- 源图派生的色带、间隙、偏移，以及在来源支持时使用的不等高竖向锚点。
- 暖象牙色面板、克制配色、精确英文标题和光学间距。
- 确定性本地合成与 JSON manifest。
- Original 源图/输出冲突保护与摄影区域逐像素验证。
- 机器验证与视觉 QA。

### V3 Adaptive Edition

- 在 Strict Fidelity、Native Image Edit、Reference Generation 之间进行基于能力的路由。
- 四个 Creative Controls：Abstraction、Creative Freedom、Identity Preservation、Spatial Fidelity。
- 7 个场景配置与肖像感知抽象。
- 5 个确定性版式配置。
- 结构化 8 维 QA 与有边界的针对性重试。
- 可选 Series Style Lock 流程。
- 可移植色键清理、本地精确排版、manifest、机器验证器和可复现安装包。

## 🧩 V3 执行模式

### Strict Fidelity

当宿主具备视觉理解、图像生成、本地文件访问、Python、兼容 Pillow 的处理能力和可用衬线字体时，V3 可以提供确定性合成、本地精确排版、manifest、机器验证器，以及在不缩放时对摄影区域进行 pixel-exact verification。

### Native Image Edit

以源图作为编辑/参考图，在宿主支持时沿用相同的艺术指导和 QA 约束。这是尽力而为，不保证 pixel-exact、确定性、本地精确排版或机器验证的 Strict。

### Reference Generation

以源图作为唯一事实参考，执行依赖模型的生成路径。这是尽力而为，不提供 Strict Fidelity 保证。

## 📋 运行要求

### Original Edition

**仅 Codex。** Original 工作流需要 Codex 视觉检查、内置图像生成路径、历史工作流使用的 Codex 工作区/运行环境辅助工具、Python 3.10+、Pillow、可用衬线字体、一张照片和透明母题。

### V3 Strict Fidelity

需要视觉理解、图像生成、本地文件系统访问、Python 3.10+、兼容 Pillow 的处理能力、可用衬线字体、一张照片和透明母题。

### V3 Native Image Edit

需要视觉理解与宿主的图像编辑/合成能力；不提供 pixel-exact Strict 保证。

### V3 Reference Generation

需要视觉理解、图像生成和参考图支持；结果依赖模型，属于尽力而为。

## 📦 安装方法

### Original Edition

下载 [photo-abstract-editorial-original.zip](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/download/v1.0.0/photo-abstract-editorial-original.zip)，解压其中的 photo-abstract-editorial 文件夹，并安装到 Codex Skill 目录。Original 仅支持 Codex。

仓库中的副本是 [dist/photo-abstract-editorial-original.zip](dist/photo-abstract-editorial-original.zip)。

### V3 Adaptive Edition

下载 [photo-abstract-editorial-skill.zip](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/download/v3.0.0/photo-abstract-editorial-skill.zip)，或直接让 Codex 从公开仓库安装根目录 Skill：

仓库中的副本是 [dist/photo-abstract-editorial-skill.zip](dist/photo-abstract-editorial-skill.zip)。

~~~text
Use $skill-installer to install the root photo-abstract-editorial Skill from https://github.com/kwhi6693-web/photo-abstract-editorial.
~~~

该安装包只包含 V3 运行环境文件。README 素材、评测文件、测试、缓存和临时输出不进入 V3 运行环境安装包。

## 🚀 使用方法

### Original Edition

~~~text
Use $photo-abstract-editorial to turn this photograph into a strict-fidelity photo-and-abstract editorial composition.
~~~

Original 提示词会调用历史 Codex-specific 工作流。

### V3 Adaptive Edition — 默认模式

~~~text
Use $photo-abstract-editorial to create an adaptive, source-faithful photo-and-abstract editorial from this image.
~~~

### V3 Adaptive Edition — 受控模式

~~~text
Use $photo-abstract-editorial. Set Abstraction to 60, Creative Freedom to 45, Identity Preservation to 80, and Spatial Fidelity to 70. Resolve the scene and layout from the photograph, then run the applicable QA.
~~~

### V3 Adaptive Edition — 系列模式

~~~text
Use $photo-abstract-editorial for this three-image series. Keep a restrained warm-ivory editorial family, but re-analyze each photograph and choose its own motif, layout, and spatial relationships.
~~~

当前 Skill 约束中的控制项是自然语言工作流输入，不声称是数值合成器 API。

## 🖼️ 输入与输出

普通源照片

→ 场景事实与源图派生关系

→ 抽象母题、面板与精确标题

→ 机器验证与视觉 QA

→ Photo Abstract Editorial 成品

## 🎞️ 真实演示

下面的 V3 图片全部来自 RC 评测数据集，是实际 Codex Strict Fidelity 输出并通过验证器；不是宣传用重构图。

| 场景 | 版本 | 版式 | 验证 |
|---|---|---|---|
| Pure Portrait | V3 Adaptive | Vertical Monument | Strict PASS |
| Landscape | V3 Adaptive | Wide Horizon | Strict PASS |
| Architecture | V3 Adaptive | Centered Archive | Strict PASS |
| Still Life | V3 Adaptive | Sparse Object | Strict PASS |
| Minimal / Light | V3 Adaptive | Sparse Object | Strict PASS |

| Pure Portrait | Landscape | Architecture |
|---|---|---|
| ![V3 纯肖像成片](assets/readme/v3/pure-portrait.png) | ![V3 横向成片](assets/readme/v3/landscape.png) | ![V3 建筑成片](assets/readme/v3/architecture.png) |

| Still Life | Minimal / Light |
|---|---|
| ![V3 静物成片](assets/readme/v3/still-life.png) | ![V3 极简光线成片](assets/readme/v3/minimal-light.png) |

完整数据集与清单文件见 [assets/evals/v3.0-rc1](assets/evals/v3.0-rc1) 和 [RC 评测报告](docs/evals/v3.0-rc1-real-world-evaluation.md)。

## ↔️ 原始版与 V3 同源对比

本对比使用 Original README 中的历史源图。Original 成片原样复用；V3 成片则在之后使用当前 V3 工作流从同一源图真实生成。

| 同一源图 | Original 历史成片 | V3 Adaptive 实际成片 |
|---|---|---|
| ![历史日落地平线源图](assets/readme/comparisons/original-horizon/source.png) | ![Original 历史成片](assets/readme/comparisons/original-horizon/original-result.png) | ![V3 同源成片](assets/readme/comparisons/original-horizon/v3-result.png) |

Original 保留固定的 lower-left 编辑行为。V3 将同一长地平线解析为 Wide Horizon，并应用当前场景感知合成。这个对比解释的是不同决策，不表示某个版本无条件更好。

## 🎛️ V3 控制能力演示

下面三个输出使用同一 E03 Landscape 源图和同一 Wide Horizon 版式。它们是真实 Codex 编排层控制项提示词的结果，并全部通过机器验证器。

| Abstraction 30 | Abstraction 60 | Abstraction 80 |
|---|---|---|
| ![Abstraction 30](assets/readme/controls/abstraction-30.png) | ![Abstraction 60](assets/readme/controls/abstraction-60.png) | ![Abstraction 80](assets/readme/controls/abstraction-80.png) |

当前合成器没有将这些值暴露为数值命令行参数；报告把它们记录为编排层决策，而不是机器强制分数。

## 🗂️ V3 系列风格演示

下面三个实际输出接受了 Codex 侧系列风格评测：共享暖象牙色面板语言、Bodoni 字体排版体系、整段字距调整、克制留白与源图可追溯的标记语汇，同时保留各自的场景逻辑。

**同一视觉家族，不同源图逻辑。**

| Landscape | Street / Crowd | Minimal / Light |
|---|---|---|
| ![系列横向成片](assets/readme/series/landscape.png) | ![系列街道人群成片](assets/readme/series/street-crowd.png) | ![系列极简光线成片](assets/readme/series/minimal-light.png) |

这是对文档化 Series Style Lock 约束的真实 Codex 视觉 PASS 评审。当前运行环境没有名为 Series Style Lock 的独立机器标志；系列演示本身仍是 Codex 侧结果，而独立 DeepSeek 验证覆盖下文所述的确定性能力路径。

## ⚙️ 工作原理

### Original Edition

照片 → Codex 视觉检查 → 无文字母题生成 → 历史清理辅助工具 → Original 合成器 → Original 验证器 → 视觉 QA。

### V3 Adaptive Edition

照片 → 场景分析 → 创意控制 → 版式选择 → 艺术指导 → 生成/编辑 → 质量门禁 → 必要时一次针对性修正 → 最终编辑成片。

### V3 Strict Fidelity 路径

透明母题 → 可移植色键清理 → 确定性合成器 → 本地精确排版 → manifest → 机器验证器。

## ✅ 验证

以下数字来自当前公开源代码与 v3.0.0 正式发布，不是历史估算。

- Original Edition：隔离的 v1.0.0 工作树中 32/32 测试通过。
- Original Edition：自身构建器与 --check 通过；历史示例验证器返回 ok=true。
- Original 安装包：9 个运行环境文件；SHA-256 为 a1a44b1a9cec9ba04b379a7d3a14315701abb14bb93e953003337870772d0a6d。
- V3 Adaptive Edition：Codex 上 41/41 测试通过。
- V3 安装包：15 个运行环境文件；安装包构建与 --check 通过。
- V3 RC 评测：7 个场景成片与 5 个控制变体通过验证器和摄影区域逐像素检查。
- V3 版式：5 个规范版式全部在真实源图上运行过。
- V3 同源对比：新的 V3 成片验证器 PASS。
- V3 安装包排除 README 素材、docs/evals、测试、缓存和临时输出。

重点是可验证，而不只是生成。

## 🔬 独立验证

独立的 DeepSeek Harness 已完成确定性能力路径验证。

- DeepSeek Harness：PASS
- Strict Fidelity：在本次测试流水线上 VERIFIED
- 项目测试：41/41 通过
- 结构化视觉/编辑 QA：8/8 PASS
- 机器验证器：`ok: true`；验证错误：`[]`
- 阻塞问题：0
- 跨 Agent 兼容性：针对已测试能力路径 VERIFIED
- 流程冒烟检查：`remove_chroma_key.py`、`compose_editorial.py`、`validate_editorial.py` 均以 0 退出

详见简洁的 [DeepSeek Harness 独立验证摘要](docs/evals/deepseek-harness-validation.md)。本次验证中的 DeepSeek Harness 未提供原生神经图像生成能力，因此母题使用确定性的 Pillow 程序化生成。该限制不影响已验证的摄影区域逐像素一致性、源图哈希、几何、排版、确定性合成或机器验证结果。

## 🌐 兼容性

### Original Edition

**仅 CODEX。** Original 在其 Codex-specific 运行环境约束内完成实现和验证。不支持 Claude、Gemini、Cursor 或其他 Agent。

### V3 Adaptive Edition

- 已验证的运行环境路径：Codex Strict Fidelity，以及独立的 DeepSeek Harness Strict Fidelity 运行。
- 按能力设计：面向具备所需能力的图像 Agents/Harnesses。
- 针对已测试能力路径的跨 Agent 兼容性已验证；这不代表每个 Agent 都提供相同的原生工具。

DESIGNED FOR COMPATIBILITY 不等于 VALIDATED。

## 📥 版本发布

### Photo Abstract Editorial — Original Edition

- 标签：v1.0.0
- 运行环境：仅 Codex
- 发布页：[Original Edition 发布页](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v1.0.0)
- 安装包：[photo-abstract-editorial-original.zip](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/download/v1.0.0/photo-abstract-editorial-original.zip)
- 演示：保留历史 README 源图/成片对
- 审计：[Original Edition 功能与来源审计](docs/releases/original-edition.md)

### Photo Abstract Editorial V3 Adaptive — v3.0.0

- 标签：v3.0.0
- 发布页：[V3 Adaptive 正式稳定版](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v3.0.0)
- 安装包：[photo-abstract-editorial-skill.zip](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/download/v3.0.0/photo-abstract-editorial-skill.zip)
- 验证：Codex 回归、构建、安装包与正式发布前校验 PASS
- 独立验证：DeepSeek Harness 针对已测试确定性能力路径 PASS

v3.0.0 是当前正式稳定版。

## 🔄 版本选择与切换

如果你偏好固定的历史视觉行为、使用 Codex 并希望更小的工作流，可以继续使用 Original。

如果你需要场景适配、四轴创意控制、自动版式、结构化 QA 或系列工作，可以尝试 V3。

Original 用户不需要迁移；两个安装包可以并行保留。

## ❓ 常见问题

### Original 可以在 Codex 之外运行吗？

不可以。Original 是 CODEX ONLY。

### 应该下载哪个版本？

想要历史固定 Codex 工作流就下载 Original；想要自适应场景逻辑与显式控制就下载 V3。

### V3 必须手动设置控制项吗？

不需要。默认工作流会从源图解析它们；你也可以在需要明确倾向时提供自然语言数值。

### 为什么 Native Image Edit 与 Reference Generation 不能保证 pixel-exact？

因为它们依赖宿主或模型的图像操作，而不是本地确定性 Strict 合成器。

### 两个版本可以同时保留吗？

可以。这正是双版本发布结构的目的。

### V3 已在 Claude、Gemini 或 Cursor 上验证了吗？

没有纳入本仓库的公开验证证据。DeepSeek Harness 已针对已测试确定性能力路径完成独立验证；其他 Agent 仍取决于能力且尚未测试。

### Series Style Lock 实际保留什么？

它保留面板语言、配色、排版、留白和标记语汇等视觉家族，同时重新分析每张源图，而不是复制坐标或母题。

## 🛠️ 技术细节

<details>
<summary>V3 运行环境结构</summary>

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
<summary>可复现安装包</summary>

Original 使用历史 v1.0.0 代码树中的 Original Edition 构建器，包含 9 个运行环境文件。V3 使用当前构建器，包含 15 个运行环境文件。两个构建器都会排除仅开发用途内容，并根据各自代码树验证归档条目。

</details>

<details>
<summary>Manifest 与 Strict 检查</summary>

V3 manifest 记录源图/输出哈希、渲染后摄影区域哈希、面板几何信息、版式配置、母题区域、清理详情和排版运行记录。验证器检查 manifest、尺寸、几何信息、面板角点、源图哈希、输出哈希与摄影区域像素。

</details>

## 📌 项目状态

- Original Edition：支持、保留，并作为历史 v1.0.0 发布版本提供。
- V3 Adaptive Edition：当前正式稳定版，已完成 Codex 验证，并针对已测试能力路径完成 DeepSeek Harness 独立验证。
- 文档：三语言双版本 README 与真实演示素材。
- 跨 Agent 兼容性：针对已测试的 DeepSeek Harness 能力路径已验证；其他 Agent 尚未测试。
- 正式 v3.0.0：当前稳定版。

## ⚖️ 许可证

本项目及其公开发布版本使用 AGPL-3.0。参见 [LICENSE](LICENSE)。
