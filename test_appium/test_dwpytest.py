from time import sleep
import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestDW():
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
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        # self.driver.back()
        # self.driver.back()
        self.driver.quit()

    def test_search(self):
        print("这是一个测试用例")
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        sleep(3)
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        sleep(10)
        reult = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        assert reult > 243

    def test_attr(self):
        element = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        element_enabled = element.is_enabled()
        print(element.text)
        print(element.location)
        print(element.size)
        if element_enabled == True:
            element.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            alibaba_element = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            # alibaba_element.is_displayed()
            element_displayed = alibaba_element.get_attribute("displayed")
            if element_displayed == "true":
                print("搜索成功")
            else:
                print("搜索失败")

    def test_touchaction(self):
        sleep(5)
        window_rect = self.driver.get_window_rect()
        width = window_rect["width"]
        height = window_rect["height"]
        x1 = int(width/2)
        y_start = int(height * 4/5)
        y_end = int(height * 1/5)
        action = TouchAction(self.driver)
        action.press(x=x1,y=y_start).wait(200).move_to(x=x1,y=y_end).release().perform()
        sleep(2)

    def test_get_current(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = self.driver.find_element_by_xpath("//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        print(f"当前09988股票的价格：{current_price}")
        assert float(current_price) > 200

    def test_scroll_find_element(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("关注")').click()
        # 滚动查找元素
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector()'
                                                        '.scrollable(true).instance(0))'
                                                        '.scrollIntoView(new UiSelector().text("花甲老头").'
                                                        'instance(0))').click()
        sleep(5)

if __name__ == '__main__':
    pytest.main()
