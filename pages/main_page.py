from .base_page import BasePage
from .locators import MainPageLocators as MPL
from playwright.sync_api import expect


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser_fixture.wait_for_selector(MPL.LOGIN_PAGE_LINK)
        login_link.click()

    def should_be_login_page(self):
        expect(self.browser_fixture.locator(MPL.LOGIN_PAGE_LINK)).to_be_visible(timeout=1000)
