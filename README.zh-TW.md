# PHOTO ABSTRACT EDITORIAL

## 01. Hero

**一個專案，兩種版本，由你選擇。**

這是一個將普通照片轉化為 Photo Abstract Editorial 的 Agent Skill：原照片始終是事實錨點，克制的抽象面板與精確英文標題共同形成編輯作品。

![V3 Adaptive 同源 Hero：日落地平線照片、源圖派生抽象面板與精確標題](assets/readme/hero/v3-original-source.png)

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md)

[Original Edition](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v1.0.0) · [V3 Adaptive Edition](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v3.0.0-rc2)

本專案同時保留兩個真實版本。它們不是互相取代的關係，而是針對不同工作流、環境與控制需求進行最佳化。

## 02. Language Switcher

- [English](README.md)
- [简体中文](README.zh-CN.md)
- [繁體中文](README.zh-TW.md)

## 03. Quick Navigation

[選擇版本](#04-選擇版本) · [版本比較](#06-original-vs-v3-比較) · [範圍與保證](#07-範圍限制與保證) · [真實 Demo](#15-真實-demo-畫廊) · [驗證](#20-驗證) · [Release](#22-releases)

## 04. 選擇版本

| | Original Edition | V3 Adaptive Edition |
|---|---|---|
| 定位 | 保留的原始 Codex 工作流 | 自適應、capability-based 的 V3 工作流 |
| Runtime | 僅支援 CODEX | Codex 已驗證；面向具備所需能力的 image-capable Agents/Harnesses 設計 |
| 視覺行為 | 固定、克制 | 場景感知、可控制、版式感知 |
| 下載 | [Original Release](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v1.0.0) | [目前 V3 RC](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v3.0.0-rc2) |

### Original Edition

如果你希望使用歷史固定工作流、已經使用 Codex，並偏好更簡單的原始 art-direction contract，請選擇 Original。

### V3 Adaptive Edition

如果你需要場景適配、四軸控制、自動版式選擇、結構化 QA、有邊界的修正，或一致的多圖視覺家族，請選擇 V3。

## 05. 該選擇哪個版本？

- 想要原始固定視覺行為？選擇 Original Edition。
- 需要場景適配、控制、版式 profile 或系列一致性？選擇 V3 Adaptive Edition。
- 正在使用非 Codex Agent？Original 不支援。若宿主具備所需圖像與本地處理能力，V3 可能適用，但額外 Agent runtime validation 仍待完成。
- 想要最小且最忠實於歷史的安裝包？選擇 Original。
- 想要更明確的 capability 與 verification contract？選擇 V3。

## 06. Original vs V3 比較

| 維度 | Original Edition | V3 Adaptive Edition |
|---|---|---|
| 定位 | V3 之前保留的工作流 | 自適應 photo-plus-abstraction Skill |
| Runtime 環境 | 僅 Codex | Codex 已驗證；依 capability-based compatibility 設計 |
| 複雜度 | 更小、更固定 | 更多輸入、profile 與 verification boundary |
| Art direction | 暖象牙色面板、源圖派生 muted motif、光學編輯間距 | 保留編輯基礎，並增加場景感知 art direction 與 control resolution |
| Source fidelity | Original 範例已驗證 pixel-exact 攝影區域 | Codex Strict Fidelity 已驗證 pixel-exact 攝影區域 |
| Creative controls | 手動標題、面板、motif、對齊與字型 override | Abstraction、Creative Freedom、Identity Preservation、Spatial Fidelity，各 0–100 |
| Scene Profiles | 無 | 7 個：Pure Portrait、Environmental Portrait、Landscape、Architecture、Street/Crowd、Still Life、Minimal/Light |
| Portrait adaptation | 在適合時使用源圖派生的不等高縱向錨點 | portrait-aware scene profile 與 identity-preservation resolution |
| Layout system | Lower Editorial 前身：lower-left 或 bottom-center | 5 個 canonical profile：Lower Editorial、Wide Horizon、Vertical Monument、Centered Archive、Sparse Object |
| QA | machine validator + visual QA；Original 範例有 9 項 validator checks | 結構化 8 維 QA、machine validator 與明確的 HARD FAIL 規則 |
| Retry | 一次 targeted motif correction；最多兩次 motif attempt | 完整嘗試後最多一次 targeted correction；關鍵 HARD FAIL 仍存在時停止 |
| Series | 沒有 Series Style Lock contract | 可選 Series Style Lock 流程 |
| Agent compatibility | 僅 Codex | 面向具備能力的 image-capable Agents/Harnesses 設計；目前只有 Codex 已驗證 |
| Installation | 歷史 Original package | V3 Adaptive package 與目前 RC |
| 適用場景 | 穩定、熟悉、Codex-specific 的原始行為 | 不同場景、明確控制、版式適配與系列工作 |
| 主要取捨 | 自適應較少，不能脫離 Codex | 流程與能力要求更多；額外 Agent validation 待完成 |

## 07. 範圍、限制與保證

### Original Edition

適合在 Codex 中用一張照片、一個無文字 motif 與一個固定編輯版式完成一次作品。它提供確定性本地合成與 Original validator 的 source/panel 檢查，但不提供 V3 control system、scene profiles、canonical auto-layout、Series Style Lock 或 cross-Agent contract。它不支援 Codex 之外的宿主。

### V3 Adaptive Edition

適合需要明確場景推理、身份與空間控制、自適應版式或系列視覺家族的照片。V3 不應憑空生成沒有來源的人物、建築、物體、地理、文字、logo、水印、色卡或裝飾事實。不同宿主與執行的圖像生成可能變化；目前公開 V3 證據來自 Codex。

### Guarantee Matrix

| 能力 | Original | V3 Strict Fidelity | V3 Native Image Edit | V3 Reference Generation |
|---|---|---|---|---|
| Source-aware behavior | 已實現，並在 Codex 驗證 | 已實現，並在 Codex 驗證 | best effort | best effort |
| Scene adaptation | 原始固定行為 | 已實現，並在 Codex 評測 | 僅 art-direction contract | 僅 art-direction contract |
| Creative controls | 手動 override | 4 個 control，0–100 | 取決於宿主的 best effort | 取決於宿主的 best effort |
| Pixel-exact photo region | Original 範例已驗證 | Strict 條件滿足時 machine-validated | 不保證 | 不保證 |
| Exact local typography | Original compositor path | local typography path | 不保證 | 不保證 |
| Deterministic composition | Original local compositor | V3 local compositor | 不保證 | 不保證 |
| Machine validation | Original validator | V3 validator 與 manifest | 不屬於 Strict output | 不屬於 Strict output |
| Host compatibility | 僅 Codex | Codex 已驗證；面向 suitable capability-based hosts 設計 | 取決於能力 | 取決於能力 |

Native Image Edit 與 Reference Generation 不能被描述為 machine-verified Strict output。

## 08. 這個專案解決什麼問題？

通用圖像 prompt 可能重繪原照片、遺失主體身份、編造沒有來源的事實、讓抽象程度不一致，或產生不可靠的 typography。固定版式也可能適合一張照片，卻不適合另一張。

Photo Abstract Editorial 將事實照片與生成的抽象 motif 分開，讓版式與創意決策明確化，在具備 Strict Fidelity 時使用本地 typography，並在交付前加入 quality gate。Original 保留第一版穩定工作流；V3 讓自適應決策更加明確。

## 09. 主要能力

### Original Edition

- 一張源照片與一個稀疏無文字 motif。
- 源圖派生的色帶、間隙、偏移，以及在來源支援時使用的不等高縱向錨點。
- 暖象牙色面板、muted palette、精確英文標題與光學間距。
- 確定性本地合成與 JSON manifest。
- Original source/output collision guards 與 pixel-level photo-region validation。
- Machine validation 與 visual QA。

### V3 Adaptive Edition

- 在 Strict Fidelity、Native Image Edit、Reference Generation 之間進行 capability-based routing。
- 四個 Creative Controls：Abstraction、Creative Freedom、Identity Preservation、Spatial Fidelity。
- 7 個 Scene Profiles 與 portrait-aware abstraction。
- 5 個確定性 Layout Profiles。
- 結構化 8 維 QA 與有邊界的 targeted retry。
- 可選 Series Style Lock 流程。
- portable chroma cleanup、exact local typography、manifest、machine validator 與 reproducible package。

## 10. V3 Execution Modes

### Strict Fidelity

當宿主具備視覺理解、圖像生成、本地檔案存取、Python、Pillow-compatible processing 與可用襯線字型時，V3 可以提供 deterministic composition、exact local typography、manifest、machine validator，以及在不縮放時對攝影區域進行 pixel-exact verification。

### Native Image Edit

以源圖作為 edit/reference image，在宿主支援時沿用相同的 art-direction 與 QA contract。這是 best effort，不保證 pixel-exact、deterministic、exact-local-typography 或 machine-verified Strict。

### Reference Generation

以源圖作為唯一事實參考，執行 model-dependent generation path。這是 best effort，不提供 Strict Fidelity 保證。

## 11. Requirements

### Original Edition

**僅 Codex。** Original workflow 需要 Codex visual inspection、內建 image-generation path、歷史工作流使用的 Codex workspace/runtime helper、Python 3.10+、Pillow、可用襯線字型、一張照片與透明 motif。

### V3 Strict Fidelity

需要視覺理解、圖像生成、本地檔案系統存取、Python 3.10+、Pillow-compatible processing、可用襯線字型、一張照片與透明 motif。

### V3 Native Image Edit

需要視覺理解與宿主的 image-editing/composition capability；不提供 pixel-exact Strict guarantee。

### V3 Reference Generation

需要視覺理解、圖像生成與 reference-image support；結果依賴模型且為 best effort。

## 12. Installation

### Original Edition

下載 [photo-abstract-editorial-original.zip](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/download/v1.0.0/photo-abstract-editorial-original.zip)，解壓其中的 photo-abstract-editorial 資料夾，並安裝到 Codex Skill 目錄。Original 僅支援 Codex。

儲存庫中的副本是 [dist/photo-abstract-editorial-original.zip](dist/photo-abstract-editorial-original.zip)。

### V3 Adaptive Edition

下載 [photo-abstract-editorial-skill.zip](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/download/v3.0.0-rc2/photo-abstract-editorial-skill.zip)，或直接讓 Codex 從公開儲存庫安裝根目錄 Skill：

儲存庫中的副本是 [dist/photo-abstract-editorial-skill.zip](dist/photo-abstract-editorial-skill.zip)。

~~~text
Use $skill-installer to install the root photo-abstract-editorial Skill from https://github.com/kwhi6693-web/photo-abstract-editorial.
~~~

該 package 只包含 V3 runtime 檔案。README assets、evaluation files、tests、cache 與暫存輸出不進入 V3 runtime package。

## 13. Usage

### Original Edition

~~~text
Use $photo-abstract-editorial to turn this photograph into a strict-fidelity photo-and-abstract editorial composition.
~~~

Original prompt 會呼叫歷史 Codex-specific workflow。

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

目前 Skill contract 中的 control 是自然語言工作流輸入，不聲稱是 numeric compositor API。

## 14. Input → Output

普通源照片

→ 場景事實與源圖派生關係

→ 抽象 motif、面板與精確標題

→ machine validation 與 visual QA

→ Photo Abstract Editorial 成品

## 15. 真實 Demo 畫廊

以下 V3 圖片全部來自 RC evaluation corpus，是實際 Codex Strict Fidelity 輸出並通過 validator；不是宣傳用重構圖。

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

完整 corpus 與 manifests 見 [assets/evals/v3.0-rc1](assets/evals/v3.0-rc1) 與 [RC evaluation report](docs/evals/v3.0-rc1-real-world-evaluation.md)。

## 16. Original vs V3 同源 Demo

本比較使用 Original README 中的歷史 source。Original result 原樣重用；V3 result 則在之後使用目前 V3 workflow 從同一 source 真實生成。

| 同一 source | Original 歷史 result | V3 Adaptive 實際 result |
|---|---|---|
| ![歷史日落地平線 source](assets/readme/comparisons/original-horizon/source.png) | ![Original 歷史 result](assets/readme/comparisons/original-horizon/original-result.png) | ![V3 同源 result](assets/readme/comparisons/original-horizon/v3-result.png) |

Original 保留固定的 lower-left 編輯行為。V3 將同一長地平線解析為 Wide Horizon，並套用目前的 scene-aware composition。這個比較解釋的是不同決策，不表示某個版本無條件更好。

## 17. V3 Control Showcase

以下三個輸出使用同一 E03 Landscape source 與同一 Wide Horizon layout。它們是真實 Codex orchestration-level control prompt 的結果，並全部通過 machine validator。

| Abstraction 30 | Abstraction 60 | Abstraction 80 |
|---|---|---|
| ![Abstraction 30](assets/readme/controls/abstraction-30.png) | ![Abstraction 60](assets/readme/controls/abstraction-60.png) | ![Abstraction 80](assets/readme/controls/abstraction-80.png) |

目前 compositor 沒有將這些值暴露為 numeric command-line argument；報告把它們記錄為 orchestration decisions，而不是 machine-enforced scores。

## 18. V3 Series Showcase

以下三個實際輸出接受了 Codex-side series-style evaluation：共享暖象牙色面板語言、Bodoni typography family、whole-run kerning、克制留白與源圖可追溯的 mark vocabulary，同時保留各自的 scene logic。

**同一視覺家族，不同源圖邏輯。**

| Landscape | Street / Crowd | Minimal / Light |
|---|---|---|
| ![Series landscape](assets/readme/series/landscape.png) | ![Series street crowd](assets/readme/series/street-crowd.png) | ![Series minimal light](assets/readme/series/minimal-light.png) |

這是對文件化 Series Style Lock contract 的真實 Codex visual PASS review。目前 runtime 沒有名為 Series Style Lock 的獨立 machine flag，這也不構成獨立 Agent validation。

## 19. How It Works

### Original Edition

Photograph → Codex visual inspection → 無文字 motif generation → 歷史 cleanup helper → Original compositor → Original validator → visual QA。

### V3 Adaptive Edition

Photograph → Scene Analysis → Creative Controls → Layout Selection → Art Direction → Generation/Edit → Quality Gate → 必要時一次 targeted correction → Final Editorial。

### V3 Strict Fidelity path

透明 motif → portable chroma cleanup → deterministic composer → exact local typography → manifest → machine validator。

## 20. 驗證

以下數字來自目前公開 source 與本輪 release preparation，不是歷史估算。

- Original Edition：隔離的 v1.0.0 worktree 中 32/32 tests 通過。
- Original Edition：自身 builder 與 --check 通過；歷史 example validator 返回 ok=true。
- Original package：9 個 runtime files；SHA-256 為 a1a44b1a9cec9ba04b379a7d3a14315701abb14bb93e953003337870772d0a6d。
- V3 Adaptive Edition：Codex 上 41/41 tests 通過。
- V3 package：15 個 runtime files；package build 與 --check 通過。
- V3 RC evaluation：7 個 scene results 與 5 個 control variants 通過 validator 與 photo-region pixel-exact checks。
- V3 layouts：5 個 canonical layouts 全部在真實 source 上執行過。
- V3 同源比較：新的 V3 result validator PASS。
- V3 package 排除 README assets、docs/evals、tests、cache 與暫存輸出。

Built to be checked, not just generated.

## 21. Compatibility

### Original Edition

**僅 CODEX。** Original 在其 Codex-specific runtime contract 內完成實作與驗證。不支援 Claude、Gemini、Cursor 或其他 Agent。

### V3 Adaptive Edition

- Validated runtime：Codex。
- Designed for capability-based compatibility：具備所需能力的 suitable image-capable Agents/Harnesses。
- Independent runtime validation on additional Agents：PENDING。

DESIGNED FOR COMPATIBILITY 不等於 VALIDATED。

## 22. Releases

### Photo Abstract Editorial — Original Edition

- Tag：v1.0.0
- Runtime：Codex only
- Release：[Original Edition release](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v1.0.0)
- Artifact：[photo-abstract-editorial-original.zip](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/download/v1.0.0/photo-abstract-editorial-original.zip)
- Demo：保留歷史 README source/result pair
- Audit：[Original Edition 功能與 provenance 審計](docs/releases/original-edition.md)

### Photo Abstract Editorial V3 Adaptive — v3.0.0-rc2

- Tag：v3.0.0-rc2
- Release：[V3 Adaptive prerelease](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v3.0.0-rc2)
- Artifact：[photo-abstract-editorial-skill.zip](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/download/v3.0.0-rc2/photo-abstract-editorial-skill.zip)
- Validation：Codex-side tests 與 RC evidence PASS
- Limitation：獨立 additional-Agent runtime validation 待完成

正式 v3.0.0 有意不發布。

## 23. Switching / Upgrade Guide

如果你偏好固定的歷史視覺行為、使用 Codex 並希望更小的 workflow，可以繼續使用 Original。

如果你需要 scene adaptation、四軸 creative controls、自動版式、結構化 QA 或 series work，可以嘗試 V3。

Original 使用者不需要遷移；兩個 package 可以並行保留。

## 24. FAQ

### Original 可以在 Codex 之外執行嗎？

不可以。Original 是 CODEX ONLY。

### 應該下載哪個版本？

想要歷史固定 Codex workflow 就下載 Original；想要自適應場景邏輯與明確控制就下載 V3。

### V3 必須手動設定 controls 嗎？

不需要。預設 workflow 會從 source 解析它們；你也可以在需要明確傾向時提供自然語言數值。

### 為什麼 Native Image Edit 與 Reference Generation 不能保證 pixel-exact？

因為它們依賴宿主或模型的圖像操作，而不是本地確定性 Strict compositor。

### 兩個版本可以同時保留嗎？

可以。這正是 dual-edition release structure 的目的。

### V3 已在 Claude、Gemini 或 Cursor 上驗證了嗎？

沒有。額外 Agent runtime validation 待完成。

### Series Style Lock 實際保留什麼？

它保留面板語言、palette、typography、whitespace 與 mark vocabulary 等視覺家族，同時重新分析每張 source，而不是複製座標或 motif。

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

Original 使用歷史 v1.0.0 tree 中的 Original Edition builder，包含 9 個 runtime files。V3 使用目前 builder，包含 15 個 runtime files。兩個 builder 都會排除 development-only 內容，並根據各自 source tree 驗證 archive entries。

</details>

<details>
<summary>Manifest 與 Strict checks</summary>

V3 manifest 記錄 source/output hashes、rendered photo-region hash、panel geometry、layout profile、motif region、cleanup details 與 typography runs。validator 檢查 manifest、尺寸、geometry、panel corners、source hash、output hash 與 photo-region pixels。

</details>

## 26. Project Status

- Original Edition：支援、保留，並作為歷史 v1.0.0 release 提供。
- V3 Adaptive Edition：目前公開 release candidate，已完成 Codex validation。
- Documentation：三語言 dual-edition README 與真實 Demo assets。
- Independent additional-Agent runtime validation：待完成。
- 正式 v3.0.0：未發布。

## 27. License

本專案及其公開 releases 使用 AGPL-3.0。參見 [LICENSE](LICENSE)。
