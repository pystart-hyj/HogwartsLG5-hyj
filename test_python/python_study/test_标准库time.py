import time

# print(time.asctime())
# print(time.time())
# print(time.localtime())
# print(time.strftime("%Y年%m月%d日 %H:%M:%S", time.localtime()))

# 获取两天前现在的时间
now_timestamp = time.time()
two_day_before= now_timestamp - 60*60*24*2
time_tuple = time.localtime(two_day_before)

print(time.strftime("%Y年%m月%d日 %H:%M:%S", time_tuple))

# 获取两天后现在的时间
now_timestamp = time.time()
two_day_before= now_timestamp + 60*60*24*2
time_tuple = time.localtime(two_day_before)

print(time.strftime("%Y年%m月%d日 %H:%M:%S", time_tuple))