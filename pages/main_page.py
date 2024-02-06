from .base_page import BasePage

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser_fixture.wait_for_selector('#lk-enter')
        login_link.click()


