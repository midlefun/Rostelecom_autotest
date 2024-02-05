import pytest, os
from playwright.sync_api import Playwright, Browser, BrowserContext, Page, sync_playwright


class Playwright:
    PAGE_VIEWPORT_SIZE = {'width': 1920, 'height': 1080}
    ENV = os.getenv('ENV') if os.getenv('ENV') is not None else 'stage'
    BROWSER = os.getenv('BROWSER') if os.getenv(
        'BROWSER') is not None else 'chrome'  # Она отвечает за то, в каком браузере будут выполняться автотесты. По умолчанию там указан Google Chrome.
    IS_HEADLESS = os.getenv('HEADLESS') if os.getenv('HEADLESS') is not None else False
    SLOW_MO = int(os.getenv('SLOW_MO')) if os.getenv('SLOW_MO') is not None else 50
    LOCALE = 'en-US'
    DEFAULT_TIMEOUT = '2'


@pytest.fixture(scope="class")
def browser_fixture() -> Page:
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = get_context(browser)
    page = context.new_page()
    # page.goto(link)
    yield page
    page.close()
    browser.close()
    playwright.stop()


def get_context(browser) -> BrowserContext:
    context = browser.new_context(
        viewport=Playwright.PAGE_VIEWPORT_SIZE,
        locale=Playwright.LOCALE
    )
    context.set_default_timeout(
        timeout=Playwright.DEFAULT_TIMEOUT
    )
    return context


@pytest.mark.parametrize('town, anchor', [("msk", " "), ("krasnodar", "/#4in1")])
def test_guest_should_see_login_link(self, browser_fixture, town, anchor) -> None:
    link = f"https://{town}.rt.ru{anchor}"
    browser_fixture.goto(link)
    browser_fixture.wait_for_selector('#lk-enter')
