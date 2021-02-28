import requests

def test_demo():
    # 获取token
    ID = "ww81243aaf97bb4052"
    SECRET = "vr57j6uYIbeiQiXW850y6sV_Md0Er9zbTutZIjJGmlg"
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={ID}&corpsecret={SECRET}"
    r = requests.get(url)
    token = r.json()["access_token"]

    # 读取成员
    USERID = "13145212"
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid={USERID}"
    r = requests.get(url)
    # print(r.json())

    # 更新成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}"
    body = {
        "userid": "13145212",
        "name": "修改后姓名"
    }
    r = requests.post(url,json=body)
    # print(r.json())

    # 创建成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
    body = {
        "userid": "userid02",
        "name": "huang2",
        "mobile": "+86 13900000005",
        "department": [1]
    }
    r = requests.post(url, json=body)
    # print(r.json())

    # 删除成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=userid01"
    r = requests.get(url)
    print(r.json())