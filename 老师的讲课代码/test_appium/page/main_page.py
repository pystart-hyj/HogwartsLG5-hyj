"""
__author__ = 'jaxon'
__time__ = '2021/1/16 下午8:38'
__desc__ = ''
"""
# 点击通讯录
from appium.webdriver.common.mobileby import MobileBy

from test_appium.page.addresslist_page import AddressListPage
from test_appium.page.basepage import BasePage


class MainPage(BasePage):

    # def __init__(self, driver):
    #     self.driver = driver
    def click_addresslist(self):
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()

        self.find_and_click((MobileBy.XPATH, '//*[@text="通讯录"]'))
        return AddressListPage(self.driver)
