"""
该代码段是一个简单的Pygame游戏主循环实现。它负责初始化Pygame环境，创建游戏窗口，并在窗口中进行游戏的持续更新和绘制。

1. 导入必要的模块，包括Pygame库、系统模块以及自定义的游戏和常量模块。
2. 初始化Pygame并设置游戏窗口大小。
3. 创建游戏对象实例。
4. 进入游戏主循环，在循环中处理退出事件，更新游戏状态，填充窗口背景色，绘制游戏元素，并更新显示。

这段代码是游戏运行的核心部分，确保游戏的持续运行和交互。
"""
# 导入pygame和sys模块
import pygame, sys
# 从pygame.locals模块中导入所有常量
from pygame.locals import *
# 从game模块中导入所有内容
from game import *
# 从const模块中导入所有内容
from const import *

# 初始化pygame
pygame.init()
# 设置游戏窗口大小
DISPLAYSURF = pygame.display.set_mode(GAME_SIZE)
# 创建游戏对象
game = Game(DISPLAYSURF)

# 游戏循环
while True:
    # 获取事件
    for event in pygame.event.get():
        # 如果事件类型为退出
        if event.type == QUIT:
            # 退出pygame
            pygame.quit()
            # 退出程序
            sys.exit()
    # 更新游戏
    game.update()
    # 填充窗口为白色
    DISPLAYSURF.fill( (255, 255, 255) )
    # 绘制游戏
    game.draw()
    # 更新显示
    pygame.display.update()
