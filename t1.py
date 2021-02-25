
import pygame

COLOR_BLACK = pygame.Color(100,120,120)
COLOR_RED = pygame.Color(255,0,0)
version = "v1.04"
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
        _display.set_caption("坦克大战"+version)
        self.getTextSurface("aaaa")
        while True:
            #给窗口完成一个颜色填充
            MainGame.window.fill(COLOR_BLACK)
            #在循环中持续完成事件的获取
            self.getEvent()
            MainGame.window.blit(self.getTextSurface("剩余敌方坦克%d辆"%5),(5,5))
            #窗口的刷新
            _display.update()


    #获取程序期间所有事件（鼠标事件，键盘事件）
    def getEvent(self):
        #1.获取所有事件
        eventList = pygame.event.get()
       #2.对事件进行处理（1.点击关闭按钮  2.按下键盘上的某个按键)
        for event in eventList:
            #判断event.type 是否QUIT，如果是退出的话，直接调用程序结束方法
            if event.type == pygame.QUIT:
                self.endGame()
            #判断事件是否为按键按下，如果是，继续判断按键是哪一个按键，来进行对应的处理
            if event.type == pygame.KEYDOWN:
             #具体是哪一个按键的处理
                if event.key == pygame.K_LEFT:
                    print("坦克向左调头，移动")
                elif event.key == pygame.K_RIGHT:
                    print("坦克向右调头，移动")
                elif event.key == pygame.K_UP:
                    print("坦克向上调头，移动")
                elif event.key == pygame.K_DOWN:
                    print("坦克向下调头，移动")
                elif event.key ==pygame.K_SPACE:
                    print("发射子弹")
    #左上角文字绘制的功能
    def getTextSurface(self,text):
        #初始化字体模块
        pygame.font.init()
        #查看系统支持的所有字体
        #fontList = pygame.font.get_fonts()
        #print(fontList)
        font = pygame.font.SysFont("kaiti",18)
        #使用对应的字符完成相关内容绘制
        textSurface = font.render(text,True,COLOR_RED)
        return textSurface






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


