'''v1.11
    1.优化敌方坦克剩余数量提示
    2.实现敌方坦克的移动
         随机移动（在某一方向移动一定的距离的时候，随机更改移动方向）
                '''
import pygame,time,random

COLOR_BLACK = pygame.Color(100,120,120)
COLOR_RED = pygame.Color(255,0,0)
version = "v1.11"
_display = pygame.display
class MainGame():
   #游戏主窗口
    window = None
    SCREEN_HEIGHT = 500
    SCREEN_WIDTH = 800
   #我方坦克
    TANK_P1 = None
   #存储所有敌方坦克的数量
    EnemyTank_List =[]
    EnemyTank_count = 6
    def __init__(self):
        pass
    #开始游戏方法
    def startGame(self):
        _display.init()
        #创建窗口，加载窗口
        MainGame.window = _display.set_mode([MainGame.SCREEN_WIDTH,MainGame.SCREEN_HEIGHT])
        #创建我方坦克
        MainGame.TANK_P1 =Tank(400,400)
        self.creatEnemyTank()

        #设置一下游戏标题
        _display.set_caption("坦克大战"+version)
        self.getTextSurface("aaaa")
        while True:
            #给窗口完成一个颜色填充
            MainGame.window.fill(COLOR_BLACK)
            #在循环中持续完成事件的获取
            self.getEvent()
            MainGame.window.blit(self.getTextSurface("剩余敌方坦克%d辆"%len(MainGame.EnemyTank_List)),(5,5))
            #将我方坦克加入到窗口中
            MainGame.TANK_P1.displayTank()
            #将敌方坦克加入到窗口中
            self.blitEnemyTank()
            #根椐坦克的开关状态调用坦克的移动方法
            if MainGame.TANK_P1 and not MainGame.TANK_P1.stop:
                MainGame.TANK_P1.move()
                time.sleep(0.02)
            #窗口的刷新
            _display.update()
        #创建敌方坦克
    def creatEnemyTank(self):
        left = random.randint(1,7)
        top = 100
        speed = random.randint(2,5)
        for i in range(MainGame.EnemyTank_count):
            #每次都随机生成一个left值
            left = random.randint(1, 7)
            eTank = EnemyTank(left*100,top,speed)
            MainGame.EnemyTank_List.append(eTank)


        #将坦克加入到窗口中

    def blitEnemyTank(self):
        for eTank in MainGame.EnemyTank_List:
            eTank.displayTank()
           #坦克的移动方法
            eTank.randMove()




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
                    #修改坦克方向
                    MainGame.TANK_P1.direction = "L"
                    MainGame.TANK_P1.stop = False
                    #完成移动操作（调用坦克的移动方法）
                    #MainGame.TANK_P1.move()
                elif event.key == pygame.K_RIGHT:
                    print("坦克向右调头，移动")
                    MainGame.TANK_P1.direction = "R"
                    MainGame.TANK_P1.stop = False
                    # 完成移动操作（调用坦克的移动方法）
                    #MainGame.TANK_P1.move()
                elif event.key == pygame.K_UP:
                    print("坦克向上调头，移动")
                    MainGame.TANK_P1.direction = "U"
                    MainGame.TANK_P1.stop = False
                    # 完成移动操作（调用坦克的移动方法）
                    #MainGame.TANK_P1.move()
                elif event.key == pygame.K_DOWN:
                    print("坦克向下调头，移动")
                    MainGame.TANK_P1.direction = "D"
                    MainGame.TANK_P1.stop = False
                    # 完成移动操作（调用坦克的移动方法）
                    #MainGame.TANK_P1.move()
                elif event.key ==pygame.K_SPACE:
                    print("发射子弹")
            if event.type == pygame.KEYUP:
                #松开的如果是方向键，才更改移动开关状态
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                # 修改坦克的移动状态
                    MainGame.TANK_P1.stop = True

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
    def __init__(self,left,top):
        self.images = {
            "U": pygame.image.load("D:\图片\\up3.png"),
            "D": pygame.image.load("D:\图片\\down.png"),
            "L": pygame.image.load("D:\图片\\left1.png"),
            "R": pygame.image.load("D:\图片\\right2.png")

        }
        self.direction = "U"
        self.image = self.images[self.direction]
        # 坦克所在的区域 Rect->
        self.rect = self.image.get_rect()
        # 指定坦克初始化位置，分别为x, y轴的位置
        self.rect.left = left
        self.rect.top = top
        # 新增速度属性
        self.speed = 5
        # 新增属性，坦克的移动开关
        self.stop = True

    #坦克的移动方法
    def move(self):
        if self.direction == "L":
            if self .rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == "R":
            if self.rect.left + self.rect.height < MainGame.SCREEN_WIDTH:
                self.rect.left += self.speed
        elif self.direction == "U":
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == "D":
            if self.rect.top +self.rect.height < MainGame.SCREEN_HEIGHT:
                self.rect.top += self.speed

        pass
    #坦克射击方法
    def shot(self):
        pass
    #展示方法（将坦克这个surface绘制到窗口中 blit()
    def displayTank(self):
        #1.重新设置坦克的图片
        self.image =  self.images[self.direction]
        #2.将坦克加入到窗口中
        MainGame.window.blit(self.image,self.rect)

class Mytank(Tank):
    def __init__(self):
        pass

class EnemyTank(Tank):
    def __init__(self,left,top,speed):
        #图片集
        self.images = {
            "U": pygame.image.load("D:\图片\\enemyup0.png"),
            "D": pygame.image.load("D:\图片\\enemydown0.png"),
            "L": pygame.image.load("D:\图片\\enemyleft0.png"),
            "R": pygame.image.load("D:\图片\\enemyright0.png")

        }
        self.direction = self.randDirection()
        self.image = self.images[self.direction]
        # 坦克所在的区域 Rect->
        self.rect = self.image.get_rect()
        # 指定坦克初始化位置，分别为x, y轴的位置
        self.rect.left = left
        self.rect.top = top
        # 新增速度属性
        self.speed = speed
        # 新增属性，坦克的移动开关
        self.stop = True
        #新增步数属性，用业控制坦克的随机移动
        self.step = 50
    def randDirection(self):
        num = random.randint(1,4)
        if num == 1:
            return "U"
        elif num == 2:
            return "D"
        elif num == 3:
            return "L"
        elif num == 4:
            return "R"
    #随机移动
    def randMove(self):
        #如果步数为0，更改方向，步数复位
        if self.step <= 0:
            self.direction = self.randDirection()
            self.step = 50
        else:
            self.move()
            self.step -= 1
    def displayTank(self):
        super().displayTank()


#图片
        #方向
        #rect
        #速度
        #live 是否活着
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


