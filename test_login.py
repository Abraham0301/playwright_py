import re
import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_orange_hrm_login_logout(page: Page):
    """
    測試目標：驗證 OrangeHRM 系統的完整登入與登出流程。
    採用 POM 架構提升代碼維護性，並使用元素斷言確保測試穩定性。
    """
    
    # 1. 初始化頁面物件 (POM)
    login_page = LoginPage(page)

    # 2. 導航至目標網站
    # 使用 navigate 方法（這需要在你的 login_page.py 中定義）
    login_page.navigate()

    # 3. 執行登入動作
    # 封裝好的動作，讓測試腳本語意更清晰
    login_page.login("Admin", "admin123")

    # 4. 驗證登入是否成功
    # 檢查 URL 是否包含 dashboard，並設定 10 秒緩衝時間處理網路延遲
    expect(page).to_have_url(re.compile(r".*dashboard"), timeout=10000)
    
    # 額外驗證：確保畫面上出現了 Dashboard 標題（確保 UI 渲染完成）
    dashboard_header = page.get_by_role("heading", name="Dashboard")
    expect(dashboard_header).to_be_visible()
    print("Log: 登入驗證成功，已進入儀表板")

    # 5. 執行登出流程
    # 點擊用戶頭像並選擇登出
    login_page.logout()

    # 6. 驗證登出是否成功 (關鍵優化點！)
    # 不要只檢查 URL，先檢查「登入按鈕」是否重新出現。
    # 這能有效解決重導向過程中 URL 暫時不匹配導致的失敗 (Flaky Test)。
    login_button = page.get_by_role("button", name="Login")
    expect(login_button).to_be_visible(timeout=10000)
    
    # 最後再確認一次網址，確保回到登入頁
    expect(page).to_have_url(re.compile(r".*login"))
    print("Log: 登出驗證成功，已回到登入頁面")


    # pages/login_page.py (檢查清單)
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.user_dropdown = page.get_by_alt_text("profile picture")
        self.logout_link = page.get_by_text("Logout")

    def navigate(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def login(self, user, pwd):
        self.username_input.fill(user)
        self.password_input.fill(pwd)
        self.login_button.click()

    def logout(self):
        self.user_dropdown.click()
        self.logout_link.click()