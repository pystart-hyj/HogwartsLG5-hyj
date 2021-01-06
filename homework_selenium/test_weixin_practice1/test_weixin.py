import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestWinXin():
    def setup(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver = webdriver.Chrome()
        # self.driver.get("https://work.weixin.qq.com/")
        # self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_cookie(self):
        # cookies = self.driver.get_cookies()
        # print(cookies)
        # with open("cookie.json","w") as f:
        #     json.dump(cookies, f)

        self.driver.get("https://work.weixin.qq.com/")

        with open("cookie.json","r") as f:
            cookies = json.load(f)

        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="menu_customer"]').click()
        sleep(2)

    def test_weixin(self):
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element(By.XPATH, '//*[@class="index_top_operation_loginBtn"]').click()
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="menu_customer"]').click()
        sleep(2)


