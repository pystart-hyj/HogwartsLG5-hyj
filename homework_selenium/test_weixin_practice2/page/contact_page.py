from time import sleep
from selenium.webdriver.common.by import By
from homework_selenium.test_weixin_practice2.page.base_page import BasePage


class ContactPage(BasePage):

        def get_department_list(self):
            self.driver.refresh()
            sleep(5)
            elements = self.driver.find_elements(By.XPATH, '//*[@class="jstree-anchor"]')
            department_list = []
            for element in elements:
                department_list.append(element.text)
            return department_list

