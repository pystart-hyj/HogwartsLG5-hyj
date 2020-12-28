from time import sleep
import pytest
from test_selenium.base import Base


class  TestJS(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        element = self.driver.execute_script('return document.getElementById("su")')
        element.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        # Xpath属性定位
        # self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
        # css属性定位
        self.driver.find_element_by_css_selector("#page > div > a.n").click()
        sleep(3)
        # for code in [
        #     'return document.title','return JSON.stringify(performance.timing)'
        # ]:
        #     print("\n" + self.driver.execute_script(code))
        print("\n" + self.driver.execute_script("return document.title;return JSON.stringify(performance.timing)"))

    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        # time_element = self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        # self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        # print(self.driver.execute_script("return document.getElementById('train_date').value"))

        self.driver.execute_script("a=document.getElementById('train_date')")
        self.driver.execute_script("a.removeAttribute('readonly')")
        # self.driver.execute_script("a.value='2020-12-30'")
        self.driver.execute_script("a.setAttribute('value','2020-12-30')")
        print(self.driver.execute_script("return a.value"))








