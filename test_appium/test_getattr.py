from time import sleep
import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import *

class TestGetAttr():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['dontStopAppOnReset'] = 'true'
        # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # self.driver.implicitly_wait(10)

    def teardown(self):
        # self.driver.back()
        # self.driver.back()
        self.driver.quit()

    @pytest.mark.skip
    def test_getattr(self):
        search_ele = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(search_ele.get_attribute("content-desc"))
        print(search_ele.get_attribute("resource-id"))
        print(search_ele.get_attribute("enabled"))
        print(search_ele.get_attribute("checkable"))
        print(search_ele.get_attribute("bounds"))

    def test_hamcrest(self):
        # assert_that(10,equal_to(9),"断言失败")
        assert_that(8,close_to(10,2))