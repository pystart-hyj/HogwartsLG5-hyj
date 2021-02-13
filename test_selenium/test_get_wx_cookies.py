import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestGetCookie:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_get_cookie(self):
        self.driver.find_element(By.CSS_SELECTOR,".index_top_operation_loginBtn").click()
        # 等待15s 人工扫码登录
        sleep(15)
        cookies = self.driver.get_cookies()
        print(cookies)
        with open("cookie.json","w") as f:
            json.dump(cookies,f)
