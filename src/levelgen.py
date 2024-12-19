back = [
    "99999999999999999999\n",
    "90000000000000000009\n",
    "90000000000000000009\n",
    "90000000000000000009\n",
    "90000000000000000009\n",
    "90000000000000000009\n",
    "90000000000000000009\n",
    "90000000000000000009\n",
    "90000000000000000009\n",
    "90000000000000000009\n",
    "90000000000000000009\n",
    "90000000000000000009\n",
    "90000000000000000009\n",
    "90000000000000000009\n",
    "90000000000000000009\n",
    "90000000000000000009\n"
]

class BlockType:
    # 定义一个空块
    NULL = 0
    # 定义一个加速块
    SPEED_UP = 1
    # 定义一个普通块
    NORMAL = 2
    # 定义一个复制块
    COPY = 3
    # 定义一个减速块
    SPEED_DOWN = 6
    # 定义一个墙块
    WALL = 9

BLOCK_TYPE_VALUE = [
    1500,    
    10,
    100,
    10,
    100,
    100,
    10,
    100,
    0,
    0,
]

# 定义一个变量maxValue，初始值为0
maxValue = 0
# 遍历BLOCK_TYPE_VALUE中的每个元素
for x in BLOCK_TYPE_VALUE:
    # 将每个元素加到maxValue上
    maxValue += x

# 定义一个随机生成函数
def randomGen():
    # 导入random模块
    import random
    # 生成一个0到maxValue之间的随机整数
    val = random.randint(0, maxValue)
    # 遍历BLOCK_TYPE_VALUE列表
    for i, x in enumerate(BLOCK_TYPE_VALUE):
        # val减去x
        val -= x
        # 如果val小于等于0，返回i
        if val <= 0:
            return i

# 遍历11到100的数字
for x in range(11, 100):
    # 打开data/level/目录下的x.x文件，如果不存在则创建
    with open('data/level/' + str(x) + ".x", "w") as fp:
        # 写入一行99999999999999999999
        fp.write("99999999999999999999\n")
        # 循环7次
        for i in range(7):
            # 定义一个字符串row，初始值为9
            row = "9"
            # 循环18次
            for j in range(18):
                # 将随机生成的数字添加到row中
                row += str(randomGen())
            # 在row末尾添加9和换行符
            row += "9\n"
            # 将row写入文件
            fp.write(row)
        # 循环8次
        for i in range(8):
            # 写入一行90000000000000000009
            fp.write("90000000000000000009\n")
