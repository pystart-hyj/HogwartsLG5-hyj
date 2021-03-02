import requests


class Base:
    def __init__(self):
        ID = "ww81243aaf97bb4052"
        SECRET = "vr57j6uYIbeiQiXW850y6sV_Md0Er9zbTutZIjJGmlg"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={ID}&corpsecret={SECRET}"
        r = requests.get(url)
        self.token = r.json()["access_token"]
        # 声明一个session
        self.session = requests.Session()
        # 把token放入到session中
        self.session.params = {"access_token": self.token}

    def send(self, *args, **kwargs):
        r = self.session.request(*args, **kwargs)
        return r.json()
