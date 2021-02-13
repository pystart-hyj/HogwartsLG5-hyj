from time import sleep

import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    # _black_list 定义黑名单元素列表,升级弹框元素
    _black_list = [(By.ID,"image_cancel")]
    # _error_cont、_error_max 用于处理死循环，加入异常不在黑名单内，代码会死循环
    _error_cont = 0
    _error_max = 10
    _params = {}
    def __init__(self, driver: WebDriver=None):
        self._driver = driver

    # find((BY.ID,"name"))
    def find(self, by, locator=None):
        # 捕获异常黑名单处理
        try:
            element = self._driver.find_element(*by) if isinstance(by, tuple) else self._driver.find_element(by, locator)
            self._error_cont = 0
            return element
        except Exception as e:
            self._error_cont += 1
            if self._error_cont >= self._error_max:
                raise
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.find(by, locator)
            raise e

    # 解决弹出版本升级弹框的时候，页面元素能够找到，但是不能操作的问题
    def sed(self, value, by, locator=None):
        try:
            self.find(by, locator).send_keys(value)
            self._error_cont = 0
        except Exception as e:
            self._error_cont += 1
            if self._error_cont >= self._error_max:
                raise
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.sed(value, by, locator)
            raise e

    def steps(self, path):
        with open(path, encoding="utf-8") as f:
            # 定义steps 是list类型，里面有很多字典
            steps: list[dict] = yaml.safe_load(f)
            print(steps)
            for step in steps:
                if "by" in step.keys():
                    element = self.find(step["by"],step["locator"])
                if "action" in step.keys():
                    if "click" == step["action"]:
                        sleep(3)
                        element.click()
                    if "send" == step["action"]:
                        # {value}
                        content: str = step["value"]
                        for param in self._params:
                            content = content.replace("{%s}"%param, self._params[param])
                        sleep(3)
                        self.sed(content, step["by"],step["locator"])

