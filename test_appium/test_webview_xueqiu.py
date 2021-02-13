from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebXQ():
    def setup(self):
        des_caps = {}
        des_caps['platformName'] = 'Android'
        des_caps['platformVersion'] = '6.0'
        des_caps['deviceName'] = '127.0.0.1:7555'
        des_caps['appPackage'] = 'com.xueqiu.android'
        des_caps['appActivity'] = '.main.view.MainActivity'
        # des_caps['browserName'] = 'Browser'
        des_caps['noReset'] = 'true'
        des_caps['skipDeviceInitialization'] = 'true'
        des_caps['chromedriverExecutable'] = r"D:\new software\appiumchromedriver\chromedriver.exe"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_a(self):
        locator = (MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/tab_name' and @text='交易']")
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        print(self.driver.contexts)
        self.driver.find_element(*locator).click()

        locator1 = (MobileBy.CSS_SELECTOR,'#app > div > div > div > ul > li.trade_home_agu_3bZ > div.trade_home_info_205 > h1')
        print(self.driver.contexts)
        self.driver.switch_to.context(self.driver.contexts[-1])
        print(self.driver.window_handles)
        WebDriverWait(self.driver,30).until(expected_conditions.element_to_be_clickable(locator1))
        self.driver.find_element(*locator1).click()
        print(self.driver.window_handles)
        window_page = self.driver.window_handles[-1]
        self.driver.switch_to.window(window_page)

        phonenumber_locator =(MobileBy.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[2]/div[1]/div/div[1]/div[2]')
        WebDriverWait(self.driver,20).until(expected_conditions.visibility_of_element_located(phonenumber_locator))
        print(self.driver.contexts)
        self.driver.find_element(*phonenumber_locator).send_keys("13162921123")
        self.driver.find_element(MobileBy.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[2]').send_keys("123456")
        self.driver.find_element(MobileBy.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[2]/div[1]/div/div[5]/div[1]').click()
        sleep(5)

