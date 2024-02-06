from .base_page import BasePage
from .locators import LoginPageLocators as LPL
from playwright.sync_api import expect


class LoginPage(BasePage):
    link = "https://lk.rt.ru/"

    def check_lk_page_is_active(self):
        self.should_be_lk_url()
        self.should_be_input_by_email_or_telephone()
        self.should_be_enter_with_password_button()

    def should_be_lk_url(self):
        assert self.url == self.link

    def should_be_input_by_email_or_telephone(self):
        self.browser_fixture.wait_for_selector(LPL.EMAIL_OR_TELEPHONE_INPUT)
        expect(self.browser_fixture.locator(LPL.EMAIL_OR_TELEPHONE_INPUT),
               'Поле E-mail или номер телефона не отображается на странице').to_be_visible(timeout=1000)

    def should_be_enter_with_password_button(self):
        expect(self.browser_fixture.locator(LPL.ENTER_WITH_PASSWORD_BUTTON),
               'Кнопка входа с помощью пароля не отображается на странице').to_be_visible(timeout=1000)
        self.browser_fixture.locator(LPL.ENTER_WITH_PASSWORD_BUTTON).click()
