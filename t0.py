'''明白需求（基于面向对象的分析）
    1.有哪些需求   2.不同的类具有不同的功能：
        1.主逻辑
            1开始游戏
            2结束游戏
        2.坦克类（1.我方坦克，2.敌方坦克）
            移动
            射击
        3.子弹类
            移动
        4.爆炸效果类
            展示爆炸效果
        5.墙壁类
            属性：是否可以通过
        6.音效类
            播放音乐'''
'''v1.03
        新增功能
        创建游戏窗口
        用游戏引擎中的功能模块
        官方开发文档'''
import pygame
COLOR_BLACK = pygame.Color(100,120,120)
_display = pygame.display
class MainGame():
   #游戏主窗口
    window = None
    SCREEN_HEIGHT = 500
    SCREEN_WIDTH = 800
    def __init__(self):
        pass
    #开始游戏方法
    def startGame(self):
        _display.init()
        #创建窗口，加载窗口
        MainGame.window = _display.set_mode([MainGame.SCREEN_WIDTH,MainGame.SCREEN_HEIGHT])
        #设置一下游戏标题
        _display.set_caption("坦克大战v1.03")
        while True:
            #给窗口完成一个颜色填充
            MainGame.window.fill(COLOR_BLACK)

            _display.update()
    #结束游戏方法

    def endGame(self):
        print("谢谢使用")
        #结束pythonq解释器
        exit()

class Tank():
    def __init__(self):
        pass
    #坦克的移动方法
    def move(self):
        pass
    #坦克射击方法
    def shot(self):
        pass
    #展示方法
    def displayTank(self):
        pass
class Mytank(Tank):
    def __init__(self):
        pass
class EnemyTank(Tank):
    def __init__(self):
        pass
class Bullet():
    def __init__(self):
        pass
    #子弹的移动
    def move(self):
        pass
    #子弹的展视
    def displayBullet(self):
        pass
class Explode():
    def __init__(self):
        pass
    #展视爆炸效果
    def displayExplode(self):
        pass
class Wall():
    def __init__(self):
        pass
    #展示墙壁的方法
    def displayWall(self):
        pass
class Music():
    def __init__(self):
        pass
    #开始播放音乐
    def play(self):
        pass
game = MainGame()
game.startGame()


