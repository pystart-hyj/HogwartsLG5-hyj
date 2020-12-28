#coding=utf-8
from time import sleep
from test_selenium.base import Base


class TestFile(Base):

    def test_file_upload(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_css_selector("#form > span.bg.s_ipt_wr.quickdelete-wrap > span.soutu-btn").click()
        sleep(3)
        self.driver.find_element_by_css_selector("#form > div > div.soutu-state-normal > div.upload-wrap > input").send_keys("D:/PycharmProjects/HogwartsLG5/selenium_file_alert/1.jpg")
        sleep(3)
