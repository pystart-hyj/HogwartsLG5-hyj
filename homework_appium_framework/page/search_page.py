from appium.webdriver.common.mobileby import MobileBy
from homework_appium_framework.config.basepage import BasePage


class SearchPage(BasePage):
    def input_search(self, text):
        self.find((MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']")).send_keys(text)
        return self

    def get_list_text(self):
        ele = self.finds((MobileBy.XPATH,"//*[@class='android.widget.RelativeLayout']"))
        return len(ele)