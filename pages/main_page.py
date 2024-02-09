from .base_page import BasePage
from .locators import MainPageLocators as MPL
from .login_page import LoginPage
from playwright.sync_api import expect
import config


class MainPage(BasePage):

    # def check_lk_enter_button_is_visible(self):
    #     expect(self.browser_fixture.locator(MPL.ENTER_BUTTON),
    #            'Кнопка вызова меню личного кабинета не отображается на странице').to_be_visible(
    #         timeout=config.expectations.LOCATOR_TIMEOUT)

    def go_to_lk_enter_menu(self):
        # self.browser_fixture.locator(MPL.ENTER_BUTTON).click()
        self.find_element(MPL.ENTER_BUTTON, config.expectations.LOCATOR_TIMEOUT).click()
        # self.browser_fixture.wait_for_timeout(30)
        # self.browser_fixture.locator(MPL.ENTER_BUTTON).click()

    def press_lk_link(self) -> None:
        with self.browser_fixture.context.expect_page() as login_page:
            self.browser_fixture.get_by_text('Личный кабинет РФ').nth(0).click()
        new_page = login_page.value
        return LoginPage(browser_fixture=new_page, url=new_page.url)
