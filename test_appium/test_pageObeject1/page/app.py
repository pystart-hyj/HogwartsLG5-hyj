import yaml
from appium import webdriver
from test_appium.test_pageObeject1.page.base_page import BasePage
from test_appium.test_pageObeject1.page.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".main.view.MainActivity"

    def start(self):
        if self._driver is None:
            caps = {}
            caps['platformName'] = 'Android'
            caps['deviceName'] = '127.0.0.1:7555'
            caps['appPackage'] = self._package
            caps['appActivity'] = self._activity
            caps['noReset'] = True
            caps['skipDeviceInitialization'] = 'true'
            caps['udid'] = yaml.safe_load(open("../page/configurations.yaml"))['caps']['udid']
            # 初始化driver
            self._driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        else:
            self._driver.start_activity(self._package,self._activity)
        self._driver.implicitly_wait(15)
        return self

    def mian(self) -> Main:
        return Main(self._driver)
