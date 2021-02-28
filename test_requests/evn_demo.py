import requests
import yaml


class TestApi:
    data = {
        "method": "get",
        "url": "http://testing-studio:9999/demo.txt",
        "headers": None,
    }

    # env = {
    #     "default": "dev",
    #     "config":
    #     {
    #     "dev": "127.0.0.1",
    #     "test": "test.test.com"
    #     }
    # }
    # 下面两个写法一样
    # env = yaml.safe_load(open("../test_requests/env.yaml"))
    with open("../test_requests/env.yaml") as f:
        env = yaml.safe_load(f)

    def send(self, data:dict):
        # 替换子字符串
        data["url"] = str(data["url"]).replace("testing-studio",self.env["config"][self.env["default"]])
        r = requests.request(method=data["method"], url=data["url"], headers=data["headers"])
        return r

    def test_send(self):
        res = self.send(self.data)
        print(res.text)
        print(self.data)
        assert res.status_code == 200