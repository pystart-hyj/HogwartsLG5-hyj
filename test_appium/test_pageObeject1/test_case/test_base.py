from test_appium.test_pageObeject1.page.app import App


class TestBase:
    app = None
    def setup(self):
        self.app = App()
