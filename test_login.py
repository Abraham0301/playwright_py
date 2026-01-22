import re
import pytest
from playwright.sync_api import Page, expect

# 定義測試案例
def test_orange_hrm_login_logout(page: Page):
    """
    測試目標：驗證 OrangeHRM 系統的登入與登出流程
    """
    
    # 1. 導航至目標網站
    # 設定較長的 timeout 確保在網路不穩時也能成功加載
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", timeout=30000)

    # 2. 執行登入動作
    # 使用 get_by_placeholder 定位，這是 Playwright 推薦的最穩定定位方式之一
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    
    # 點擊登入按鈕
    page.get_by_role("button", name="Login").click()

    # 3. 驗證登入是否成功
    # 使用 re.compile 進行正規匹配，只要 URL 包含 dashboard 即通過
    # expect 內建自動重試機制，預設會等待 5 秒
    expect(page).to_have_url(re.compile(r".*dashboard"), timeout=10000)
    
    # 額外驗證：確保畫面上出現了 Dashboard 標題（確保頁面渲染完成）
    dashboard_header = page.get_by_role("heading", name="Dashboard")
    expect(dashboard_header).to_be_visible()
    print("登入驗證成功：已進入儀表板")

    # 4. 執行登出流程
    # 點擊右上角用戶頭像選單
    page.get_by_alt_text("profile picture").click()
    
    # 點擊登出演算
    page.get_by_text("Logout").click()

    # 5. 驗證登出是否成功
    # 確保頁面跳轉回登入頁
    expect(page).to_have_url(re.compile(r".*login"))
    
    # 確保登入輸入框重新出現，代表登出程序徹底完成
    expect(page.get_by_placeholder("Username")).to_be_visible()
    print("登出驗證成功：已返回登入頁面")

if __name__ == "__main__":
    # 此段落方便你直接執行此檔案進行偵錯
    pytest.main([__file__, "--headed"])