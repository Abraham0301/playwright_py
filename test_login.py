import re
from playwright.sync_api import Page, expect

def test_valid_login(page: Page):
    # 1. 導航至登入頁面
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    # 2. 輸入用戶名 (注意 Admin 的 A 要大寫)
    page.get_by_placeholder("Username").fill("Admin")
    
    # 3. 輸入密碼
    page.locator('[name="password"]').fill("admin123")
    
    # 4. 點擊登入按鈕
    page.get_by_role("button", name="Login").click()
    
    # 5. 斷言：驗證是否跳轉到 Dashboard
    # 使用 re.compile 確保只要 URL 包含 dashboard 關鍵字即通過
    expect(page).to_have_url(re.compile(r".*dashboard"), timeout=10000)
    
    # 6. 執行登出流程
    # 點擊右上角頭像
    page.get_by_alt_text("profile picture").click()
    
    # 點擊 Logout 連結
    page.get_by_text("Logout").click()
    
    # 7. 斷言：驗證是否回到登入頁面
    expect(page).to_have_url(re.compile(r".*login"))
    
    print("\n測試成功：已完成登入與登出流程")