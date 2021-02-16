from time import sleep

from selenium.webdriver.common.by import By
from test_appium.test_pageObeject1.page.base_page import BasePage


class Main(BasePage):
    def goto_search(self):
        # By.ID = "id"
        # self.find("id", "home_search").click()
        self.steps("../page/main.yaml")

    def goto_windows(self):
        self.find(By.ID, "post_status").click()
        sleep(5)
        self.find("id", "home_search").click()