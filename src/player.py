import pygame
from pygame.locals import *
from utils import *
from const import *

class Player(pygame.sprite.Sprite):
    def __init__(self, imgPaths, x, y, xMin, xMax):
        """
        初始化 Player 类的实例。
 
        :param imgPaths: 玩家图像文件路径列表。
        :param x: 玩家初始位置的 x 坐标。
        :param y: 玩家初始位置的 y 坐标。
        :param xMin: 玩家位置的最小 x 坐标。
        :param xMax: 玩家位置的最大 x 坐标。
        """
        super(Player, self).__init__()
        self.images = []  # 存储玩家的图像列表
        self.imageIndex = 0  # 当前显示的图像索引
        self.posX = x  # 玩家的初始 x 坐标
        self.posY = y  # 玩家的初始 y 坐标
        self.posXMin = xMin  # 玩家位置的最小 x 坐标
        self.posXMax = xMax  # 玩家位置的最大 x 坐标
        self.preChangeTime = getCurrentTime()  # 记录上一次图像切换的时间
        for path in imgPaths:
            img = pygame.image.load(path)  # 加载图像文件
            img = pygame.transform.scale(img, (PLAYER_SIZE_W, PLAYER_SIZE_H))  # 缩放图像到指定大小
            self.images.append(img)  # 将缩放后的图像添加到图像列表


    def update(self):
        """
        更新玩家的状态。

        这个方法负责处理玩家的输入并更新玩家的位置和图像。
        """
        # 获取当前按下的所有键
        pressed = pygame.key.get_pressed()
        # 如果按下左键并且玩家的位置在最小x坐标的右侧
        if pressed[K_LEFT]:
            if self.posX > self.posXMin:
                # 向左移动玩家
                self.posX -= 3
        # 如果按下右键并且玩家的位置在最大x坐标的左侧
        if pressed[K_RIGHT]:
            if self.posX < self.posXMax:
                # 向右移动玩家
                self.posX += 3
        # 如果距离上次切换图像的时间超过200毫秒
        if getCurrentTime() - self.preChangeTime > 200:
            # 更新上次切换图像的时间
            self.preChangeTime = getCurrentTime()
            # 切换到下一张图像
            self.imageIndex = (self.imageIndex + 1) % len(self.images)
        # 如果当前时间减去上一次切换时间大于200毫秒
        if getCurrentTime() - self.preChangeTime > 200:
            # 更新上一次切换时间为当前时间
            self.preChangeTime = getCurrentTime()
            # 更新图片索引为下一张图片的索引
            self.imageIndex = (self.imageIndex + 1) % len(self.images)

    # 获取矩形
    def GetRect(self):
        # 获取当前图片
        image = self.images[ self.imageIndex ]
        # 获取图片的矩形
        rect = image.get_rect()
        # 设置矩形的位置
        rect.x = self.posX
        rect.y = self.posY
        # 返回矩形
        return rect
    
    def draw(self, surface):
        # 获取当前要绘制的图像
        image = self.images[ self.imageIndex ]
        # 将图像绘制到指定位置
        surface.blit(image, self.GetRect())

