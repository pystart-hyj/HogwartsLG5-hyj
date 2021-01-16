import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWinXin():
    def setup(self):
        # 复用chrome调试窗口
        chrome_options = webdriver.ChromeOptions()
        chrome_options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver = webdriver.Chrome()
        # self.driver.get("https://work.weixin.qq.com/")
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(3)
        # sleep(30)

    def teardown(self):
        self.driver.quit()

    def test_cookie(self):
        # #获取  cookie
        # cookies = self.driver.get_cookies()
        # print(cookies)
        # #以文件流的形式打开文件
        # with open("cookie.json","w") as f:
        #     # 存储 cookie 到 cookie.json
        #     json.dump(cookies, f)

        self.driver.get("https://work.weixin.qq.com/")
        # 以文件流的形式打开文件
        with open("../../test_weixin_practice2/page/cookie.json", "r") as f:
            # 读取 cookies
            cookies = json.load(f)
        # 注入 cookies
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


