import pytest
from pythoncode.calculator import Calculator
import yaml

def get_datas():
    with open("./test_cal.yml") as f:
        datas = yaml.safe_load(f)
        datas_add = datas["add"]
        print(f"取出用于计算加法的数据 {datas_add}")
        datas_sub = datas["sub"]
        print(f"取出用于计算减法的数据 {datas_sub}")
        datas_mul = datas["mul"]
        print(f"取出用于计算乘法的数据 {datas_mul}")
        datas_div = datas["div"]
        print(f"取出用于计算除法的数据 {datas_div}")
        return [datas_add,datas_sub,datas_mul,datas_div]

class TestCalc:
    def setup_class(self):
        # 实例化类,生成类的对象
        self.calc = Calculator()
        print("\n开始计算")

    def teardown_class(self):
        print("\n结束计算")

    #  使用参数化
    @pytest.mark.parametrize("a,b,expect",get_datas()[0],ids=("test_add","test_add","test_add"))
    # 测试add函数
    def test_add(self,a,b,expect):
        # 调用add函数,返回的结果保存在result里面
        result = self.calc.add(a,b)
        # 判断result结果是否等于期望的值
        assert result == expect

    @pytest.mark.parametrize("a,b,expect",get_datas()[1])
    def test_sub(self,a,b,expect):
        result1 = self.calc.sub(a,b)
        assert result1 == expect

    @pytest.mark.parametrize("a,b,expect",get_datas()[2])
    def test_mul(self,a,b,expect):
        result2 = self.calc.mul(a,b)
        assert result2 == expect

    @pytest.mark.parametrize("a,b,expect",get_datas()[3])
    def test_div(self,a,b,expect):
        result_div = self.calc.div(a,b)
        assert result_div == expect
