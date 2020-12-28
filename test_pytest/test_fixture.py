import pytest


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
def test_case1(login):
    print(f"password: {login[0]}")
    print(f"password: {login}")
    print("测试用例1")

def test_case2(connectDB):
    print("测试用例2")

# 需要登录
def test_case3(login):
    print("测试用例3")

@pytest.mark.usefixtures("login")
def test_case4():
    print("测试用例4")