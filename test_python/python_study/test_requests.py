import requests
# 可找requests官方文档学习 https://requests.readthedocs.io/zh_CN/latest/user/quickstart.html
# r = requests.get("http://www.baidi.com")
# print(r)


r = requests.post("http://httpbin.org/post", data={'key': 'value'})
print(r)

