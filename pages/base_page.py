from playwright.sync_api import expect
import config

class BasePage:
    def __init__(self, browser_fixture, url):
        self.browser_fixture = browser_fixture
        self.url = url

    def open(self):
        return self.browser_fixture.goto(self.url)

    def find_element(self, locator, timeout):
        expect(self.browser_fixture.locator(locator),
               f'На странице отсутствует элемент с локатором {locator}').to_be_visible(
            timeout=timeout)
        return self.browser_fixture.locator(locator)

        # TODO Создать методы find element и find elements

    def pause(self):
        self.browser_fixture.pause()
