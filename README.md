# Marketing Growth Skills

五個主題包，來源為 [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)（MIT 授權，見 `LICENSE`）：

- 「Marketing & Growth」、「AAS Marketing, SEO & Growth」、「Creative Director」：v18.9.0
- 「AAS Web App Builder」、「AAS Secure App Builder」：v20.4.0

技能放在 `.claude/skills/`，用 Claude Code 開啟這個倉庫時會自動載入。

| 技能 | 用途 |
| --- | --- |
| `ab-test-setup` | 設計 A/B 測試：假設、變體、樣本數 |
| `analytics-tracking` | 設計與稽核追蹤埋點 |
| `content-creator` | 依品牌語氣撰寫與檢查內容（附品牌語氣、SEO 分析腳本） |
| `content-strategy` | 內容策略、主題群集、編輯路線圖 |
| `email-sequence` | Email 自動化序列 |
| `programmatic-seo` | 程式化 SEO 大量頁面 |
| `seo-audit` | SEO 健檢：爬取、索引、排名 |
| `copywriting` | 轉換導向的著陸頁與 Email 文案 |
| `schema-markup` | schema.org 結構化資料設計與驗證 |
| `seo-content-planner` | SEO 內容大綱與主題群集 |
| `seo-fundamentals` | SEO 基礎：E-E-A-T、Core Web Vitals（附 SEO 檢查腳本） |
| `algorithmic-art` | 用 p5.js 生成演算法藝術 |
| `canvas-design` | 海報、視覺設計稿（附 OFL 授權字型） |
| `copy-editing` | 行銷文案校稿與改寫 |
| `frontend-design` | 在既有品牌規範內設計前端介面 |
| `interactive-portfolio` | 能帶來工作與客戶的作品集網站 |
| `accessibility-compliance-accessibility-audit` | 依 WCAG 範圍稽核頁面與流程的無障礙 |
| `browser-automation` | 用語意定位與有界等待寫穩定的瀏覽器檢查 |
| `build-ui` | UI 開發的逐步工作流程 |
| `form-cro` | 名單蒐集、聯絡等表單（非註冊）的轉換優化 |
| `frontend-api-integration-patterns` | 前端串接後端 API 的實務模式 |
| `frontend-developer` | React 元件、響應式版面、前端狀態管理 |
| `javascript-pro` | 現代 JavaScript、非同步模式、Node.js API |
| `nextjs-app-router-patterns` | Next.js App Router 架構與 Server Components |
| `nextjs-best-practices` | Next.js App Router 原則：資料取得、路由 |
| `nodejs-best-practices` | Node.js 框架選擇與非同步模式 |
| `react-best-practices` | React／Next.js 效能優化指南 |
| `react-patterns` | 現代 React 模式：Hooks、組合、效能 |
| `shadcn` | 管理 shadcn/ui 元件 |
| `tailwind-patterns` | Tailwind CSS v4 原則與模式 |
| `typescript-expert` | TypeScript 型別設計與效能（附本機 `tsc` 診斷腳本） |
| `ui-a11y` | 稽核並修正元件或頁面的無障礙問題 |
| `ui-states` | 首次使用、空白、載入、錯誤、離線等 UI 狀態 |
| `api-security-best-practices` | 安全的 API 設計：驗證、授權、輸入檢查 |
| `auth-implementation-patterns` | 實作或審查身分驗證與授權（token、session、資源權限） |
| `backend-security-coder` | 後端安全程式碼：輸入驗證、驗證機制 |
| `cc-skill-security-review` | 安全實務與潛在漏洞審查 |
| `dependency-management-deps-audit` | 相依套件漏洞掃描與授權合規 |
| `django-access-review` | Django／DRF 存取控制與 IDOR 審查 |
| `frontend-security-coder` | 前端安全：XSS 防護、輸出淨化 |
| `pci-compliance` | 支付資料流程與 PCI 範圍控制審查 |
| `sast-configuration` | 靜態安全掃描（SAST）工具設定與自訂規則 |
| `secrets-management` | CI/CD 機密管理：Vault、AWS Secrets Manager 等 |
| `security-requirement-extraction` | 從威脅模型推導安全需求 |
| `threat-modeling-expert` | 威脅建模、安全架構審查、風險評估 |

## 更新

上游在 v20 起移除了 `agentic-bundle-marketing-growth` 和 `agentic-bundle-creative-director`，這兩包要從 v18.9.0 標籤取得：

```bash
git clone --depth 1 --branch v18.9.0 https://github.com/sickn33/agentic-awesome-skills.git /tmp/aas-v18
git clone --depth 1 https://github.com/sickn33/agentic-awesome-skills.git /tmp/aas
rm -rf .claude/skills && mkdir -p .claude/skills
cp -r /tmp/aas-v18/plugins/agentic-bundle-marketing-growth/skills/* .claude/skills/
cp -r /tmp/aas-v18/plugins/agentic-bundle-creative-director/skills/* .claude/skills/
cp -r /tmp/aas/plugins/agentic-bundle-aas-marketing-seo-growth/skills/* .claude/skills/
cp -r /tmp/aas/plugins/agentic-bundle-web-app/skills/* .claude/skills/
cp -r /tmp/aas/plugins/agentic-bundle-aas-secure-app-builder/skills/* .claude/skills/
python scripts/validate_skills.py
```

後面複製的會覆蓋前面同名的技能，所以重疊的技能會以最新版為準。
