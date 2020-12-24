# f = open('data.txt')
# print(f.readable())
# print(f.readlines())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.read())
# f.close()

# with语句块，可以将文件打开以后，操作完毕，自动关闭这个文件
# 图片读取需要使用rb  读取二进制的格式
# 正常的文本，可以使用rt，也就是默认格式即可
with open("data.txt", 'rt') as f:
    # print(f.readlines())
    while True:
        line = f.readline()
        if line:
            print(line)
        else:
            break
    # print(f.read())




