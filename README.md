# Lightweight Adaptive Photo Abstract Editorial

[中文](#中文) | [English](#english)

公开仓库 / Public repository: [kwhi6693-web/photo-abstract-editorial](https://github.com/kwhi6693-web/photo-abstract-editorial)

最新版安装包 / Latest package: [`dist/photo-abstract-editorial-skill.zip`](dist/photo-abstract-editorial-skill.zip)

## 中文

这是一个轻量、跨 Agent 的 Photo Abstract Editorial Agent Skill：把一张照片变成“完整原片区域 + 照片关系派生的抽象面板 + 精确英文标题”的编辑作品。

主要能力：

- capability-based routing，按主机真实能力选择 Strict Fidelity、Native Image Edit 或 Reference Generation；
- 可控的 Abstraction、Creative Freedom、Identity Preservation、Spatial Fidelity 四轴；
- 7 个场景 profile，包含纯人像、环境人像、风景、建筑、街头/人群、静物、极简/光线；
- 5 个确定性版式 profile：Lower Editorial、Wide Horizon、Vertical Monument、Centered Archive、Sparse Object；
- 结构化 8 维视觉 QA、一次 targeted correction 和明确的 HARD FAIL 停止规则；
- 明确区分主角身份保留与人群节奏，避免把纯人像主角一律简化成短竖线；
- 多图系列的可选 Style Lock，保持视觉家族但重新分析每张照片；
- 在具备本地 Python、Pillow、文件访问和可用衬线字体时，继续提供确定性合成、精确标题、manifest 和摄影区域逐像素验证。

### 三种执行模式

**Strict Fidelity** 需要视觉理解、图像生成、文件访问、本地 Python/script、Pillow 和字体。它只生成抽象 motif，使用本地清理、确定性 compositor、manifest 和 validator 合成最终结果；照片区域默认 pixel-exact，标题由本地字体精确渲染。

**Native Image Edit** 需要视觉理解和图像编辑/合成能力。它使用原图作为 edit/reference source，沿用相同的 art direction、scene、controls、layout 和 QA，但不能保证 pixel-exact、deterministic 或 machine-verified 的摄影区域保留。

**Reference Generation** 需要视觉理解、图像生成和 reference-image 支持。原图是唯一事实来源，结果是 best-effort source fidelity；同样不能声称 Strict Mode 的 pixel-exact、deterministic 或 machine-verified 保证。

如果主机没有视觉理解或任何图像生成/编辑能力，Skill 会停止，不伪造能力。Codex 是已验证的 Strict Mode 环境之一，但 Skill 的通用 contract 不依赖某个特定 Agent 或工具名称。

### 安装与使用

在 Codex 中可以直接告诉 Agent：

> 使用 `$skill-installer` 从 `https://github.com/kwhi6693-web/photo-abstract-editorial` 安装根目录的 `photo-abstract-editorial` Skill。

也可以下载 [`dist/photo-abstract-editorial-skill.zip`](dist/photo-abstract-editorial-skill.zip)，解压后把 `photo-abstract-editorial` 文件夹复制到 `~/.codex/skills/`。安装后上传一张照片并使用：

> 使用 `$photo-abstract-editorial` 把这张照片制作成自适应、严格保真的摄影抽象编辑作品。

Strict Fidelity 的本地运行依赖为 Python 3.10+、Pillow、可用衬线字体、源照片和 motif PNG。项目自带 `scripts/remove_chroma_key.py`，不依赖某个图像工具私有安装目录中的 helper。

### 验证与打包

```text
python -m unittest discover -s tests -v
python tools/build_skill_package.py
python tools/build_skill_package.py --check
python scripts/validate_editorial.py --source SOURCE --output OUTPUT --manifest MANIFEST
```

Strict validator 必须输出 JSON `"ok": true`。安装包是可重复构建的，包含 15 个实际运行时文件，不包含 tests、docs/evals、cache、`__pycache__` 或临时文件；构建器会统一文本 LF 换行并固定 ZIP 时间戳。

### 示例

| 输入 | 输出 |
|---|---|
| ![输入照片](assets/examples/source-horizon.png) | ![完成作品](assets/examples/result-horizon.png) |

示例只是结构和严格验证基线，不应复用其题材、标题、色彩或版式。

## English

This is a lightweight, capability-based Photo Abstract Editorial Agent Skill. It turns one photograph into a vertical editorial composition with the complete source photo, a source-derived abstract panel, and exact English typography.

### Capabilities

- cross-agent capability routing across Strict Fidelity, Native Image Edit, and Reference Generation;
- controllable Abstraction, Creative Freedom, Identity Preservation, and Spatial Fidelity;
- scene-aware and portrait-aware abstraction across seven profiles;
- deterministic layout intelligence across Lower Editorial, Wide Horizon, Vertical Monument, Centered Archive, and Sparse Object;
- structured eight-dimension visual QA with a bounded one-correction retry;
- optional series style lock for a consistent visual family without duplicating motifs or coordinates;
- deterministic local composition, exact local typography, manifest output, and pixel-exact photo preservation whenever the host supports the Strict toolchain.

### Mode boundaries

Universal / Native Image Edit and Reference Generation modes are broadly compatible and use the source as the factual reference, but they cannot guarantee pixel-exact source preservation, deterministic photo preservation, or machine-verified Strict output.

Strict Fidelity additionally needs local file access, Python 3.10+, Pillow, a usable serif font, and a transparent motif. It provides deterministic photo/panel/motif assembly, exact typography, a manifest, a machine validator, and pixel-exact verification of the rendered photo region when no resizing is requested.

The generic workflow is capability-based; Codex is only one verified Strict environment. No image-capable host may invent people, buildings, objects, geography, text, logos, watermarks, swatches, or unsupported decoration.

### Install and use

For Codex, ask:

> Use `$skill-installer` to install the root `photo-abstract-editorial` Skill from `https://github.com/kwhi6693-web/photo-abstract-editorial`.

Alternatively, download [`dist/photo-abstract-editorial-skill.zip`](dist/photo-abstract-editorial-skill.zip), extract it, and install the `photo-abstract-editorial` directory in the host Skill directory. Then attach a photograph and ask:

> Use `$photo-abstract-editorial` to create an adaptive, source-faithful photo-and-abstract editorial composition.

### Runtime structure

```text
photo-abstract-editorial/
|- SKILL.md
|- agents/openai.yaml
|- references/
|  |- art-direction.md
|  |- control-system.md
|  |- scene-profiles.md
|  |- layout-profiles.md
|  |- quality-check.md
|  |- series-style.md
|  `- example-pair.md
|- scripts/
|  |- compose_editorial.py
|  |- remove_chroma_key.py
|  `- validate_editorial.py
`- assets/examples/
```

Development tests and evaluation notes stay outside the clean installable package. Run the commands above to verify tests, rebuild the deterministic archive, check package contents, and validate the supplied example.
