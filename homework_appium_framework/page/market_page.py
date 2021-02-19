from appium.webdriver.common.mobileby import MobileBy
from homework_appium_framework.config.basepage import BasePage
from homework_appium_framework.page.search_page import SearchPage


class MarketPage(BasePage):
    def click_search(self):
        self.run_steps("../page/market_page.yaml","click_search")
        return SearchPage(self.driver)