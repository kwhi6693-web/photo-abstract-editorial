# Photo Abstract Editorial

[中文](#中文) | [English](#english)

公开仓库 / Public repository: [kwhi6693-web/photo-abstract-editorial](https://github.com/kwhi6693-web/photo-abstract-editorial)

最新版安装包 / Latest package: [`dist/photo-abstract-editorial-skill.zip`](dist/photo-abstract-editorial-skill.zip)

## 中文

把一张照片制作成“完整原片区域 + 照片关系派生的抽象面板 + 精确英文标题”的竖向编辑作品。图像生成只负责无文字抽象母题；照片、均匀面板和标题由本地脚本确定性合成，并在交付前逐像素验证摄影区域。

### 主要改进

- 默认保留完整照片，不让图像模型重绘最终摄影区域。
- 标题使用本地高对比衬线字体与自然整词字距；可将一个连接词缩小并改为斜体。
- 使用光学边距组织图形与标题，不强求所有元素机械对齐。
- 当原图有决定性的竖向主体时，使用一主一辅、不同高度和粗细的短竖线；其余关系仍以负形断口与横向错层表达。
- 自动生成 JSON 清单，逐像素验证摄影区域，并清除孤立色键噪点。
- 合成器拒绝让输出覆盖原图、抽象 motif、已有结果或已有 manifest。
- 禁止色卡、logo、地点标签、水印、额外文字和无来源装饰。
- 只有机器验证和视觉检查同时通过才交付。

### 安装与使用

推荐直接告诉 Codex：

> 使用 `$skill-installer` 从 `https://github.com/kwhi6693-web/photo-abstract-editorial` 安装根目录的 `photo-abstract-editorial` Skill。

也可以下载 [`dist/photo-abstract-editorial-skill.zip`](dist/photo-abstract-editorial-skill.zip)，解压后把 `photo-abstract-editorial` 文件夹复制到 `~/.codex/skills/`。安装后开启新任务并上传一张照片：

> 使用 `$photo-abstract-editorial` 把这张照片制作成严格保真的摄影抽象编辑作品。

依赖：Codex 内置 `imagegen`、Python 3.10+、Pillow，以及可用的衬线字体。Skill 会优先使用 Codex 工作区提供的绝对 Python 路径，并使用 imagegen 的色键移除辅助脚本。

### 验证状态

- 官方 Skill 结构校验通过。
- 全部自动化测试通过。
- 示例摄影区域逐像素一致。
- 可重复构建的安装包只包含 9 个当前运行时文件，不包含测试和工作缓存。

### 已验证示例

| 输入 | 输出 |
|---|---|
| ![输入照片](assets/examples/source-horizon.png) | ![完成作品](assets/examples/result-horizon.png) |

示例仅用于说明流程，不应复用其题材、标题、色彩或版式。

## English

Turn one photograph into a vertical editorial composition containing the complete source photo, a photo-derived abstract panel, and exact English typography. Image generation creates only a text-free motif; local scripts assemble and validate the photograph, uniform panel, and title.

### Key improvements

- Preserve the complete photograph instead of asking a model to redraw the final photo region.
- Typeset exact titles locally with a high-contrast serif and native whole-run kerning; optionally style one connector in a smaller matching italic.
- Use optical spacing between the motif and title rather than mechanically equal margins.
- When the source has decisive vertical structures, translate them into one primary and one subordinate unequal anchor; keep negative gaps and horizontal offsets dominant elsewhere.
- Write a JSON manifest, compare every decoded photograph-region pixel, and remove isolated chroma-key components.
- Reject output paths that would overwrite the source, motif, an existing result, or an existing manifest.
- Reject swatches, logos, place labels, watermarks, extra text, and unsupported decoration.
- Deliver only after deterministic validation and visual QA both pass.

### Install and use

Recommended: ask Codex directly:

> Use `$skill-installer` to install the root `photo-abstract-editorial` Skill from `https://github.com/kwhi6693-web/photo-abstract-editorial`.

Alternatively, download [`dist/photo-abstract-editorial-skill.zip`](dist/photo-abstract-editorial-skill.zip), extract it, and copy the `photo-abstract-editorial` folder into `~/.codex/skills/`. Start a new task and attach one photograph:

> Use `$photo-abstract-editorial` to create a strict-fidelity photo-and-abstract editorial from this image.

Requirements: Codex built-in `imagegen`, Python 3.10+, Pillow, and an available serif font. The Skill prefers Codex's absolute workspace Python path and the imagegen chroma-key removal helper.

### Validation status

- Official Skill structure validation passes.
- All automated tests pass.
- The example photograph region is pixel-exact.
- The reproducible downloadable package contains only the nine current runtime files, without tests or work caches.

### Validated example

| Source | Result |
|---|---|
| ![Source photograph](assets/examples/source-horizon.png) | ![Completed composition](assets/examples/result-horizon.png) |

The example demonstrates the workflow only. Do not reuse its subject, title, palette, or composition.

## Repository structure

```text
photo-abstract-editorial/
|- SKILL.md
|- agents/openai.yaml
|- scripts/
|  |- compose_editorial.py
|  `- validate_editorial.py
|- references/
|  |- art-direction.md
|  `- example-pair.md
|- assets/examples/
|  |- source-horizon.png
|  |- result-horizon.png
|  `- result-horizon.png.manifest.json
|- docs/evals/legacy-baseline.md
|- dist/photo-abstract-editorial-skill.zip
|- tests/
`- tools/build_skill_package.py
```

Run `python tools/build_skill_package.py --check` to verify that every archived runtime file exactly matches the repository; run it without `--check` to rebuild the archive deterministically. The public README, packaging tool, evaluation notes, and development tests are intentionally excluded from the clean installable package. No license is asserted because the repository does not currently contain a LICENSE file.
