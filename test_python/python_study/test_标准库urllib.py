import urllib.request

response = urllib.request.urlopen('http://www.baidu.com')
print(response.status)
# print(response.read())  # 响应数据
print(response.headers)   #返回头部信息
# 这个标准版作为了解即可，升级的request第三方包后面会讲，更好用
