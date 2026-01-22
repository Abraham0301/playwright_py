# Playwright Python Automation Framework

這是一個基於 Python 與 Playwright 的自動化測試練習專案，目前已完成 **POM (Page Object Model)** 架構實作，並處理了實際自動化測試中會遇到的同步與定位問題。

---

## 🛠 技術實作重點

### 1. 架構設計 (POM)
為了讓腳本好維護，我將頁面元素與測試動作封裝在 `pages/` 下，避免測試腳本（Test Scripts）過於臃腫：
* **`login_page.py`**: 負責導航、登入欄位操作與登出邏輯。
* **`pim_page.py`**: 負責處理 PIM 模組，包含附件區塊的定位與檔案上傳。

### 2. 踩坑與解決方案
在開發過程中，我針對以下常見的自動化測試問題進行了優化：
* **穩定性優化 (Flaky Test)**：原本登出後直接檢查 URL 會因為系統重導向時間差導致 Assertion Error。改用等待「登入按鈕」重新出現（To be visible）後再斷言，解決了測試不穩定的問題。
* **精準定位 (Strict Mode Violation)**：OrangeHRM 頁面存在多個重複的 "Save" 按鈕。我改用 **容器定位** 方式，先縮定範圍至 `.orangehrm-attachment` 再尋找按鈕，成功解決 Playwright 找不到唯一元素的問題。
* **檔案上傳處理**：實作了動態路徑獲取，並加入測試後的環境清理機制（自動移除產生的 `test_upload.txt`）。

---

## 📂 專案結構
```text
/python_playwright
├── pages/                  # Page Objects (邏輯封裝)
├── test_login.py           # 登入功能測試
├── test_upload.py          # 附件上傳功能測試
├── pytest.ini              # Pytest 配置
└── .gitignore              # 排除 Cache 與測試報告
