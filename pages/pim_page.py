class PimPage:
    def __init__(self, page):
        self.page = page
        # 1. 先定位到「附件區」這個容器
        self.attachment_section = page.locator(".orangehrm-attachment")
        
        # 2. 在附件區內尋找按鈕
        self.add_button = self.attachment_section.get_by_role("button", name="Add")
        self.file_input = page.locator("input[type='file']")
        
        # 3. 關鍵修正：只找附件區裡的 Save 按鈕
        self.save_button = self.attachment_section.get_by_role("button", name="Save")

    def upload_file(self, file_path):
        # 捲動到附件區，避免被上方選單遮擋
        self.attachment_section.scroll_into_view_if_needed()
        
        self.add_button.click()
        self.file_input.set_input_files(file_path)
        self.save_button.click()