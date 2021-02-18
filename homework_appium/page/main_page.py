from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from homework_appium.page.addresslist_page import AddressListPage
from homework_appium.page.basepage import BasePage


class MainPage(BasePage):
    def click_addresslist(self):
        locator = (MobileBy.XPATH,"//*[@text='通讯录']")
        WebDriverWait(self.driver,60).until(expected_conditions.element_to_be_clickable(locator))
        self.find_and_click(locator)
        return AddressListPage(self.driver)