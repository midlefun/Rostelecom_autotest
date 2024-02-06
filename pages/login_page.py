from .base_page import BasePage
from .locators import LoginPageLocators as LPL
from playwright.sync_api import expect


class LoginPage(BasePage):
    def should_be_login_pages(self):
        self.should_be_login_url()
        self.should_be_input_by_login()
        self.should_be_register_form()

    def should_be_login_url(self):
        print(self.url)
        assert self.url == "https://lk.rt.ru/"

    def should_be_input_by_login(self):
        self.browser_fixture.wait_for_selector(LPL.LOGIN_INPUT)
        expect(self.browser_fixture.locator(LPL.LOGIN_INPUT)).to_be_visible(timeout=1000)

    def should_be_register_form(self):
        expect(self.browser_fixture.locator(LPL.LOGIN_ENTER_WITH_PASSWORD_BUTTON)).to_be_visible(timeout=1000)
        self.browser_fixture.locator(LPL.LOGIN_ENTER_WITH_PASSWORD_BUTTON).click()
        # self.browser_fixture.pause()

    # _BUTTON_LOGIN_MENU = '#lk-enter'
    # _LINK_LOGIN_PAGE = '.lk-popup__links .'
    # _BUTTON_TOWN_CHANGE_MODAL = '#block-b2cpanellichnykhkabinetoviligeo'
    #
    # def open_index_page(self, page: Page) -> None:
    #     page.goto(config.url.DOMAIN_MSC)
    #
    # def press_login_menu_button(self, page: Page) -> None:
    #     page.locator(self._BUTTON_LOGIN_MENU).click()
    #
    # def press_login_page_link(self, page: Page) -> None:
    #     page.get_by_text('Личный кабинет РФ').nth(0).click()
    #
    # def go_to_and_compare_url_login_page(self, page: Page) -> None:
    #     with page.context.expect_page() as login_page:
    #         self.press_login_page_link(page)
    #     new_page = login_page.value
    #     assert new_page.url == config.url.LOGIN
