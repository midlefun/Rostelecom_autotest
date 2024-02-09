import pytest
from playwright.sync_api import  BrowserContext, Page, sync_playwright
import config


@pytest.fixture(scope="class")
def browser_fixture() -> Page:
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    # browser = playwright.chromium.launch(headless=True)
    context = get_context(browser)
    page = context.new_page()
    yield page
    page.close()
    browser.close()
    playwright.stop()


def get_context(browser) -> BrowserContext:
    context = browser.new_context(
        viewport=config.Playwright.PAGE_VIEWPORT_SIZE,
        locale=config.Playwright.LOCALE
    )
    context.set_default_timeout(
        timeout=config.expectations.DEFAULT_TIMEOUT
    )
    return context

#TODO УБрать ?
@pytest.mark.parametrize('town, anchor', [("msk", " "), ("krasnodar", "/#4in1")])
def test_guest_should_see_login_link(self, browser_fixture, town, anchor) -> None:
    link = f"https://{town}.rt.ru{anchor}"
    browser_fixture.goto(link)
    browser_fixture.wait_for_selector('#lk-enter')
