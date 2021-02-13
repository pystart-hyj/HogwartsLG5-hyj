from test_appium.test_pageObeject.page.base_page import BasePage
from test_appium.test_pageObeject.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.steps("../page/main.yaml")
        return Market(self._driver)