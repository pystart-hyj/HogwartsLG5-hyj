import pytest
import yaml
from test_appium.test_pageObeject1.page.app import App
from test_appium.test_pageObeject1.test_case.test_base import TestBase


class TestMain(TestBase):
    @pytest.mark.parametrize("value1, value2", yaml.safe_load(open("./test_main.yaml")))
    def test_mian(self, value1, value2):
        self.app.start().mian().goto_search()
        print(value1)
        print(value2)
        print(yaml.safe_load(open("../page/configurations.yaml"))['caps']['udid'])

    def test_windows(self):
        self.app.start().mian().goto_windows()
