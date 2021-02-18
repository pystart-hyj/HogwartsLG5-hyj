from appium.webdriver.common.mobileby import MobileBy
from homework_appium.page.basepage import BasePage
from homework_appium.page.contactedit_page import ContactEditPage


class MemberInvitePage(BasePage):
    def addconect_menual(self):
        self.find_and_click((MobileBy.XPATH, '//*[@text="手动输入添加"]'))
        return ContactEditPage(self.driver)

    def get_toast(self):
        ele = self.find_and_get_text((MobileBy.XPATH, '//*[@class="android.widget.Toast"]'))
        return ele