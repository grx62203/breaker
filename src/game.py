# 导入pygame库
import pygame
# 从pygame库中导入所有常量
from pygame.locals import *
from const import *
# 从player.py文件中导入所有类
from player import *
# 从ball.py文件中导入所有类
from ball import *
# 从level.py文件中导入所有类
from level import *
# 从block.py文件中导入所有类
from block import *

class Game(object):
        def __init__(self, surface):
        """
        初始化游戏对象。

        参数:
            surface (pygame.Surface): 游戏窗口的Surface对象。
        """
        # 初始化Pygame的mixer模块，用于处理声音
        pygame.mixer.init()
        # 将传入的Surface对象赋值给self.surface，用于后续的绘制操作
        self.surface = surface
        # 调用Load方法，加载第一关的游戏数据
        self.Load(1)

    
        def Load(self, lv):
        """
        加载指定关卡的游戏数据。
    def loadPlayer(self):
        """
        加载玩家角色。

        该方法创建一个Player对象，并将其赋值给self.player。Player对象的位置在游戏窗口的底部中央。
        """
        # 创建一个Player对象，使用PLAYER_RES中的图像资源，位置在游戏窗口底部中央，宽度为SPRITE_SIZE_W，可移动范围为游戏窗口宽度减去玩家角色宽度再减去SPRITE_SIZE_W
        self.player = Player(
            PLAYER_RES, 
            (GAME_SIZE[0] - PLAYER_SIZE_W)/2, GAME_SIZE[1] - PLAYER_SIZE_H, 
            SPRITE_SIZE_W, GAME_SIZE[0] - PLAYER_SIZE_W - SPRITE_SIZE_W)

        参数:
            lv (int): 关卡编号。
        """
        # 创建一个Level对象，用于管理当前关卡的游戏数据
        self.level = Level(lv)
        # 初始化游戏结束标志为False，表示游戏尚未结束
        self.isGameOver = False
        # 初始化球的列表为空列表
        self.balls = []
        # 调用loadPlayer方法，加载玩家角色
        self.loadPlayer()
        # 调用loadOneBall方法，加载一个球，位置在玩家角色上方
        self.loadOneBall(self.player.GetRect().x, self.player.GetRect().y - SPRITE_SIZE_H - 5, 1, -1)
        # 调用loadBlockImages方法，加载方块图像
        self.loadBlockImages()
    def loadPlayer(self):
        """
        加载玩家角色。

        该方法创建一个Player对象，并将其赋值给self.player。Player对象的位置在游戏窗口的底部中央。
        """
        # 创建一个Player对象，使用PLAYER_RES中的图像资源，位置在游戏窗口底部中央，宽度为SPRITE_SIZE_W，可移动范围为游戏窗口宽度减去玩家角色宽度再减去SPRITE_SIZE_W
        self.player = Player(
            PLAYER_RES, 
            (GAME_SIZE[0] - PLAYER_SIZE_W)/2, GAME_SIZE[1] - PLAYER_SIZE_H, 
            SPRITE_SIZE_W, GAME_SIZE[0] - PLAYER_SIZE_W - SPRITE_SIZE_W)

    
    def loadPlayer(self):
        self.player = Player(
              def loadPlayer(self):
        """
        加载玩家角色。

        该方法创建一个Player对象，并将其赋值给self.player。Player对象的位置在游戏窗口的底部中央。
        """
        # 创建一个Player对象，使用PLAYER_RES中的图像资源，位置在游戏窗口底部中央，宽度为SPRITE_SIZE_W，可移动范围为游戏窗口宽度减去玩家角色宽度再减去SPRITE_SIZE_W
        self.player = Player(
            PLAYER_RES, 
            (GAME_SIZE[0] - PLAYER_SIZE_W)/2, GAME_SIZE[1] - PLAYER_SIZE_H, 
            SPRITE_SIZE_W, GAME_SIZE[0] - PLAYER_SIZE_W - SPRITE_SIZE_W)
  PLAYER_RES, 
            (GAME_SIZE[0] - PLAYER_SIZE_W)/2, GAME_SIZE[1] - PLAYER_SIZE_H, 
            SPRITE_SIZE_W, GAME_SIZE[0] - PLAYER_SIZE_W - SPRITE_SIZE_W)
    
    def loadOneBall(self, x, y, dirX, dirY):
        """
        加载一个球到游戏中。

        参数:
            x (int): 球的初始x坐标。
            y (int): 球的初始y坐标。
            dirX (int): 球在x轴上的初始方向（1表示向右，-1表示向左）。
            dirY (int): 球在y轴上的初始方向（1表示向下，-1表示向上）。
        """
        # 创建一个Ball对象，使用BALL_RES中的图像资源，位置在(x, y)，初始方向为(dirX, dirY)
        ball = Ball(BALL_RES, x, y, dirX, dirY)
        # 将创建的球添加到游戏的球列表中
        self.balls.append(ball)


    def loadBlockImages(self):
        """
        加载方块图像。

        该方法根据当前关卡的方块数据，创建并加载方块图像。
        """
        # 初始化方块列表为空列表
        self.blocks = []
        # 遍历当前关卡的方块数据
        for block in self.level.GetBlocks():
            # 创建一个Block对象，使用block[2]中的图像资源，位置在(block[0], block[1])，初始方向为(0, 0)
            sp = Block(block[2], block[0], block[1], (0, 0))
            # 将创建的方块添加到游戏的方块列表中
            self.blocks.append(sp)

    
    def update(self):
        """
        更新游戏状态。

        该方法在每一帧中被调用，用于更新游戏中的所有元素，包括玩家、球和碰撞检测。
        """
        # 如果游戏结束，直接返回，不进行更新
        if self.isGameOver:
            return
        # 更新玩家的状态
        self.player.update()
        # 更新所有球的状态
        [ball.update() for ball in self.balls]
        # 检查球与方块、玩家的碰撞
        self.checkCollide()
        # 如果游戏胜利，加载下一关
        if self.isGameWin():
            self.Load( self.level.level + 1 )


        def draw(self):
        """
        绘制游戏画面。

        该方法在每一帧中被调用，用于绘制游戏中的所有元素，包括玩家、球和方块。如果游戏结束，绘制游戏结束画面。
        """
        # 如果游戏结束，绘制游戏结束画面
        if self.isGameOver:
            # 加载游戏结束图像
            img = pygame.image.load(GAME_OVER_RES)
            # 将游戏结束图像绘制到游戏窗口的左上角
            self.surface.blit(img, img.get_rect())
            # 返回，不进行后续绘制
            return 
        # 绘制玩家角色
        self.player.draw(self.surface)
        # 绘制所有方块
        [block.draw(self.surface) for block in self.blocks]
        # 绘制所有球
        [ball.draw(self.surface) for ball in self.balls]



    def checkBallBlockCollide(self):
        """
        检查球与方块的碰撞。

        该方法遍历所有球和方块，检查它们之间是否发生碰撞。如果发生碰撞，调用球的changeDirection方法改变球的方向，并调用processBlock方法处理方块。
        """
        # 遍历所有球
        for ball in self.balls:
            # 遍历所有方块
            for block in self.blocks:
                # 如果球与方块发生碰撞
                if ball.GetRect().colliderect( block.GetRect() ):
                    # 调用球的changeDirection方法改变球的方向
                    ball.changeDirection( block.GetRect() )
                    # 调用processBlock方法处理方块
                    self.processBlock(ball, block)
                    # 跳出内层循环，继续检查下一个球
                    break


    def processBlock(self, ball, block):
        """
        处理球与方块的碰撞。

        根据方块的类型，执行相应的操作，如复制球、改变球的速度或移除方块。

        参数:
            ball (Ball): 与方块碰撞的球对象。
            block (Block): 被球碰撞的方块对象。
        """
        # 如果方块类型是COPY，调用copyBalls方法复制所有球
        if block.GetBlockType() == BlockType.COPY:
            self.copyBalls()
        # 如果方块类型是SPEED_UP，将球的速度设置为1.5倍
        if block.GetBlockType() == BlockType.SPEED_UP:
            ball.SetSpeed(1.5)
        # 如果方块类型是SPEED_DOWN，将球的速度设置为0.2倍
        if block.GetBlockType() == BlockType.SPEED_DOWN:
            ball.SetSpeed(0.2)
        # 如果方块类型是WALL，直接返回，不做任何处理
        if block.GetBlockType() == BlockType.WALL:
            return
        # 移除被碰撞的方块
        self.blocks.remove(block)

 
    def checkBallPlayerCollide(self):
        """
        检查球与玩家的碰撞。

        该方法遍历所有球，检查它们是否与玩家角色发生碰撞。如果发生碰撞，调用球的changeYDirection方法改变球在y轴上的方向。
        """
        # 遍历所有球
        for ball in self.balls:
            # 如果球与玩家角色发生碰撞
            if ball.GetRect().colliderect( self.player.GetRect() ):
                # 调用球的changeYDirection方法改变球在y轴上的方向
                ball.changeYDirection( self.player.GetRect() )
                # 跳出循环，继续检查下一个球
                break


       def checkCollide(self):
        """
        检查碰撞。

        该方法检查球与方块、玩家的碰撞，并处理球超出游戏窗口底部的情况。如果所有球都超出游戏窗口底部，游戏结束。
        """
        # 检查球与方块的碰撞
        self.checkBallBlockCollide()
        # 检查球与玩家的碰撞
        self.checkBallPlayerCollide()

        # 初始化标志位为True，表示需要检查球是否超出游戏窗口底部
        flag = True
        # 当标志位为True时，循环检查球是否超出游戏窗口底部
        while flag:
            # 将标志位设置为False，表示当前没有球超出游戏窗口底部
            flag = False
            # 遍历所有球
            for ball in self.balls:
                # 如果球的y坐标大于游戏窗口的高度，表示球超出游戏窗口底部
                if ball.GetRect().y > GAME_SIZE[1]:
                    # 从球列表中移除该球
                    self.balls.remove(ball)
                    # 将标志位设置为True，表示有球超出游戏窗口底部，需要继续检查
                    flag = True
                    # 跳出循环，继续检查下一个球
                    break
        # 如果球列表为空，表示所有球都超出游戏窗口底部，游戏结束
        if len(self.balls) == 0:
            self.isGameOver = True

    
    def copyBalls(self):
        """
        复制所有球。

        该方法遍历当前所有球，为每个球创建一个新的球，并将其添加到游戏中。新球的初始位置和方向与原球相同。
        """
        # 创建一个列表，包含当前所有球的副本
        balls = [ball for ball in self.balls]
        # 遍历所有球的副本
        for ball in balls:
            # 调用loadOneBall方法，为每个球创建一个新的球，并将其添加到游戏中，新球的初始位置和方向与原球相同
            self.loadOneBall(ball.GetRect().x, ball.GetRect().y, 1, -1)

    def isGameWin(self):
        """
        检查游戏是否胜利。

        该方法遍历所有方块，检查是否所有非墙壁类型的方块都已被移除。如果是，则返回True，表示游戏胜利；否则返回False。

        返回:
            bool: 如果所有非墙壁类型的方块都已被移除，返回True；否则返回False。
        """
        # 遍历所有方块
        for block in self.blocks:
            # 如果方块类型不是墙壁类型
            if block.GetBlockType() != BlockType.WALL:
                # 返回False，表示游戏尚未胜利
                return False
        # 如果所有方块都是墙壁类型，返回True，表示游戏胜利
        return True
