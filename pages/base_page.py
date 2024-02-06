class BasePage():
    def __init__(self, browser_fixture, url):
        self.browser_fixture = browser_fixture
        self.url = url

    def open(self):
        self.browser_fixture.goto(self.url)

    def pause(self):
        self.browser_fixture.pause()