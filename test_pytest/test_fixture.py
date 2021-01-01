import pytest
# fixture 是 pytest 的一个外壳函数，可以模拟setup和teardown的操作
# yield 之前的操作相当于 setup，yield 之后的操作相当于teardown
# yield 相当于 return，如果需要返回数据的话，直接放在 yield 后面

# 创建一个登录的fixture方法
@pytest.fixture()
def login():
    print("\n登录操作")
    print("获取token")
    username = "tom"
    passworg = "123456"
    token = "token123456"
    yield [username,passworg,token]
    print("\n登出操作")

# 需要登录
def test_case1():
    # print(f"\npassword: {login[1]}")
    # print(f"\nlogin username and password: {login}")
    print("测试用例1")

def test_case2(connectDB):
    print("测试用例2")

# 需要登录
def test_case3():
    print("测试用例3")

# @pytest.mark.usefixtures("login")
def test_case4():
    print("测试用例4")