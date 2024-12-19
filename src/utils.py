import time

# 定义一个函数，用于获取当前时间
def getCurrentTime():
    # 获取当前时间的时间戳
    t = time.time()
    # 将时间戳转换为毫秒
    return int(t * 1000)

