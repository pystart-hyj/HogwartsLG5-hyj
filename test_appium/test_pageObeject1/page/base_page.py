import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    _driver: WebDriver
    # 异常弹框的黑名单，下面的登录页面的关闭按钮定位元素
    _black_list = [(By.ID, "iv_close")]
    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value):
        try:
            element = self._driver.find_element(locator, value)
            return element
        except:
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    break
            return self.find(locator, value)

    def steps(self, path):
        with open(path, encoding="utf-8") as f:
            steps = yaml.safe_load(f)
        element = None
        for step in steps:
            if "by" in step.keys():
                element = self.find(step["by"], step["locator"])
            if "action" in step.keys():
                action = step["action"]
                if action == "click":
                    element.click()