import pygame
from const import *

class Block(pygame.sprite.Sprite):
    def __init__(self, blockType, rowIdx, colIdx, relativePos):
        """
        初始化 Block 类的实例。

        :param blockType: 方块的类型。
        :param rowIdx: 方块所在的行索引。
        :param colIdx: 方块所在的列索引。
        :param relativePos: 方块相对于父容器的位置。
        """
        # 调用父类（pygame.sprite.Sprite）的构造函数
        super(Block, self).__init__()
        # 设置方块的类型
        self.blockType = blockType
        # 加载方块的图像
        self.image = pygame.image.load( BLOCK_RES_FMT % blockType )
        # 缩放图像到指定的大小
        self.image = pygame.transform.scale(self.image, (SPRITE_SIZE_W, SPRITE_SIZE_H))
        # 获取图像的矩形区域
        self.rect = self.image.get_rect()
        # 计算方块的实际位置
        self.rect.x = relativePos[1] + colIdx * self.rect.width
        self.rect.y = relativePos[0] + rowIdx * self.rect.height

    
    def draw(self, surface):
        # 将self.image绘制到surface上，位置为self.rect
        surface.blit(self.image, self.rect)

    # 获取块类型
    def GetBlockType(self):
        # 返回块类型
        return self.blockType
        
    # 获取矩形
    def GetRect(self):
        # 返回矩形
        return self.rect