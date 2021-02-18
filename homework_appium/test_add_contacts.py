from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestAddContacts:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['settings[waitForIdleTimeout]'] = 1
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_add_contacts(self):
        name = "张一"
        gender = "女"
        phonenum = "19000000001"
        locator = (MobileBy.XPATH,"//*[@text='通讯录']")
        WebDriverWait(self.driver,60).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成员']").click()
        # 通讯录人员多的时候，需要滑动查找添加成员按钮
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector()'
                                                        '.scrollable(true).instance(0))'
                                                        '.scrollIntoView(new UiSelector().text("添加成员").'
                                                        'instance(0))').click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/ern']/android.widget."
                                                "RelativeLayout/android.widget.EditText").send_keys(name)
        if gender == "女":
            self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/d9j']/android.widget."
                                                    "RelativeLayout").click()
            self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/boh']/android.widget."
                                                    "RelativeLayout[2]").click()
        else:
            self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/d9j']/android.widget."
                                                    "RelativeLayout").click()
            self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/boh']/android.widget."
                                                    "RelativeLayout[1]").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='手机号']").send_keys(phonenum)
        self.driver.find_element(MobileBy.XPATH,"//*[@text='设置部门']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'确定')]").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='保存']").click()
        # 定位页面有安卓的Toast弹框
        ele = self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.Toast']").text
        assert ele == "添加成功"
        sleep(5)

