import time

import pytest

link = "https://msk.rt.ru/"


class TestMainPage():
    @pytest.mark.skip
    @pytest.mark.smoke
    def test_add_todo(self, browser_fixture) -> None:
        browser_fixture.goto(link)
        browser_fixture.wait_for_selector('#lk-enter').click()

    def go_to_login_page(self, browser_fixture):
        login_link = browser_fixture.wait_for_selector('#lk-enter')
        login_link.click()

    def test_guest_could_click_to_login_link(self, browser_fixture) -> None:
        browser_fixture.goto(link)
        self.go_to_login_page(browser_fixture)
