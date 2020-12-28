import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com/")
        # 隐式等待
        # self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        self.driver.find_element(By.XPATH,'//*[@title="原创精华文章,有100元奖金"]').click()

        # 显式等待
        def wait(x):
            return len(self.driver.find_elements(By.XPATH,'//*[@class="default"]')) >= 1

        WebDriverWait(self.driver,10).until(wait)
        self.driver.find_element(By.XPATH,'//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()