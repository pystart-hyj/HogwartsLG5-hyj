from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Selenium():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_selenium(self):
        self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.XPATH, '//*[@id="su"]').click()