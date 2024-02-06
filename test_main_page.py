import time
from .pages.main_page import MainPage
import pytest



def test_guest_can_go_to_login_page(browser_fixture):
    link = "https://msk.rt.ru/"
    page = MainPage(browser_fixture, link)
    page.open()
    page.go_to_login_page()


# def test_guest_could_click_to_login_link(browser_fixture) -> None:
#     guest_can_go_to_login_page(browser_fixture)


# class TestMainPage():
#
#
#     @pytest.mark.skip
#     @pytest.mark.smoke
#     def test_add_todo(self, browser_fixture) -> None:
#         browser_fixture.goto(link)
#         browser_fixture.wait_for_selector('#lk-enter').click()

