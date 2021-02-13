from time import sleep
import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import *

class TestWebDriverWait():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        # desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['resetKeyboard'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize('searchkey,type,price',[
        ('alibaba','BABA',240),
        ('xiaomi','01810',28)
    ])
    def test_search(self,searchkey,type,price):
        locator = (By.ID,"com.xueqiu.android:id/tv_search")
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        self.driver.find_element_by_id("com.xueqiu.android:id/name").click()
        locator = (By.XPATH,f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        current_price = float(self.driver.find_element(*locator).text)
        expect_price = price
        assert_that(current_price,close_to(expect_price,expect_price*0.1))