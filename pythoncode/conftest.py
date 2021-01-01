import pytest
import yaml
from pythoncode.calculator import Calculator
import os

@pytest.fixture(scope="module")
def get_calc():
    print("开始计算\n")
    calc = Calculator()
    yield calc
    print("\n计算结束")

# os.path.dirname(__file__)  取当前路径
yaml_file_path = os.path.dirname(__file__) + "/test_cal.yml"
with open(yaml_file_path,'rb') as f:
    datas = yaml.safe_load(f)
    datas_add = datas["add"]
    # print(f"取出用于计算加法的数据 {datas_add}")
    datas_sub = datas["sub"]
    # print(f"取出用于计算减法的数据 {datas_sub}")
    datas_mul = datas["mul"]
    # print(f"取出用于计算乘法的数据 {datas_mul}")
    datas_div = datas["div"]
    # print(f"取出用于计算除法的数据 {datas_div}")

# @pytest.fixture(params=[datas_add,datas_sub,datas_mul,datas_div])
@pytest.fixture(params=datas_add)
def get_datas_add(request):
    data = request.param
    print(f"request.param的测试数据是{data}")
    yield data

@pytest.fixture(params=datas_sub)
def get_datas_sub(request):
    data = request.param
    print(f"request.param的测试数据是{data}")
    yield data

@pytest.fixture(params=datas_mul)
def get_datas_mul(request):
    data = request.param
    print(f"request.param的测试数据是{data}")
    yield data

@pytest.fixture(params=datas_div)
def get_datas_div(request):
    data = request.param
    print(f"request.param的测试数据是{data}")
    yield data
