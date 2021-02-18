from homework_appium.page.basepage import BasePage
from homework_appium.page.memberinvit_page import MemberInvitePage


class AddressListPage(BasePage):
    def add_member(self):
        self.scroll_find_click("添加成员")
        return MemberInvitePage(self.driver)