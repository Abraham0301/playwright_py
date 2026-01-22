import os
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.pim_page import PimPage

def test_file_upload_verification(page: Page):
    # 1. 準備測試檔案
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "test_upload.txt")
    with open(file_path, "w") as f:
        f.write("Hello Playwright Portfolio Test!")

    # 2. 登入
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("Admin", "admin123")

    # 3. 模擬真人點擊進入 PIM 頁面 (解決 ERR_ABORTED)
    # 點擊左側選單的 PIM
    page.get_by_role("link", name="PIM").click()
    
    # 點擊第一個員工進入詳情
    page.locator(".oxd-table-card").first.click()
    
    # 點擊右側或下方的 "Attachments" (或直接滾動到附件區)
    # 注意：OrangeHRM 介面可能隨版本變動，這裡改用 PIM 頁面物件
    pim_page = PimPage(page)
    
    # 4. 執行上傳
    # 確保 pim_page.py 裡面的 upload_file 有處理點擊 Add 的動作
    pim_page.upload_file(file_path)

    # 5. 驗證
    expect(page.get_by_text("test_upload.txt")).to_be_visible(timeout=10000)
    
    # 6. 清理
    os.remove(file_path)