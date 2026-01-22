# Playwright Python Automation Framework

這是一個基於 **Python** 與 **Playwright** 實作的高品質端到端（E2E）自動化測試專案。本專案模擬真實世界的測試需求，展示了自動化腳本的穩定性設計與除錯技術。

## 專案亮點
- **專業斷言機制**：利用 Web-First Assertions（智慧斷言）與 **正規表示法 (Regex)**，確保在動態網頁跳轉中的穩定性。
- **除錯工具整合**：完整整合 Playwright **Trace Viewer**，可記錄並回放每一格測試動作、網絡請求與控制台日誌。
- **自動化生命週期**：透過 Pytest 框架管理測試生命週期，具備高度的可擴充性。
- **容錯設計**：實作智慧等待機制，徹底解決傳統測試中常見的 Flaky Test（不穩定測試）問題。

---

##  目錄結構
- `tests/test_login.py`: 主要測試邏輯（包含 OrangeHRM 登入/登出流程驗證）。
- `pytest.ini`: 全域測試配置檔（設定自動開啟錄製與瀏覽器參數）。
- `.gitignore`: 排除快取與測試報告，保持倉庫整潔。

---

##  環境安裝與執行

### 1. 安裝環境依賴
建議使用 Python 3.8+ 環境：
```bash
pip install pytest-playwright
playwright install
