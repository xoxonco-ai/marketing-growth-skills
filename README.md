# Marketing Growth Skills

「Marketing & Growth」與「AAS Marketing, SEO & Growth」兩個主題包，來源為 [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) v18.9.0（MIT 授權，見 `LICENSE`）。

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

## 更新

```bash
git clone --depth 1 https://github.com/sickn33/agentic-awesome-skills.git /tmp/aas
rm -rf .claude/skills && mkdir -p .claude/skills
cp -r /tmp/aas/plugins/agentic-bundle-marketing-growth/skills/* .claude/skills/
cp -r /tmp/aas/plugins/agentic-bundle-aas-marketing-seo-growth/skills/* .claude/skills/
```
