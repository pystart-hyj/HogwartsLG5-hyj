import requests
from jsonpath import jsonpath
from hamcrest import *

class TestDemo:
    def test_demo(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r.text)
        print(r.json())
        print(r.status_code)
        assert r.status_code == 200

    def test_query(self):
        payload = {
            "a": 1,
            "name": "xingming"
        }
        r = requests.get('https://httpbin.testing-studio.com/get',params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            "key1": "value1",
            "key2": "value2"
        }
        r = requests.post('https://httpbin.testing-studio.com/post', data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_header(self):
        r = requests.get('https://httpbin.testing-studio.com/get',headers={"h":"headers demo"})
        print(r.text)
        print(r.json())
        print(r.status_code)
        print(r.headers)
        assert r.status_code == 200
        assert r.json()["headers"]["H"] == "headers demo"

    def test_post_json(self):
        payload = {
            "key1": "value1",
            "key2": "value2"
        }
        r = requests.post('https://httpbin.testing-studio.com/post', json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()["json"]["key1"] == "value1"

    def test_hogwarts_json(self):
        r = requests.get('https://ceshiren.com/categories.json')
        print(r.text)
        print(r.json())
        assert r.status_code == 200
        assert r.json()["category_list"]["categories"][9]["name"] == "霍格沃兹测试学院教务处"
        print(jsonpath(r.json(), "$..name"))
        assert jsonpath(r.json(),"$..name")[9] == "霍格沃兹测试学院教务处"

    def test_hamcrest(self):
        r = requests.get('https://ceshiren.com/categories.json')
        assert r.status_code == 200
        assert_that(r.json()["category_list"]["categories"][9]["name"],equal_to("霍格沃兹测试学院教务处"))
