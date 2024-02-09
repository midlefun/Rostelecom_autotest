from .pages.main_page import MainPage
import pytest
import config


class TestMainPage:
    link = config.url.DOMAIN_MSC

    # @pytest.mark.skip
    def test_lk_page_is_open(self, browser_fixture):
        page = MainPage(browser_fixture, self.link)
        page.open()
        # page.check_lk_enter_button_is_visible()
        page.go_to_lk_enter_menu()
        login_page = page.press_lk_link()
        login_page.check_lk_page_is_active()


