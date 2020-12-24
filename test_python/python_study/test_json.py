# from json import *
import json

# json 有字典和列表组成的
data = {
    "name": ["jerry", "nickname"],
    "age": 26,
    "gander": "famale"
}
print(type(data))
# 字典转字符串
data1 = json.dumps(data)
print(data1)
print(type(data1))

# 字符串转字典
data2 = json.loads(data1)
print(data2)
print(type(data2))