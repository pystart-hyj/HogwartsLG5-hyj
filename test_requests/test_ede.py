import json
import requests
import base64

def test_encode():
    url= "http://127.0.0.1:9999/demo.txt"
    r = requests.get(url=url)
    print(r.text)
    # r.content 获取二进制的响应结果
    print(r.content)
    res = base64.b64decode(r.content)
    print(res)
    res1 = json.loads(base64.b64decode(r.content))
    print(res1)