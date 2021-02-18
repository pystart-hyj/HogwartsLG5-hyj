from appium.webdriver.common.mobileby import MobileBy
from homework_appium_framework.config.basepage import BasePage
from homework_appium_framework.page.search_page import SearchPage


class MarketPage(BasePage):
    def click_search(self):
        self.find((MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']")).click()
        return SearchPage(self.driver)