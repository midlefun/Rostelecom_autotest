import pytest

link = "https://msk.rt.ru/"


class TestMainPage():
    @pytest.mark.skip
    @pytest.mark.smoke
    def test_add_todo(self, browser_fixture) -> None:
        browser_fixture.goto(link)
        browser_fixture.wait_for_selector('#lk-enter').click()

    def test_add_to(self, browser_fixture) -> None:
        browser_fixture.goto(link)
        browser_fixture.wait_for_selector('#block-b2cpanellichnykhkabinetoviligeo').click()
        # browser_fixture.pause()
