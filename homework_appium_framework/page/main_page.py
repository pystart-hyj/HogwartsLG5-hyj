from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from homework_appium_framework.config.basepage import BasePage
from homework_appium_framework.page.market_page import MarketPage


class MainPage(BasePage):
    def goto_market(self):
        locator = (MobileBy.XPATH,"//*[@text='行情']")
        WebDriverWait(self.driver,15).until(expected_conditions.element_to_be_clickable(locator))
        # 点击发帖按钮，验证黑名单功能
        # self.find((By.ID, "post_status")).click()
        self.find(locator).click()
        return MarketPage(self.driver)