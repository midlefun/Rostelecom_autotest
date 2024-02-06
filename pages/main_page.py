from .base_page import BasePage
from .locators import MainPageLocators as MPL
from .login_page import LoginPage
from playwright.sync_api import expect


class MainPage(BasePage):

    def check_lk_enter_button_is_visible(self):
        expect(self.browser_fixture.locator(MPL.ENTER_BUTTON),
               'Кнопка вызова меню личного кабинета не отображается на странице').to_be_visible(timeout=1000)

    def go_to_lk_enter_menu(self):
        self.browser_fixture.locator(MPL.ENTER_BUTTON).click()

    # TODO: Разбить функцию на две разные ?
    def press_lk_link(self) -> None:
        with self.browser_fixture.context.expect_page() as login_page:
            self.browser_fixture.get_by_text('Личный кабинет РФ').nth(0).click()
        new_page = login_page.value
        # TODO:Избавиться от ошибки деление str на INT
        return LoginPage(browser_fixture=new_page, url=new_page.url)
