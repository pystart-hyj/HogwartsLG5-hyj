from selenium.webdriver.common.by import By
from homework_selenium.test_weixin_practice2.page.base_page import BasePage
from homework_selenium.test_weixin_practice2.page.contact_page import ContactPage


class AddDepartment(BasePage):
    def add_department(self):
        self.find(By.NAME,"name").send_keys("部门02")
        self.find(By.CSS_SELECTOR,".js_parent_party_name").click()
        self.find(By.CSS_SELECTOR,".qui_dialog_body [id='1688853566111920_anchor']").click()
        self.find(By.XPATH,'//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]').click()
        return ContactPage(self.driver)