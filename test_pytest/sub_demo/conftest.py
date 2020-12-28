import pytest

@pytest.fixture()
def connectDB():
    print("这是 sub_demo下的connectDB")
    yield
    print("这是 sub_demo下的connectDB")


