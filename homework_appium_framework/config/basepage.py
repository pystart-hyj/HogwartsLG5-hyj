import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from homework_appium_framework.config.handle_black import handle_black


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    @handle_black
    def find(self, locator):
        return self.driver.find_element(*locator)

    def finds(self,locator):
        return self.driver.find_elements(*locator)

    def send(self,locator,content):
        return self.find(locator).send_keys(content)

    def scroll_find_click(self, text):
        element = (MobileBy.ANDROID_UIAUTOMATOR,
                   'new UiScrollable(new UiSelector().'
                   'scrollable(true).instance(0)).'
                   'scrollIntoView(new UiSelector().'
                   f'text("{text}").instance(0));')
        self.find(element).click()

    def find_and_get_text(self, locator):
        return self.find(locator).text

    def run_steps(self, page_path, operation):
        with open(page_path,'r',encoding="UTF-8") as f:
            data = yaml.safe_load(f)
        # 支持 PO 下多个操作
        steps = data[operation]
        for step in steps:
            action = step['action']
            if action == "find":
                self.find(step["locator"]).click()
            elif action == "send":
                self.send(step["locator"],step["content"])