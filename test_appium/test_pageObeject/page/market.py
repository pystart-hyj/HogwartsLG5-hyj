from test_appium.test_pageObeject.page.base_page import BasePage
from test_appium.test_pageObeject.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.steps("../page/market.yaml")
        return Search(self._driver)