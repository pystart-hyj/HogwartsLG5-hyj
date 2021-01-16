from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from homework_selenium.test_weixin_practice2.page.add_department import AddDepartment
from homework_selenium.test_weixin_practice2.page.base_page import BasePage


class MyMain(BasePage):
    def goto_address_list(self):
        self.find(By.ID,"menu_contacts").click()
        # 显示等待 通讯录页面-添加按钮展示
        WebDriverWait(self.driver,5).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="js_contacts54"]/div/div[2]/div/div[2]/div[3]/table/thead/tr/th[2]')))
        self.find(By.CSS_SELECTOR,".member_colLeft_top_addBtn").click()
        self.find(By.CSS_SELECTOR,".js_create_party").click()
        return AddDepartment(self.driver)