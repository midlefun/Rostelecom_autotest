from .base_page import BasePage
from .locators import MainPageLocators as MPL
from .login_page import LoginPage
from playwright.sync_api import expect


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser_fixture.wait_for_selector(MPL.LOGIN_PAGE_LINK)
        login_link.click()

    def should_be_login_page(self):
        expect(self.browser_fixture.locator(MPL.LOGIN_PAGE_LINK), 'Поле Логин не отображается на странице').to_be_visible(timeout=1000)

        # def press_login_page_link(self) -> None:
        #     self.browser_fixture.get_by_text('Личный кабинет РФ').nth(0).click()
        #     print(self.browser_fixture, self.browser_fixture.url)
        #     return LoginPage(browser_fixture=self.browser_fixture, url=self.browser_fixture.url)

    def press_login_page_link(self) -> None:
        with self.browser_fixture.context.expect_page() as login_page:
            self.browser_fixture.get_by_text('Личный кабинет РФ').nth(0).click()
        new_page = str(login_page.value)
        #TODO:Избавиться от ошибки деление str на INT

        # self.browser_fixture.get_by_text('Личный кабинет РФ').nth(0).click()
        # print(self.browser_fixture, self.browser_fixture.url)

        print(self.browser_fixture)
        print(new_page.url)

        return LoginPage(browser_fixture=new_page, url=new_page.url)

        # assert new_page.url == config.url.LOGIN
