from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright

link = "https://msk.rt.ru/"

def test_guest_should_see_login_link(page_fix):
    page_fix.goto(link)
    page_fix.locator('#lk-enter')
    page_fix.pause()