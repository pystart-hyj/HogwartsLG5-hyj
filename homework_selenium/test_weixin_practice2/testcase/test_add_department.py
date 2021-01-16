from homework_selenium.test_weixin_practice2.page.main import MyMain


class TestAddDepartment():
    def setup_class(self):
        self.main = MyMain()

    def test_add_department_success(self):
        result = self.main.goto_address_list().add_department().get_department_list()
        assert '部门02' in result
