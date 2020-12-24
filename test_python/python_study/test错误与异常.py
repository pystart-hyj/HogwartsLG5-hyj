import datetime

try:
    num1 = int(input("输入一个除数"))
    num2 = int(input("输入一个被除数"))
    print(num1 / num2)
# 针对报错类型，打印信息
# except ZeroDivisionError:
#     print(str(datetime.datetime.now()) + "  " + "程序出现异常:被除数不能为0")
# except ValueError:
#     print(str(datetime.datetime.now()) + "  " + "程序出现异常:输入的需要是数值型整数")
# 所有报错都打印
except:
    print(str(datetime.datetime.now()) + "  " + "程序出现异常:这是一个通用性异常")
# 没有报错打印
# else:
#     print("程序没有异常")
# 有异常、无异常 都打印
finally:
    print("无论有没有发生异常，都执行finally语句块程序 ")

# x = 10
# if x > 5:
#     raise Exception("这是抛出的异常信息")
#自定义异常抛出
class MyException(Exception):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2


raise MyException("value1", "value2")