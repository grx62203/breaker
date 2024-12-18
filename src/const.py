"""
本文件定义了游戏中的常量，包括游戏窗口尺寸、玩家角色与精灵的尺寸、资源文件路径以及方块类型和声音资源的枚举类。

- `GAME_SIZE`：游戏窗口的尺寸，宽度为800像素，高度为600像素。
- `PLAYER_SIZE_W` 和 `PLAYER_SIZE_H`：玩家角色的宽度和高度。
- `SPRITE_SIZE_W` 和 `SPRITE_SIZE_H`：精灵（如球、方块等）的宽度和高度。
- `PLAYER_RES`：玩家角色的资源文件路径列表，包含不同状态的图片。
- `BALL_RES`：球的资源文件路径。
- `BLOCK_RES_FMT`：方块的资源文件路径格式，%d会被替换为具体的数字。
- `GAME_OVER_RES`：游戏结束画面的资源文件路径。

此外，还定义了两个枚举类：
- `BlockType`：表示方块的类型，包括空方块、加速方块、普通方块、复制方块、减速方块和墙壁方块。
- `SoundRes`：表示声音资源的路径，包括背景音乐和游戏音效。
"""
# 游戏窗口的尺寸，宽度为800像素，高度为600像素
GAME_SIZE = (800, 600)
# 玩家角色的宽度为96像素
PLAYER_SIZE_W = 96
# 玩家角色的高度为128像素
PLAYER_SIZE_H = 128
# 精灵（如球、方块等）的宽度为40像素
SPRITE_SIZE_W = 40
# 精灵（如球、方块等）的高度为40像素
SPRITE_SIZE_H = 40

# 玩家角色的资源文件路径列表，包含不同状态的图片
PLAYER_RES = (
    'res/player/0.png',  # 玩家角色的初始状态图片
    'res/player/1.png',  # 玩家角色的移动状态图片1
    'res/player/2.png',  # 玩家角色的移动状态图片2
    'res/player/3.png',  # 玩家角色的移动状态图片3
    'res/player/4.png',  # 玩家角色的移动状态图片4
    'res/player/5.png',  # 玩家角色的移动状态图片5
    'res/player/6.png',  # 玩家角色的移动状态图片6
)

# 球的资源文件路径
BALL_RES = "res/ball.png"
# 方块的资源文件路径格式，%d会被替换为具体的数字
BLOCK_RES_FMT = "res/block/%d.png"

# 游戏结束画面的资源文件路径
GAME_OVER_RES = "res/lose.png"

# 定义方块类型的枚举类
class BlockType:
    # 空方块，没有特殊效果
    NULL = 0
    # 加速方块，碰到后球的速度会增加
    SPEED_UP = 1
    # 普通方块，没有特殊效果
    NORMAL = 2
    # 复制方块，碰到后会复制一个球
    COPY = 3
    # 减速方块，碰到后球的速度会减小
    SPEED_DOWN = 6
    # 墙壁方块，球碰到后会反弹
    WALL = 9

# 定义声音资源的枚举类
class SoundRes:
    # 背景音乐资源路径
    JNTM = 'snd/jntm.WAV'
    # 游戏音效资源路径
    NGM = 'snd/niganma.WAV'

