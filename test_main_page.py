from .pages.main_page import MainPage
import pytest


class TestMainPage:
    # TODO Вынести линки в отдельный файл

    link = "https://msk.rt.ru/"

    @pytest.mark.skip
    def test_lk_page_is_open(self, browser_fixture):
        page = MainPage(browser_fixture, self.link)
        page.open()
        page.check_lk_enter_button_is_visible()
        page.go_to_lk_enter_menu()
        # TODO Можно ли обращаться таким образом
        page.press_lk_link().check_lk_page_is_active()
