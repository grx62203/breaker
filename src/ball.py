import pygame
from pygame.locals import *
from utils import *
from const import *

class Ball(pygame.sprite.Sprite):
    def __init__(self, imgPath, x, y, dirX, dirY):
        """
        初始化 Ball 类的实例。

        :param imgPath: 球的图像文件路径。
        :param x: 球的初始 x 坐标。
        :param y: 球的初始 y 坐标。
        :param dirX: 球在 x 轴方向的初始速度。
        :param dirY: 球在 y 轴方向的初始速度。
        """
        super(Ball, self).__init__()
        # 初始化球的位置
        self.posX = x
        self.posY = y
        # 初始化球在x和y轴方向的速度
        self.dirX = dirX
        self.dirY = dirY
        # 初始化球的速度
        self.speed = 0.5
        # 加载球的图像
        img = pygame.image.load(imgPath)
        # 缩放图像到指定的大小
        img = pygame.transform.scale(img, (SPRITE_SIZE_W, SPRITE_SIZE_H))
        # 设置球的图像
        self.image = img
        # 获取图像的矩形区域
        self.rect = img.get_rect()
        # 记录上一次旋转的时间
        self.preRotateTime = getCurrentTime()
        # 加载球的音效
        self.jntmSound = pygame.mixer.Sound(SoundRes.JNTM)
        self.ngmSound = pygame.mixer.Sound(SoundRes.NGM)

    
    # 设置速度
    def SetSpeed(self, speed):
        # 将传入的speed参数赋值给self.speed
        self.speed = speed
    
    # 获取矩形
    def GetRect(self):
        # 返回矩形
        return self.rect

    def update(self):
        """
        更新球的位置和旋转状态。

        这个方法负责根据球的速度和方向更新球的位置，并根据时间间隔旋转球的图像。
        """
        # 根据球的速度和方向更新球的x坐标
        self.posX += self.speed * self.dirX
        # 根据球的速度和方向更新球的y坐标
        self.posY += self.speed * self.dirY
        # 更新球的矩形区域的x坐标
        self.rect.x = self.posX
        # 更新球的矩形区域的y坐标
        self.rect.y = self.posY
        # 如果距离上次旋转的时间超过50毫秒
        if getCurrentTime() - self.preRotateTime > 50:
            # 更新上次旋转的时间
            self.preRotateTime = getCurrentTime()
            # 旋转球的图像，旋转角度根据当前时间计算
            self.image = pygame.transform.rotate(self.image, (getCurrentTime() % 4 - 2) * 90)

    def draw(self, surface):
        # 将self.image绘制到surface上，位置为self.rect
        surface.blit(self.image, self.rect)
        
    def changeDirection(self, rect):
        """
        改变球的运动方向。

        这个方法负责根据球与其他物体的碰撞情况来改变球的运动方向。
        当球与其他物体碰撞时，根据碰撞的位置和方向来决定球的反弹方向。

        :param rect: 与球碰撞的物体的矩形区域。
        """
        # 播放球碰撞的音效
        self.jntmSound.play()
        # 如果球与物体在x轴方向的距离小于等于y轴方向的距离
        if abs(self.GetRect().x - rect.x) <= abs(self.GetRect().y - rect.y):
            # 改变球在y轴方向的速度
            self.dirY *= -1
        # 否则
        else:
            # 改变球在x轴方向的速度
            self.dirX *= -1
    def changeYDirection(self, rect):
        """
        改变球在Y轴方向的运动方向。

        这个方法负责根据球与其他物体的碰撞情况来改变球在Y轴方向的运动方向。
        当球与其他物体碰撞时，根据碰撞的位置和方向来决定球的反弹方向。

        :param rect: 与球碰撞的物体的矩形区域。
        """
        # 播放音效
        self.ngmSound.play()
        # 如果矩形在x轴上的距离小于在y轴上的距离，则改变y轴方向
        if abs(self.GetRect().x - rect.x) <= abs(self.GetRect().y - rect.y):
            # 改变球在y轴方向的速度
            self.dirY *= -1
        # 否则改变x轴方向，如果y轴方向为正，则改变y轴方向
        else:
            # 改变球在x轴方向的速度
            self.dirX *= -1
            # 如果球在y轴方向的速度为正，则改变球在y轴方向的速度
            if self.dirY > 0:
                # 改变球在y轴方向的速度
                self.dirY *= -1