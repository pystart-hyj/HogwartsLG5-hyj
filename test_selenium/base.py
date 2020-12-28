import os
from selenium import webdriver

class Base():
    def setup(self):
        # 使用不同浏览器进行自动化测试，根据传入的值browser判断，使用什么浏览器
        # browser = os.getenv("browser")
        # if browser == "firefox":
        #     self.driver = webdriver.Firefox()
        # elif browser == "headless":
        #     self.driver = webdriver.PhantomJS()
        # else:
        #     self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()