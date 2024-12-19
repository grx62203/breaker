class Level(object):
    def __init__(self, level):

        # 初始化函数，传入参数level
        self.blocks = []  # 初始化blocks列表
        self.level = level  # 将传入的level赋值给实例变量level
        with open ('data/level/' + str(self.level) + '.x', 'r') as f:

            # 打开data/level/目录下，以level命名的文件，以只读方式打开
            r = 0  # 初始化行数r为0
            for line in f.readlines():
                # 遍历文件中的每一行
                col = len(line)
                # 获取当前行的长度
                for c in range(col - 1):
                    # 遍历当前行的每一个字符
                    if line[c] != '0':
                        # 如果当前字符不是'0'，则将其添加到blocks列表中
                        # (r, c) 表示方块的位置，int(line[c]) 表示方块的类型
                        # 此时还没有利用blocks函数实例化，只是先生成列表
                        self.blocks.append(  (r, c, int(line[c])) )
                r += 1  # 行数加1
                
    # 获取块
    def GetBlocks(self):
        # 返回块
        return self.blocks
    

