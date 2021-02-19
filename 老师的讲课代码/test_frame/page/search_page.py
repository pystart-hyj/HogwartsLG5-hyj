from 老师的讲课代码.test_frame.basepage import BasePage


class SearchPage(BasePage):
    def search(self):
        self.run_steps("../page/search_page.yaml", "search")
        # self.send((By.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']"), "alibaba")
        # self.find_and_click((By.XPATH, "//*[@text='阿里巴巴-SW']"))
        return True
