from appium.webdriver.common.mobileby import MobileBy
from homework_appium_framework.config.basepage import BasePage


class SearchPage(BasePage):
    def input_search(self):
        self.run_steps("../page/search_page.yaml","input_search")
        return self

    def get_list_text(self):
        ele = self.finds((MobileBy.XPATH,"//*[@class='android.widget.RelativeLayout']"))
        return len(ele)