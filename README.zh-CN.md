# 🎨 Photo Abstract Editorial

一个以源图保真为核心的 Agent Skill，将照片转为具备自适应版式、可控抽象和确定性合成路径的编辑作品。

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md)

[![Original](https://img.shields.io/badge/Original-Codex%20only-7a5c4f?style=flat-square)](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v1.0.0) [![V3 Adaptive](https://img.shields.io/badge/V3%20Adaptive-v3.0.0-c45a2f?style=flat-square)](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v3.0.0) [![Agent Skill](https://img.shields.io/badge/Type-Agent%20Skill-3f4856?style=flat-square)](https://github.com/kwhi6693-web/photo-abstract-editorial) [![Codex](https://img.shields.io/badge/Validated-Codex-6e5a76?style=flat-square)](https://github.com/kwhi6693-web/photo-abstract-editorial#compatibility)

Photo Abstract Editorial 保留源照片的事实内容，将源图关系转化为克制的抽象面板，并在已验证路径支持时使用本地排版生成标题。

<a id="before-after"></a>
## 转换前 → 转换后

**同一源图 · 实际 V3 成片 · Strict Fidelity / 验证器 PASS**

源图原样展示。右侧是仓库中已有的 V3 同源成片；其 [manifest](assets/readme/comparisons/original-horizon/v3-result.png.manifest.json) 记录了 pixel-exact 摄影区域，已发布的同源检查报告为验证器 PASS。

| 转换前 | 转换后 |
|---|---|
| ![同一源照片](assets/readme/comparisons/original-horizon/source.png) | ![同源实际 V3 成片](assets/readme/comparisons/original-horizon/v3-result.png) |

<a id="navigation"></a>
**快速跳转：** [快速开始](#quick-start) · [作品画廊](#gallery) · [选择版本](#choose-an-edition) · [兼容性](#compatibility) · [验证](#validation) · [发布版本](#releases) · [环境契约](#environment-contract)

<a id="quick-start"></a>
## ⚡ 30 秒快速开始

V3 Adaptive 是大多数新用户的推荐起点。

### 安装

下载 [v3.0.0 发布 ZIP](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/download/v3.0.0/photo-abstract-editorial-skill.zip)，安装其中的 Skill；也可以使用现有安装器方法：

~~~text
Use $skill-installer to install the root photo-abstract-editorial Skill from https://github.com/kwhi6693-web/photo-abstract-editorial.
~~~

### 运行

~~~text
Use $photo-abstract-editorial to create an adaptive, source-faithful photo-and-abstract editorial from this image.
~~~

### 可选控制

~~~text
Use $photo-abstract-editorial. Set Abstraction to 60, Creative Freedom to 45, Identity Preservation to 80, and Spatial Fidelity to 70.
~~~

<a id="gallery"></a>
## 🖼️ 作品画廊

下面五张图片均来自 RC 评测集，是实际的 V3 Codex Strict Fidelity 成片，并通过验证器；不是宣传重构图。

| 纯肖像 | 风景 | 建筑 |
|---|---|---|
| ![V3 纯肖像成片](assets/readme/v3/pure-portrait.png) | ![V3 风景成片](assets/readme/v3/landscape.png) | ![V3 建筑成片](assets/readme/v3/architecture.png) |

| 静物 | 极简 / 光线 |
|---|---|
| ![V3 静物成片](assets/readme/v3/still-life.png) | ![V3 极简光线成片](assets/readme/v3/minimal-light.png) |

| 场景 | 版式 | 验证 |
|---|---|---|
| 纯肖像 | Vertical Monument | Strict Fidelity · 验证器 PASS |
| 风景 | Wide Horizon | Strict Fidelity · 验证器 PASS |
| 建筑 | Centered Archive | Strict Fidelity · 验证器 PASS |
| 静物 | Sparse Object | Strict Fidelity · 验证器 PASS |
| 极简 / 光线 | Sparse Object | Strict Fidelity · 验证器 PASS |

完整数据集与 manifest 见 [assets/evals/v3.0-rc1](assets/evals/v3.0-rc1) 和 [RC 评测报告](docs/evals/v3.0-rc1-real-world-evaluation.md)。

如果这个工作流对你有帮助，点一颗 ⭐ 能让更多人发现这个项目。

<a id="why"></a>
## 为什么选择 Photo Abstract Editorial？

- 在已验证的 Strict Fidelity 路径中保留源照片。
- 根据场景选择版式，不把所有源图强行塞进同一个画面。
- 让抽象程度可控，并保持与照片的来源关系。
- 在 Strict Fidelity 下使用精确的本地排版。
- 在交付前执行结构化 QA。
- 在具备所需能力时提供可复现的确定性路径。

通用图像提示词可能重绘源照片、丢失主体身份、编造没有来源的事实、造成抽象程度不一致，或生成不可靠的排版。本项目将事实照片与生成的抽象母题分开，让版式和创意决策明确化，并在交付前加入质量门禁。

<a id="choose-an-edition"></a>
## 🧭 选择版本

**推荐大多数新用户使用：V3 Adaptive。**

| | Original | V3 Adaptive |
|---|---|---|
| 运行环境 | 仅 Codex | 基于能力；已在 Codex 与经测试的 DeepSeek Harness 路径验证 |
| 版式 | 固定 | 自适应 |
| 控制项 | 手动 | 四个创意控制项 |
| QA | Original 验证器 | 结构化 V3 QA |
| 最适合 | 历史 Codex 工作流 | 当前推荐工作流 |

Original 继续为希望使用固定 Codex 工作流的用户提供支持。V3 是当前正式稳定版，适合场景适配、显式控制、自适应版式、结构化 QA 与系列工作。两个版本可以并行保留。

- [Original v1.0.0 发布版本](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v1.0.0)
- [V3 Adaptive v3.0.0 发布版本](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v3.0.0)

<a id="original-vs-v3"></a>
## 🔍 Original 与 V3 对比

<details>
<summary>展开完整版本对比</summary>

| 维度 | Original Edition | V3 Adaptive Edition |
|---|---|---|
| 定位 | 保留的 V3 之前工作流 | 自适应照片加抽象面板 Skill |
| 运行环境 | 仅 Codex | Codex 与经测试的 DeepSeek Harness 能力路径已验证；按能力设计兼容性 |
| 复杂度 | 更小的固定工作流 | 更多输入、配置与验证边界 |
| 艺术指导 | 暖象牙色面板、源图派生的克制母题、光学编辑间距 | 相同编辑基础，加上场景感知艺术指导与控制项解析 |
| 源图保真 | Original 示例已验证摄影区域 pixel-exact | Codex 与经测试的 DeepSeek Harness 路径已验证 Strict Fidelity 摄影区域 pixel-exact |
| 创意控制 | 标题、面板、母题、对齐与字体手动覆盖 | Abstraction、Creative Freedom、Identity Preservation、Spatial Fidelity，每项 0–100 |
| 场景配置 | 无 | 7 个：Pure Portrait、Environmental Portrait、Landscape、Architecture、Street/Crowd、Still Life、Minimal/Light |
| 肖像适配 | 来源支持时使用源图派生的不等高纵向锚点 | 肖像感知场景配置与身份保留解析 |
| 版式系统 | Lower Editorial 前身：左下或底部居中 | 5 个规范配置：Lower Editorial、Wide Horizon、Vertical Monument、Centered Archive、Sparse Object |
| QA | 机器验证器加视觉 QA；Original 示例有 9 项验证 | 结构化 8 维 QA、机器验证器与明确的 HARD FAIL 规则 |
| 重试 | 一次针对性母题修正；最多两次母题尝试 | 完整尝试后一次针对性修正；仍有关键 HARD FAIL 时停止 |
| 系列 | 没有 Series Style Lock 约束 | 可选 Series Style Lock 流程 |
| Agent 兼容性 | 仅 Codex | Codex 与经测试的 DeepSeek Harness 能力路径已验证；其他宿主仍取决于能力 |
| 安装 | 历史 Original 安装包 | V3 Adaptive 安装包与当前稳定版 |
| 最适合 | 稳定、熟悉、Codex 专用的 Original 行为 | 不同场景、显式控制、自适应版式与系列工作 |
| 主要取舍 | 自适应性较少，不能移植到 Codex 之外 | 流程与能力要求更多；不同宿主的原生工具仍有差异 |

</details>

<a id="scope"></a>
## 🎯 适用范围、限制与能力保证

<details>
<summary>展开适用范围与保证详情</summary>

### Original Edition

适合在 Codex 中使用一张照片、一个无文字母题和一个固定编辑构图。它提供确定性本地合成以及 Original 的源图/面板检查。不提供 V3 控制系统、场景配置、规范自动版式、Series Style Lock 或跨 Agent 合同。不支持在 Codex 之外运行。

### V3 Adaptive Edition

适合需要显式场景推理、身份与空间控制、自适应版式或系列视觉家族的照片。V3 不会凭空生成没有来源的人物、建筑、物体、地理信息、文字、Logo、水印、色卡或装饰性事实。图像生成会因宿主和运行次序而变化；当前公开证据包括 Codex Strict Fidelity 与经独立测试的 DeepSeek Harness 能力路径。

### 能力保证矩阵

| 能力 | Original | V3 Strict Fidelity | V3 Native Image Edit | V3 Reference Generation |
|---|---|---|---|---|
| 源图感知行为 | 已实现并经 Codex 验证 | 已在 Codex 与经测试的 DeepSeek Harness 路径实现并验证 | 尽力而为 | 尽力而为 |
| 场景适配 | 固定 Original 行为 | 已实现并经 Codex 评测 | 仅艺术指导约束 | 仅艺术指导约束 |
| 创意控制 | 手动覆盖 | 4 个控制项，0–100 | 取决于宿主的尽力而为 | 取决于宿主的尽力而为 |
| 摄影区域 pixel-exact | Original 示例已验证 | Strict 条件满足时机器验证 | 不保证 | 不保证 |
| 精确本地排版 | Original 合成器路径 | 本地排版路径 | 不保证 | 不保证 |
| 确定性合成 | Original 本地合成器 | V3 本地合成器 | 不保证 | 不保证 |
| 机器验证 | Original 验证器 | V3 验证器与 manifest | 不是 Strict 输出 | 不是 Strict 输出 |
| 宿主兼容性 | 仅 Codex | Codex 与经测试的 DeepSeek Harness 路径已验证；面向具备所需能力的宿主设计 | 取决于能力 | 取决于能力 |

Native Image Edit 与 Reference Generation 不得被描述为机器验证的 Strict 成片。

</details>

<a id="features"></a>
## ✨ 主要功能

<details>
<summary>展开功能级约束</summary>

### Original Edition

- 一张源照片与一个稀疏的无文字母题。
- 源图派生的色带、间隙、偏移，以及在来源支持时使用的不等高纵向锚点。
- 暖象牙色面板、克制配色、精确英文标题与光学间距。
- 确定性本地合成与 JSON manifest。
- Original 源图/输出冲突保护与逐像素摄影区域验证。
- 机器验证与视觉 QA。

### V3 Adaptive Edition

- 在 Strict Fidelity、Native Image Edit、Reference Generation 之间进行基于能力的路由。
- 四个 Creative Controls：Abstraction、Creative Freedom、Identity Preservation、Spatial Fidelity。
- 7 个场景配置与肖像感知抽象。
- 5 个确定性版式配置。
- 结构化 8 维 QA 与有边界的针对性重试。
- 可选 Series Style Lock 流程。
- 可移植色键清理、本地精确排版、manifest、机器验证器与可复现安装包。

</details>

<a id="execution-modes"></a>
## 🧩 V3 执行模式

<details>
<summary>展开模式边界</summary>

### Strict Fidelity

当宿主具备视觉理解、图像生成、本地文件访问、Python、兼容 Pillow 的处理能力和可用的衬线字体时，V3 可以提供确定性合成、精确本地排版、manifest、机器验证器，以及在不缩放时对摄影区域进行 pixel-exact 验证。

### Native Image Edit

以源图作为编辑/参考图，在宿主支持时遵循相同的艺术指导与 QA 约束。这是尽力而为，不保证 pixel-exact、确定性、精确本地排版或机器验证的 Strict 结果。

### Reference Generation

以源图作为唯一事实参考，执行依赖模型的生成路径。这是尽力而为，不提供 Strict Fidelity 保证。

</details>

<a id="requirements"></a>
## 📋 运行要求

<details>
<summary>展开运行要求</summary>

### Original Edition

**仅 Codex。** Original 工作流需要 Codex 视觉检查、内置图像生成路径、历史工作流使用的 Codex 工作区/运行环境辅助工具、Python 3.10–3.13（CI 已验证）、Pillow、可用衬线字体、一张照片和透明母题。

### V3 Strict Fidelity

需要视觉理解、图像生成、本地文件系统访问、Python 3.10–3.13（CI 已验证）、兼容 Pillow 的处理能力、可用衬线字体、一张照片和透明母题。

### V3 Native Image Edit

需要视觉理解以及宿主图像编辑/合成能力；不提供 pixel-exact Strict 保证。

### V3 Reference Generation

需要视觉理解、图像生成和参考图支持；结果取决于模型，属于尽力而为。

</details>

### 开发测试

测试运行器仅作为开发依赖，不会进入任何运行时发布包。从全新检出开始，创建隔离环境、安装仓库开发依赖，然后直接运行 `pytest`：

~~~powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python scripts/doctor.py --development
pytest
python scripts/validate_editorial.py --source assets/examples/source-horizon.png --output assets/examples/result-horizon.png --manifest assets/examples/result-horizon.png.manifest.json
~~~

~~~bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python scripts/doctor.py --development
pytest
python scripts/validate_editorial.py --source assets/examples/source-horizon.png --output assets/examples/result-horizon.png --manifest assets/examples/result-horizon.png.manifest.json
~~~

<a id="environment-contract"></a>
## 🩺 环境契约

本地合成器和验证器只使用 `Pillow` 这一项 Python 运行时依赖。从仓库运行脚本时，请按 [requirements.txt](requirements.txt) 安装；[requirements-dev.txt](requirements-dev.txt) 复用运行时清单，并额外加入仅供开发使用的 `pytest` 测试运行器。

只读预检入口是 `python scripts/doctor.py`。它会检查已验证的 Python 版本（3.10–3.13）、Pillow 与必要导入、临时目录、RGB/RGBA PNG 往返、项目文件、验证器、衬线字体发现和正式运行时安装包。`python scripts/doctor.py --development --strict-packages` 是完整的本地开发检查。

视觉理解、图像生成、原生图像编辑和文件系统访问属于宿主能力，不是 pip 依赖。CI 覆盖 Ubuntu/Linux 的 Python 3.10–3.13、Windows 的 Python 3.12，以及 macOS 的 Python 3.13。运行时发布包继续保持现有 Skill 文件契约，并排除测试、缓存和仅供开发使用的文件。

依赖/导入检查命令是 `python tools/check_dependency_contract.py`；安装包和仓库卫生检查命令分别是 `python tools/check_package_parity.py` 与 `python tools/check_repository_hygiene.py`。

<a id="installation"></a>
## 📦 安装方法

<details>
<summary>展开两个版本的安装详情</summary>

### Original Edition

下载 [photo-abstract-editorial-original.zip](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/download/v1.0.0/photo-abstract-editorial-original.zip)，解压其中的 photo-abstract-editorial 文件夹，并安装到 Codex Skill 目录。Original 仅支持 Codex。

仓库中的副本是 [dist/photo-abstract-editorial-original.zip](dist/photo-abstract-editorial-original.zip)。

### V3 Adaptive Edition

下载 [photo-abstract-editorial-skill.zip](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/download/v3.0.0/photo-abstract-editorial-skill.zip)，或让 Codex 从公开仓库安装根目录 Skill。仓库中的副本是 [dist/photo-abstract-editorial-skill.zip](dist/photo-abstract-editorial-skill.zip)。

该安装包只包含 V3 运行环境文件。README 素材、评测文件、测试、缓存和临时输出不进入 V3 运行环境安装包。

</details>

<a id="usage"></a>
## 🚀 使用方法

<details>
<summary>展开其他使用方式</summary>

### Original Edition

~~~text
Use $photo-abstract-editorial to turn this photograph into a strict-fidelity photo-and-abstract editorial composition.
~~~

Original 提示词会调用历史 Codex-specific 工作流。

### V3 Adaptive Edition — 默认模式

默认 V3 提示词见[30 秒快速开始](#quick-start)。

### V3 Adaptive Edition — 系列模式

~~~text
Use $photo-abstract-editorial for this three-image series. Keep a restrained warm-ivory editorial family, but re-analyze each photograph and choose its own motif, layout, and spatial relationships.
~~~

当前 Skill 约束中的控制项是自然语言工作流输入，不是数值合成器 API。

</details>

<a id="input-output"></a>
## 🖼️ 输入与输出

普通源照片

→ 场景事实与源图派生关系

→ 抽象母题、面板与精确标题

→ 机器验证与视觉 QA

→ Photo Abstract Editorial 成片

<a id="same-source-showcase"></a>
## ↔️ Original 与 V3 同源对比

本对比使用 Original README 中的历史源图。Original 成片原样复用；V3 成片则在之后使用当前 V3 工作流从同一源图真实生成。

| 同一源图 | Original 历史成片 | V3 Adaptive 实际成片 |
|---|---|---|
| ![历史日落地平线源图](assets/readme/comparisons/original-horizon/source.png) | ![Original 历史成片](assets/readme/comparisons/original-horizon/original-result.png) | ![V3 同源成片](assets/readme/comparisons/original-horizon/v3-result.png) |

Original 保留固定的 lower-left 编辑行为。V3 将同一长地平线解析为 Wide Horizon，并应用当前的场景感知合成。这个对比解释的是不同决策，不表示某个版本无条件更好。

<a id="control-showcase"></a>
## 🎛️ V3 控制能力演示

下面三个输出使用同一 E03 Landscape 源图和同一 Wide Horizon 版式。它们是真实 Codex 编排层控制项提示词的结果，并全部通过机器验证器。

| Abstraction 30 | Abstraction 60 | Abstraction 80 |
|---|---|---|
| ![Abstraction 30](assets/readme/controls/abstraction-30.png) | ![Abstraction 60](assets/readme/controls/abstraction-60.png) | ![Abstraction 80](assets/readme/controls/abstraction-80.png) |

当前合成器没有将这些值暴露为数值命令行参数；报告把它们记录为编排层决策，而不是机器强制分数。

<a id="series-showcase"></a>
## 🗂️ V3 系列风格演示

下面三个实际输出接受了 Codex 侧系列风格评测：共享暖象牙色面板语言、Bodoni 字体排版体系、整段字距调整、克制留白与源图可追溯的标记语汇，同时保留各自的场景逻辑。

**同一视觉家族，不同源图逻辑。**

| Landscape | Street / Crowd | Minimal / Light |
|---|---|---|
| ![系列横向成片](assets/readme/series/landscape.png) | ![系列街道人群成片](assets/readme/series/street-crowd.png) | ![系列极简光线成片](assets/readme/series/minimal-light.png) |

这是对文档化 Series Style Lock 约束的真实 Codex 视觉 PASS 评审。当前运行环境没有名为 Series Style Lock 的独立机器标志；系列演示本身仍是 Codex 侧结果，而独立 DeepSeek 验证覆盖下文所述的确定性能力路径。

<a id="how-it-works"></a>
## ⚙️ 工作原理

<details>
<summary>展开工作流顺序</summary>

### Original Edition

照片 → Codex 视觉检查 → 无文字母题生成 → 历史清理辅助工具 → Original 合成器 → Original 验证器 → 视觉 QA。

### V3 Adaptive Edition

照片 → 场景分析 → 创意控制 → 版式选择 → 艺术指导 → 生成/编辑 → 质量门禁 → 必要时一次针对性修正 → 最终编辑成片。

### V3 Strict Fidelity 路径

透明母题 → 可移植色键清理 → 确定性合成器 → 本地精确排版 → manifest → 机器验证器。

</details>

<a id="validation"></a>
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

<a id="independent-validation"></a>
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

<a id="compatibility"></a>
## 🌐 兼容性

### Original Edition

**仅 CODEX。** Original 在其 Codex-specific 运行环境约束内完成实现和验证。不支持 Claude、Gemini、Cursor 或其他 Agent。

### V3 Adaptive Edition

- 已验证的运行环境路径：Codex Strict Fidelity，以及独立的 DeepSeek Harness Strict Fidelity 运行。
- 按能力设计：面向具备所需能力的图像 Agents/Harnesses。
- 针对已测试能力路径的跨 Agent 兼容性已验证；这不代表每个 Agent 都提供相同的原生工具。

DESIGNED FOR COMPATIBILITY 不等于 VALIDATED。

<a id="releases"></a>
## 📥 发布版本

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

<a id="switching"></a>
## 🔄 版本选择与切换

如果你偏好固定的历史视觉行为、使用 Codex 并希望更小的工作流，可以继续使用 Original。

如果你需要场景适配、四轴创意控制、自动版式、结构化 QA 或系列工作，可以尝试 V3。

Original 用户不需要迁移；两个安装包可以并行保留。

<a id="faq"></a>
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

<a id="technical-details"></a>
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

<a id="project-status"></a>
## 📌 项目状态

- Original Edition：支持、保留，并作为历史 v1.0.0 发布版本提供。
- V3 Adaptive Edition：当前正式稳定版，已完成 Codex 验证，并针对已测试能力路径完成 DeepSeek Harness 独立验证。
- 文档：三语言双版本 README 与真实演示素材。
- 跨 Agent 兼容性：针对已测试的 DeepSeek Harness 能力路径已验证；其他 Agent 尚未测试。
- 正式 v3.0.0：当前稳定版。

<a id="license"></a>
## ⚖️ 许可证

本项目及其公开发布版本使用 AGPL-3.0。参见 [LICENSE](LICENSE)。
