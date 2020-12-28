import pytest
from selenium import webdriver
import time

# @pytest.mark.flaky(reruns=3,reruns_delay=2)
class TestHogwards():
    def setup(self):
        self.driver = webdriver.Chrome()
        # 浏览器最大化
        self.driver.maximize_window()
        # 隐示等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_hogwards(self):
        self.driver.get("https://testerhome.com/")
        self.driver.find_element_by_link_text("跳过").click()
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_link_text("求职面试圈").click()
        self.driver.find_element_by_css_selector(".topic-26766 .title > a").click()




