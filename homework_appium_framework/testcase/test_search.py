import pytest
import yaml

from homework_appium_framework.config.app import App


class TestSearch:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardowd(self):
        self.app.stop()

    # with open("../data/search.yaml", encoding="UTF-8") as f:
    #     search_datas = yaml.safe_load(f)

    def test_search(self):
        result = self.main.goto_market().click_search().input_search().get_list_text()
        assert result > 0
