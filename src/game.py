import pygame
from pygame.locals import *
from const import *
from player import *
from ball import *
from level import *
from block import *

class Game(object):
    def __init__(self, surface):
        """
        初始化游戏对象。

        :param surface: 游戏窗口的表面对象，用于绘制游戏元素。
        """
        # 初始化 Pygame 的 mixer 模块，用于处理音频
        pygame.mixer.init()
        # 将传入的 surface 对象赋值给 self.surface，用于后续的绘制操作
        self.surface = surface
        # 调用 Load 方法加载第一关
        self.Load(1)

    
    # 加载关卡
    def Load(self, lv):
        # 设置关卡等级
        self.level = Level(lv)
        # 设置游戏是否结束的标志
        self.isGameOver = False
        # 初始化小球列表
        self.balls = []
        # 加载玩家
        self.loadPlayer()
        # 加载一个球，位置为玩家位置的上方，方向为1，-1
        self.loadOneBall(self.player.GetRect().x, self.player.GetRect().y - SPRITE_SIZE_H - 5, 1, -1)
        # 加载方块图片
        self.loadBlockImages()
    
    def loadPlayer(self):
        # 加载玩家，但未显示
        self.player = Player(
            # 玩家资源路径
            PLAYER_RES, 
            # 玩家初始位置，水平居中，垂直位置为游戏区域高度减去玩家高度
            (GAME_SIZE[0] - PLAYER_SIZE_W)/2, GAME_SIZE[1] - PLAYER_SIZE_H, 
            # 玩家位置的x的最小最大，最小为精灵宽度，最大为游戏区域宽度减去玩家宽度减去精灵宽度
            SPRITE_SIZE_W, GAME_SIZE[0] - PLAYER_SIZE_W - SPRITE_SIZE_W)
     
    # 加载一个球
    def loadOneBall(self, x, y, dirX, dirY):
        # 创建一个球对象，传入球的资源、位置和方向
        ball = Ball(BALL_RES, x, y, dirX, dirY)
        # 将球对象添加到球的列表中
        self.balls.append(ball)

    # 加载方块图片
    def loadBlockImages(self):
        # 初始化方块列表
        self.blocks = []
        # 遍历关卡中的所有方块集合
        for block in self.level.GetBlocks():
            # 创建方块对象。方块数字、行、列、基准点
            sp = Block(block[2], block[0], block[1], (0, 0))
            # 将方块对象添加到方块列表中
            self.blocks.append(sp)
            
    def update(self):
        """
        更新游戏状态。

        该方法会更新玩家和球的位置，并检查碰撞。如果游戏已经结束，则直接返回。
        """
        # 如果游戏已经结束，则直接返回
        if self.isGameOver:
            return
        # 更新玩家的位置
        self.player.update()
        # 更新每个球的位置
        [ball.update() for ball in self.balls]
        # 检查碰撞
        self.checkCollide()
        # 如果游戏胜利
        if self.isGameWin():
            # 加载下一关
            self.Load( self.level.level + 1 )

    def draw(self):
        # 如果游戏结束，则加载游戏结束图片并绘制到屏幕上
        if self.isGameOver:
            img = pygame.image.load(GAME_OVER_RES)
            self.surface.blit(img, img.get_rect())
            return
        # 绘制玩家
        self.player.draw(self.surface)
        # 绘制所有方块
        [block.draw(self.surface) for block in self.blocks]
        # 绘制所有小球
        [ball.draw(self.surface) for ball in self.balls]


    # 检查球和方块是否碰撞
    def checkBallBlockCollide(self):
        # 遍历所有球
        for ball in self.balls:
            # 遍历所有方块
            for block in self.blocks:
                # 如果球和方块的矩形相交
                if ball.GetRect().colliderect( block.GetRect() ):
                    # 改变球的方向
                    ball.changeDirection( block.GetRect() )
                    # 处理方块
                    self.processBlock(ball, block)
                    # 跳出循环
                    break

    # 处理球与方块碰撞
    def processBlock(self, ball, block):
        # 如果方块类型为COPY，则复制球
        if block.GetBlockType() == BlockType.COPY:
            self.copyBalls()
        # 如果方块类型为SPEED_UP，则将球的速度设置为1.5
        if block.GetBlockType() == BlockType.SPEED_UP:
            ball.SetSpeed(1.5)
        # 如果方块类型为SPEED_DOWN，则将球的速度设置为0.2
        if block.GetBlockType() == BlockType.SPEED_DOWN:
            ball.SetSpeed(0.2)
        # 如果方块类型为WALL，则不处理----这就是游戏的边界
        if block.GetBlockType() == BlockType.WALL:
            return
        # 从方块列表中移除该方块
        self.blocks.remove(block)
 
    def checkBallPlayerCollide(self):
        # 遍历所有的球
        for ball in self.balls:
            # 如果球和玩家的矩形相交
            if ball.GetRect().colliderect( self.player.GetRect() ):
                # 改变球的方向
                ball.changeYDirection( self.player.GetRect() )
                # 跳出循环，考虑到多球与一个人相撞的情况去掉-wwh
                # break

    def checkCollide(self):
        # 检查球与砖块的碰撞
        self.checkBallBlockCollide()
        # 检查球与玩家的碰撞
        self.checkBallPlayerCollide()

        # 设置标志位，用于判断是否需要继续循环
        flag = True
        while flag:
            # 将标志位设为False
            flag = False
            # 遍历所有的球
            for ball in self.balls:
                # 如果球的y坐标大于游戏区域的高度
                if ball.GetRect().y > GAME_SIZE[1]:
                    # 将球从列表中移除
                    self.balls.remove(ball)
                    # 将标志位设为True
                    flag = True
                    # 跳出循环
                    break
        # 如果球的数量为0，则游戏结束
        if len(self.balls) == 0:
            self.isGameOver = True
    
    def copyBalls(self):
        # 复制self.balls中的所有球
        balls = [ball for ball in self.balls]
        # 遍历所有球
        for ball in balls:
            # 加载一个球，参数为球的x坐标、y坐标、速度x、速度y
            self.loadOneBall(ball.GetRect().x, ball.GetRect().y, 1, -1)

    # 判断游戏是否胜利
    def isGameWin(self):
        # 遍历所有方块
        for block in self.blocks:
            # 如果方块类型不是墙
            if block.GetBlockType() != BlockType.WALL:
                # 返回False
                return False
        # 如果所有方块都是墙，返回True
        return True