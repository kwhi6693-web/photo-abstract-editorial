# 🎨 Photo Abstract Editorial

一個以源圖保真為核心的 Agent Skill，將照片轉為具備自適應版式、可控抽象和確定性合成路徑的編輯作品。

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md)

[![Original](https://img.shields.io/badge/Original-Codex%20only-7a5c4f?style=flat-square)](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v1.0.0) [![V3 Adaptive](https://img.shields.io/badge/V3%20Adaptive-v3.0.0-c45a2f?style=flat-square)](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v3.0.0) [![Agent Skill](https://img.shields.io/badge/Type-Agent%20Skill-3f4856?style=flat-square)](https://github.com/kwhi6693-web/photo-abstract-editorial) [![Codex](https://img.shields.io/badge/Validated-Codex-6e5a76?style=flat-square)](https://github.com/kwhi6693-web/photo-abstract-editorial#compatibility)

Photo Abstract Editorial 保留源照片的事實內容，將源圖關係轉化為克制的抽象面板，並在已驗證路徑支援時使用本地排版生成標題。

<a id="before-after"></a>
## 轉換前 → 轉換後

**同一源圖 · 實際 V3 成片 · Strict Fidelity / 驗證器 PASS**

源圖原樣展示。右側是儲存庫中已有的 V3 同源成片；其 [manifest](assets/readme/comparisons/original-horizon/v3-result.png.manifest.json) 記錄了 pixel-exact 攝影區域，已發布的同源檢查報告為驗證器 PASS。

| 轉換前 | 轉換後 |
|---|---|
| ![同一源照片](assets/readme/comparisons/original-horizon/source.png) | ![同源實際 V3 成片](assets/readme/comparisons/original-horizon/v3-result.png) |

<a id="navigation"></a>
**快速跳轉：** [快速開始](#quick-start) · [作品畫廊](#gallery) · [選擇版本](#choose-an-edition) · [相容性](#compatibility) · [驗證](#validation) · [發布版本](#releases) · [環境合約](#environment-contract)

<a id="quick-start"></a>
## ⚡ 30 秒快速開始

V3 Adaptive 是大多數新使用者的推薦起點。

### 安裝

下載 [v3.0.0 發布 ZIP](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/download/v3.0.0/photo-abstract-editorial-skill.zip)，安裝其中的 Skill；也可以使用現有安裝器方法：

~~~text
Use $skill-installer to install the root photo-abstract-editorial Skill from https://github.com/kwhi6693-web/photo-abstract-editorial.
~~~

### 執行

~~~text
Use $photo-abstract-editorial to create an adaptive, source-faithful photo-and-abstract editorial from this image.
~~~

### 可選控制項

~~~text
Use $photo-abstract-editorial. Set Abstraction to 60, Creative Freedom to 45, Identity Preservation to 80, and Spatial Fidelity to 70.
~~~

<a id="gallery"></a>
## 🖼️ 作品畫廊

以下五張圖片均來自 RC 評測集，是實際的 V3 Codex Strict Fidelity 成片，並通過驗證器；不是宣傳重構圖。

| 純肖像 | 風景 | 建築 |
|---|---|---|
| ![V3 純肖像成片](assets/readme/v3/pure-portrait.png) | ![V3 風景成片](assets/readme/v3/landscape.png) | ![V3 建築成片](assets/readme/v3/architecture.png) |

| 靜物 | 極簡 / 光線 |
|---|---|
| ![V3 靜物成片](assets/readme/v3/still-life.png) | ![V3 極簡光線成片](assets/readme/v3/minimal-light.png) |

| 場景 | 版式 | 驗證 |
|---|---|---|
| 純肖像 | Vertical Monument | Strict Fidelity · 驗證器 PASS |
| 風景 | Wide Horizon | Strict Fidelity · 驗證器 PASS |
| 建築 | Centered Archive | Strict Fidelity · 驗證器 PASS |
| 靜物 | Sparse Object | Strict Fidelity · 驗證器 PASS |
| 極簡 / 光線 | Sparse Object | Strict Fidelity · 驗證器 PASS |

完整資料集與 manifest 見 [assets/evals/v3.0-rc1](assets/evals/v3.0-rc1) 和 [RC 評測報告](docs/evals/v3.0-rc1-real-world-evaluation.md)。

如果這個工作流對你有幫助，點一顆 ⭐ 能讓更多人發現這個專案。

<a id="why"></a>
## 為什麼選擇 Photo Abstract Editorial？

- 在已驗證的 Strict Fidelity 路徑中保留源照片。
- 根據場景選擇版式，不把所有源圖強行塞進同一個畫面。
- 讓抽象程度可控，並保持與照片的來源關係。
- 在 Strict Fidelity 下使用精確的本地排版。
- 在交付前執行結構化 QA。
- 在具備所需能力時提供可重現的確定性路徑。

通用圖像提示詞可能重繪源照片、遺失主體身份、編造沒有來源的事實、造成抽象程度不一致，或產生不可靠的排版。本專案將事實照片與生成的抽象母題分開，讓版式與創意決策明確化，並在交付前加入品質門禁。

<a id="choose-an-edition"></a>
## 🧭 選擇版本

**推薦大多數新使用者使用：V3 Adaptive。**

| | Original | V3 Adaptive |
|---|---|---|
| 執行環境 | 僅 Codex | 基於能力；已在 Codex 與經測試的 DeepSeek Harness 路徑驗證 |
| 版式 | 固定 | 自適應 |
| 控制項 | 手動 | 四個創意控制項 |
| QA | Original 驗證器 | 結構化 V3 QA |
| 最適合 | 歷史 Codex 工作流 | 目前推薦工作流 |

Original 繼續為希望使用固定 Codex 工作流的使用者提供支援。V3 是目前正式穩定版，適合場景適配、明確控制、自適應版式、結構化 QA 與系列工作。兩個版本可以並行保留。

- [Original v1.0.0 發布版本](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v1.0.0)
- [V3 Adaptive v3.0.0 發布版本](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v3.0.0)

<a id="original-vs-v3"></a>
## 🔍 Original 與 V3 比較

<details>
<summary>展開完整版本比較</summary>

| 維度 | Original Edition | V3 Adaptive Edition |
|---|---|---|
| 定位 | 保留的 V3 之前工作流 | 自適應照片加抽象面板 Skill |
| 執行環境 | 僅 Codex | Codex 與經測試的 DeepSeek Harness 能力路徑已驗證；按能力設計相容性 |
| 複雜度 | 更小的固定工作流 | 更多輸入、設定與驗證邊界 |
| 藝術指導 | 暖象牙色面板、源圖派生的克制母題、光學編輯間距 | 相同編輯基礎，加上場景感知藝術指導與控制項解析 |
| 源圖保真 | Original 範例已驗證攝影區域 pixel-exact | Codex 與經測試的 DeepSeek Harness 路徑已驗證 Strict Fidelity 攝影區域 pixel-exact |
| 創意控制 | 標題、面板、母題、對齊與字型手動覆蓋 | Abstraction、Creative Freedom、Identity Preservation、Spatial Fidelity，每項 0–100 |
| 場景設定 | 無 | 7 個：Pure Portrait、Environmental Portrait、Landscape、Architecture、Street/Crowd、Still Life、Minimal/Light |
| 肖像適配 | 來源支援時使用源圖派生的不等高縱向錨點 | 肖像感知場景設定與身份保留解析 |
| 版式系統 | Lower Editorial 前身：左下或底部置中 | 5 個規範設定：Lower Editorial、Wide Horizon、Vertical Monument、Centered Archive、Sparse Object |
| QA | 機器驗證器加視覺 QA；Original 範例有 9 項驗證 | 結構化 8 維 QA、機器驗證器與明確的 HARD FAIL 規則 |
| 重試 | 一次針對性母題修正；最多兩次母題嘗試 | 完整嘗試後一次針對性修正；仍有關鍵 HARD FAIL 時停止 |
| 系列 | 沒有 Series Style Lock 約束 | 可選 Series Style Lock 流程 |
| Agent 相容性 | 僅 Codex | Codex 與經測試的 DeepSeek Harness 能力路徑已驗證；其他宿主仍取決於能力 |
| 安裝 | 歷史 Original 安裝包 | V3 Adaptive 安裝包與目前穩定版 |
| 最適合 | 穩定、熟悉、Codex 專用的 Original 行為 | 不同場景、明確控制、自適應版式與系列工作 |
| 主要取捨 | 自適應性較少，不能移植到 Codex 之外 | 流程與能力要求更多；不同宿主的原生工具仍有差異 |

</details>

<a id="scope"></a>
## 🎯 適用範圍、限制與能力保證

<details>
<summary>展開適用範圍與保證詳情</summary>

### Original Edition

適合在 Codex 中使用一張照片、一個無文字母題與一個固定編輯構圖。它提供確定性本地合成以及 Original 的源圖/面板檢查。不提供 V3 控制系統、場景設定、規範自動版式、Series Style Lock 或跨 Agent 合約。不支援在 Codex 之外執行。

### V3 Adaptive Edition

適合需要明確場景推理、身份與空間控制、自適應版式或系列視覺家族的照片。V3 不會憑空生成沒有來源的人物、建築、物體、地理資訊、文字、Logo、水印、色卡或裝飾性事實。圖像生成會因宿主與執行次序而變化；目前公開證據包括 Codex Strict Fidelity 與經獨立測試的 DeepSeek Harness 能力路徑。

### 能力保證矩陣

| 能力 | Original | V3 Strict Fidelity | V3 Native Image Edit | V3 Reference Generation |
|---|---|---|---|---|
| 源圖感知行為 | 已實作並經 Codex 驗證 | 已在 Codex 與經測試的 DeepSeek Harness 路徑實作並驗證 | 盡力而為 | 盡力而為 |
| 場景適配 | 固定 Original 行為 | 已實作並經 Codex 評測 | 僅藝術指導約束 | 僅藝術指導約束 |
| 創意控制 | 手動覆蓋 | 4 個控制項，0–100 | 取決於宿主的盡力而為 | 取決於宿主的盡力而為 |
| 攝影區域 pixel-exact | Original 範例已驗證 | 滿足 Strict 條件時機器驗證 | 不保證 | 不保證 |
| 精確本地排版 | Original 合成器路徑 | 本地排版路徑 | 不保證 | 不保證 |
| 確定性合成 | Original 本地合成器 | V3 本地合成器 | 不保證 | 不保證 |
| 機器驗證 | Original 驗證器 | V3 驗證器與 manifest | 不是 Strict 輸出 | 不是 Strict 輸出 |
| 宿主相容性 | 僅 Codex | Codex 與經測試的 DeepSeek Harness 路徑已驗證；面向具備所需能力的宿主設計 | 取決於能力 | 取決於能力 |

Native Image Edit 與 Reference Generation 不得被描述為機器驗證的 Strict 成片。

</details>

<a id="features"></a>
## ✨ 主要功能

<details>
<summary>展開功能級約束</summary>

### Original Edition

- 一張源照片與一個稀疏的無文字母題。
- 源圖派生的色帶、間隙、偏移，以及在來源支援時使用的不等高縱向錨點。
- 暖象牙色面板、克制配色、精確英文標題與光學間距。
- 確定性本地合成與 JSON manifest。
- Original 源圖/輸出衝突保護與逐像素攝影區域驗證。
- 機器驗證與視覺 QA。

### V3 Adaptive Edition

- 在 Strict Fidelity、Native Image Edit、Reference Generation 之間進行基於能力的路由。
- 四個 Creative Controls：Abstraction、Creative Freedom、Identity Preservation、Spatial Fidelity。
- 7 個場景設定與肖像感知抽象。
- 5 個確定性版式設定。
- 結構化 8 維 QA 與有邊界的針對性重試。
- 可選 Series Style Lock 流程。
- 可攜式色鍵清理、本地精確排版、manifest、機器驗證器與可重現安裝包。

</details>

<a id="execution-modes"></a>
## 🧩 V3 執行模式

<details>
<summary>展開模式邊界</summary>

### Strict Fidelity

當宿主具備視覺理解、圖像生成、本地檔案存取、Python、相容 Pillow 的處理能力與可用襯線字型時，V3 可以提供確定性合成、精確本地排版、manifest、機器驗證器，以及在不縮放時對攝影區域進行 pixel-exact 驗證。

### Native Image Edit

以源圖作為編輯/參考圖，在宿主支援時遵循相同的藝術指導與 QA 約束。這是盡力而為，不保證 pixel-exact、確定性、精確本地排版或機器驗證的 Strict 結果。

### Reference Generation

以源圖作為唯一事實參考，執行依賴模型的生成路徑。這是盡力而為，不提供 Strict Fidelity 保證。

</details>

<a id="requirements"></a>
## 📋 執行要求

<details>
<summary>展開執行要求</summary>

### Original Edition

**僅 Codex。** Original 工作流需要 Codex 視覺檢查、內建圖像生成路徑、歷史工作流使用的 Codex 工作區/執行環境輔助工具、Python 3.10–3.13（CI 已驗證）、Pillow、可用襯線字型、一張照片與透明母題。

### V3 Strict Fidelity

需要視覺理解、圖像生成、本地檔案系統存取、Python 3.10–3.13（CI 已驗證）、相容 Pillow 的處理能力、可用襯線字型、一張照片與透明母題。

### V3 Native Image Edit

需要視覺理解與宿主的圖像編輯/合成能力；不提供 pixel-exact Strict 保證。

### V3 Reference Generation

需要視覺理解、圖像生成與參考圖支援；結果依賴模型，屬於盡力而為。

</details>

### 開發測試

測試執行器僅作為開發依賴，不會進入任何執行階段發布包。從全新檢出開始，建立隔離環境、安裝儲存庫開發依賴，然後直接執行 `pytest`：

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
## 🩺 環境合約

本地合成器與驗證器只使用 `Pillow` 這一項 Python 執行階段依賴。從儲存庫執行腳本時，請依 [requirements.txt](requirements.txt) 安裝；[requirements-dev.txt](requirements-dev.txt) 會重用執行階段清單，並額外加入僅供開發使用的 `pytest` 測試執行器。

唯讀預檢入口是 `python scripts/doctor.py`。它會檢查已驗證的 Python 版本（3.10–3.13）、Pillow 與必要匯入、暫存目錄、RGB/RGBA PNG 往返、專案檔案、驗證器、襯線字型發現與正式執行階段安裝包。`python scripts/doctor.py --development --strict-packages` 是完整的本地開發檢查。

視覺理解、圖像生成、原生圖像編輯與檔案系統存取屬於宿主能力，不是 pip 依賴。CI 覆蓋 Ubuntu/Linux 的 Python 3.10–3.13、Windows 的 Python 3.12，以及 macOS 的 Python 3.13。執行階段發布包繼續保持現有 Skill 檔案合約，並排除測試、快取與僅供開發使用的檔案。

依賴/匯入檢查命令是 `python tools/check_dependency_contract.py`；安裝包與儲存庫衛生檢查命令分別是 `python tools/check_package_parity.py` 與 `python tools/check_repository_hygiene.py`。

<a id="installation"></a>
## 📦 安裝方法

<details>
<summary>展開兩個版本的安裝詳情</summary>

### Original Edition

下載 [photo-abstract-editorial-original.zip](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/download/v1.0.0/photo-abstract-editorial-original.zip)，解壓其中的 photo-abstract-editorial 資料夾，並安裝到 Codex Skill 目錄。Original 僅支援 Codex。

儲存庫中的副本是 [dist/photo-abstract-editorial-original.zip](dist/photo-abstract-editorial-original.zip)。

### V3 Adaptive Edition

下載 [photo-abstract-editorial-skill.zip](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/download/v3.0.0/photo-abstract-editorial-skill.zip)，或讓 Codex 從公開儲存庫安裝根目錄 Skill。儲存庫中的副本是 [dist/photo-abstract-editorial-skill.zip](dist/photo-abstract-editorial-skill.zip)。

該安裝包只包含 V3 執行環境檔案。README 素材、評測檔案、測試、快取與暫存輸出不進入 V3 執行環境安裝包。

</details>

<a id="usage"></a>
## 🚀 使用方法

<details>
<summary>展開其他使用方式</summary>

### Original Edition

~~~text
Use $photo-abstract-editorial to turn this photograph into a strict-fidelity photo-and-abstract editorial composition.
~~~

Original 提示詞會呼叫歷史 Codex-specific 工作流。

### V3 Adaptive Edition — 預設模式

預設 V3 提示詞見[30 秒快速開始](#quick-start)。

### V3 Adaptive Edition — 系列模式

~~~text
Use $photo-abstract-editorial for this three-image series. Keep a restrained warm-ivory editorial family, but re-analyze each photograph and choose its own motif, layout, and spatial relationships.
~~~

目前 Skill 約束中的控制項是自然語言工作流輸入，不是數值合成器 API。

</details>

<a id="input-output"></a>
## 🖼️ 輸入與輸出

普通源照片

→ 場景事實與源圖派生關係

→ 抽象母題、面板與精確標題

→ 機器驗證與視覺 QA

→ Photo Abstract Editorial 成片

<a id="same-source-showcase"></a>
## ↔️ Original 與 V3 同源比較

本比較使用 Original README 中的歷史源圖。Original 成片原樣重用；V3 成片則在之後使用目前 V3 工作流從同一源圖真實生成。

| 同一源圖 | Original 歷史成片 | V3 Adaptive 實際成片 |
|---|---|---|
| ![歷史日落地平線源圖](assets/readme/comparisons/original-horizon/source.png) | ![Original 歷史成片](assets/readme/comparisons/original-horizon/original-result.png) | ![V3 同源成片](assets/readme/comparisons/original-horizon/v3-result.png) |

Original 保留固定的 lower-left 編輯行為。V3 將同一長地平線解析為 Wide Horizon，並套用目前的場景感知合成。這個比較解釋的是不同決策，不表示某個版本無條件更好。

<a id="control-showcase"></a>
## 🎛️ V3 控制能力演示

以下三個輸出使用同一 E03 Landscape 源圖與同一 Wide Horizon 版式。它們是真實 Codex 編排層控制項提示詞的結果，並全部通過機器驗證器。

| Abstraction 30 | Abstraction 60 | Abstraction 80 |
|---|---|---|
| ![Abstraction 30](assets/readme/controls/abstraction-30.png) | ![Abstraction 60](assets/readme/controls/abstraction-60.png) | ![Abstraction 80](assets/readme/controls/abstraction-80.png) |

目前合成器沒有將這些值暴露為數值命令列參數；報告把它們記錄為編排層決策，而不是機器強制分數。

<a id="series-showcase"></a>
## 🗂️ V3 系列風格演示

以下三個實際輸出接受了 Codex 側系列風格評測：共享暖象牙色面板語言、Bodoni 字體排版體系、整段字距調整、克制留白與源圖可追溯的標記語彙，同時保留各自的場景邏輯。

**同一視覺家族，不同源圖邏輯。**

| Landscape | Street / Crowd | Minimal / Light |
|---|---|---|
| ![系列橫向成片](assets/readme/series/landscape.png) | ![系列街道人群成片](assets/readme/series/street-crowd.png) | ![系列極簡光線成片](assets/readme/series/minimal-light.png) |

這是對文件化 Series Style Lock 約束的真實 Codex 視覺 PASS 評審。目前執行環境沒有名為 Series Style Lock 的獨立機器標誌；系列演示本身仍是 Codex 側結果，而獨立 DeepSeek 驗證涵蓋下文所述的確定性能力路徑。

<a id="how-it-works"></a>
## ⚙️ 工作原理

<details>
<summary>展開工作流順序</summary>

### Original Edition

照片 → Codex 視覺檢查 → 無文字母題生成 → 歷史清理輔助工具 → Original 合成器 → Original 驗證器 → 視覺 QA。

### V3 Adaptive Edition

照片 → 場景分析 → 創意控制 → 版式選擇 → 藝術指導 → 生成/編輯 → 品質門禁 → 必要時一次針對性修正 → 最終編輯成片。

### V3 Strict Fidelity 路徑

透明母題 → 可攜式色鍵清理 → 確定性合成器 → 本地精確排版 → manifest → 機器驗證器。

</details>

<a id="validation"></a>
## ✅ 驗證

以下數字來自目前公開原始碼與 v3.0.0 正式發布，不是歷史估算。

- Original Edition：隔離的 v1.0.0 工作樹中 32/32 測試通過。
- Original Edition：自身構建器與 --check 通過；歷史範例驗證器返回 ok=true。
- Original 安裝包：9 個執行環境檔案；SHA-256 為 a1a44b1a9cec9ba04b379a7d3a14315701abb14bb93e953003337870772d0a6d。
- V3 Adaptive Edition：Codex 上 41/41 測試通過。
- V3 安裝包：15 個執行環境檔案；安裝包構建與 --check 通過。
- V3 RC 評測：7 個場景成片與 5 個控制變體通過驗證器與攝影區域逐像素檢查。
- V3 版式：5 個規範版式全部在真實源圖上執行過。
- V3 同源比較：新的 V3 成片驗證器 PASS。
- V3 安裝包排除 README 素材、docs/evals、測試、快取與暫存輸出。

重點是可驗證，而不只是生成。

<a id="independent-validation"></a>
## 🔬 獨立驗證

獨立的 DeepSeek Harness 已完成確定性能力路徑驗證。

- DeepSeek Harness：PASS
- Strict Fidelity：在本次測試流水線上 VERIFIED
- 專案測試：41/41 通過
- 結構化視覺/編輯 QA：8/8 PASS
- 機器驗證器：`ok: true`；驗證錯誤：`[]`
- 阻塞問題：0
- 跨 Agent 相容性：針對已測試能力路徑 VERIFIED
- 流程冒煙檢查：`remove_chroma_key.py`、`compose_editorial.py`、`validate_editorial.py` 均以 0 退出

詳見簡潔的 [DeepSeek Harness 獨立驗證摘要](docs/evals/deepseek-harness-validation.md)。本次驗證中的 DeepSeek Harness 未提供原生神經圖像生成能力，因此母題使用確定性的 Pillow 程式化生成。該限制不影響已驗證的攝影區域逐像素一致性、源圖雜湊、幾何、排版、確定性合成或機器驗證結果。

<a id="compatibility"></a>
## 🌐 相容性

### Original Edition

**僅 CODEX。** Original 在其 Codex-specific 執行環境約束內完成實作與驗證。不支援 Claude、Gemini、Cursor 或其他 Agent。

### V3 Adaptive Edition

- 已驗證的執行環境路徑：Codex Strict Fidelity，以及獨立的 DeepSeek Harness Strict Fidelity 執行。
- 按能力設計：面向具備所需能力的圖像 Agents/Harnesses。
- 針對已測試能力路徑的跨 Agent 相容性已驗證；這不代表每個 Agent 都提供相同的原生工具。

DESIGNED FOR COMPATIBILITY 不等於 VALIDATED。

<a id="releases"></a>
## 📥 發布版本

### Photo Abstract Editorial — Original Edition

- 標籤：v1.0.0
- 執行環境：僅 Codex
- 發布頁：[Original Edition 發布頁](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v1.0.0)
- 安裝包：[photo-abstract-editorial-original.zip](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/download/v1.0.0/photo-abstract-editorial-original.zip)
- 演示：保留歷史 README 源圖/成片對
- 審計：[Original Edition 功能與來源審計](docs/releases/original-edition.md)

### Photo Abstract Editorial V3 Adaptive — v3.0.0

- 標籤：v3.0.0
- 發布頁：[V3 Adaptive 正式穩定版](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/tag/v3.0.0)
- 安裝包：[photo-abstract-editorial-skill.zip](https://github.com/kwhi6693-web/photo-abstract-editorial/releases/download/v3.0.0/photo-abstract-editorial-skill.zip)
- 驗證：Codex 回歸、構建、安裝包與正式發布前校驗 PASS
- 獨立驗證：DeepSeek Harness 針對已測試確定性能力路徑 PASS

v3.0.0 是目前正式穩定版。

<a id="switching"></a>
## 🔄 版本選擇與切換

如果你偏好固定的歷史視覺行為、使用 Codex 並希望更小的工作流，可以繼續使用 Original。

如果你需要場景適配、四軸創意控制、自動版式、結構化 QA 或系列工作，可以嘗試 V3。

Original 使用者不需要遷移；兩個安裝包可以並行保留。

<a id="faq"></a>
## ❓ 常見問題

### Original 可以在 Codex 之外執行嗎？

不可以。Original 是 CODEX ONLY。

### 應該下載哪個版本？

想要歷史固定 Codex 工作流就下載 Original；想要自適應場景邏輯與明確控制就下載 V3。

### V3 必須手動設定控制項嗎？

不需要。預設工作流會從源圖解析它們；你也可以在需要明確傾向時提供自然語言數值。

### 為什麼 Native Image Edit 與 Reference Generation 不能保證 pixel-exact？

因為它們依賴宿主或模型的圖像操作，而不是本地確定性 Strict 合成器。

### 兩個版本可以同時保留嗎？

可以。這正是雙版本發布結構的目的。

### V3 已在 Claude、Gemini 或 Cursor 上驗證了嗎？

沒有納入本專案的公開驗證證據。DeepSeek Harness 已針對已測試確定性能力路徑完成獨立驗證；其他 Agent 仍取決於能力且尚未測試。

### Series Style Lock 實際保留什麼？

它保留面板語言、配色、排版、留白與標記語彙等視覺家族，同時重新分析每張源圖，而不是複製座標或母題。

<a id="technical-details"></a>
## 🛠️ 技術細節

<details>
<summary>V3 執行環境結構</summary>

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
<summary>可重現安裝包</summary>

Original 使用歷史 v1.0.0 程式碼樹中的 Original Edition 建構器，包含 9 個執行環境檔案。V3 使用目前建構器，包含 15 個執行環境檔案。兩個建構器都會排除僅開發用途內容，並根據各自程式碼樹驗證歸檔條目。

</details>

<details>
<summary>Manifest 與 Strict 檢查</summary>

V3 manifest 記錄源圖/輸出雜湊、渲染後攝影區域雜湊、面板幾何資訊、版式設定、母題區域、清理詳情與排版執行記錄。驗證器檢查 manifest、尺寸、幾何資訊、面板角點、源圖雜湊、輸出雜湊與攝影區域像素。

</details>

<a id="project-status"></a>
## 📌 專案狀態

- Original Edition：支援、保留，並作為歷史 v1.0.0 發布版本提供。
- V3 Adaptive Edition：目前正式穩定版，已完成 Codex 驗證，並針對已測試能力路徑完成 DeepSeek Harness 獨立驗證。
- 文件：三語言雙版本 README 與真實演示素材。
- 跨 Agent 相容性：針對已測試的 DeepSeek Harness 能力路徑已驗證；其他 Agent 尚未測試。
- 正式 v3.0.0：目前穩定版。

<a id="license"></a>
## ⚖️ 授權條款

本專案及其公開發布版本使用 AGPL-3.0。參見 [LICENSE](LICENSE)。
