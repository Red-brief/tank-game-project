'''v1.25
    新增功能
    1.音效的处理
                '''
import pygame,time,random

COLOR_BLACK = pygame.Color(100,120,120)
COLOR_RED = pygame.Color(255,0,0)
version = "v1.25"
_display = pygame.display
class MainGame():
   #游戏主窗口
    window = None
    SCREEN_HEIGHT = 700
    SCREEN_WIDTH = 600
   #我方坦克
    TANK_P1 = None
   #存储所有敌方坦克的数量
    EnemyTank_List =[]
    EnemyTank_count = 5
   #存储我方子弹的列表
    Bullet_list = []
    #存储敌方子弹列表
    Enemy_bullet_list = []
   #爆炸效果列表
    Explode_list = []
   #墙壁列表
    Wall_list = []
    #开始游戏方法
    def startGame(self):

        _display.init()
        #创建窗口，加载窗口
        MainGame.window = _display.set_mode([MainGame.SCREEN_WIDTH,MainGame.SCREEN_HEIGHT])
        self.creatMytank()
        self.creatEnemyTank()
        self.creatWalls()

        #设置一下游戏标题
        _display.set_caption("坦克大战"+version)
        self.getTextSurface("aaaa")
        while True:
            #给窗口完成一个颜色填充
            MainGame.window.fill(COLOR_BLACK)
            #在循环中持续完成事件的获取
            self.getEvent()
            MainGame.window.blit(self.getTextSurface("剩余敌方坦克%d辆"%len(MainGame.EnemyTank_List)),(5,5))
            self.blitWalls()
            if MainGame.TANK_P1 and MainGame.TANK_P1.live:
                #将我方坦克加入到窗口中
                MainGame.TANK_P1.displayTank()
            else:
                del MainGame.TANK_P1
                MainGame.TANK_P1 = None
            #将敌方坦克加入到窗口中
            self.blitEnemyTank()
            #根椐坦克的开关状态调用坦克的移动方法
            if MainGame.TANK_P1 and not MainGame.TANK_P1.stop:
                MainGame.TANK_P1.move()
                #调用碰撞墙壁的方法
                MainGame.TANK_P1.hitWalls()
                #调用我方坦克碰撞敌方敌坦克不能移动的方法
                MainGame.TANK_P1.hitEnemyTank()
            #调用渲染子弹列表的一个方法
            self.blitBullet()
            #调用渲染敌方子弹列表的一个方法
            self.blitEnemyBullet()
            #调用展示爆炸效果的方法
            self.displayEeplodes()

            time.sleep(0.02)
            #窗口的刷新
            _display.update()
        #创建敌方坦克
    #创建我方坦克的方法
    def creatMytank(self):
        MainGame.TANK_P1 = MyTank(400,400)
       #创建音乐对象方法
        music = Music()
       #调用播放方法
        music.play()
    #创建敌方坦克
    def creatEnemyTank(self):
        left = random.randint(1,7)
        top = 100
        for i in range(MainGame.EnemyTank_count):
            speed = random.randint(3, 6)
            #每次都随机生成一个left值
            left = random.randint(1, 7)
            eTank = EnemyTank(left*100,top,speed)
            MainGame.EnemyTank_List.append(eTank)

        #将敌方坦克加入到窗口中
    #创建墙壁的方法
    def creatWalls(self):
        for i in range(1,6):
            wall = Wall(130*i,300)
            MainGame.Wall_list.append(wall)
    def blitWalls(self):
        for wall in MainGame.Wall_list:
            if wall.live:
                wall.displayWall()
            else:
                MainGame.Wall_list.remove(wall)

    def blitEnemyTank(self):
        for eTank in MainGame.EnemyTank_List:
           if eTank.live:
               eTank.displayTank()
               # 坦克的移动方法
               eTank.randMove()
               #调用敌方坦克与墙壁的碰撞方法
               eTank.hitWalls()
               #敌方坦克是否碰撞到我方坦克
               eTank.hitMyTank()
               # 调用敌方坦克的射击
               eBullet = eTank.shot()

               # 将子弹存储在敌方子弹列表中,如果子弹为None,不加入列表
               if eBullet:
                   MainGame.Enemy_bullet_list.append(eBullet)
           else:
               MainGame.EnemyTank_List.remove(eTank)
    #将我方子弹加入到窗口中
    def blitBullet(self):
        for bullet in MainGame.Bullet_list:
            #如果子弹还活着，绘制出来，否则，直接从列表中移除该子弹
            if bullet.live:
                bullet.displayBullet()
                #让子弹移动
                bullet.bulletMove()
                # 调用我方坦克与敌方坦克的碰撞方法
                bullet.hitEnemyTank()
                #调用判断我方子弹是否碰撞到墙壁的方法
                bullet.hitWalls()
            else:
                MainGame.Bullet_list.remove(bullet)
     #将敌方子弹加入到窗口中
    def blitEnemyBullet(self):
        for eBullet in MainGame.Enemy_bullet_list:
            #如果子弹活着，绘制出来，否则，直接从列表中移除该子弹
            if eBullet.live:
                eBullet.displayBullet()
                #让子弹移动
                eBullet.bulletMove()
                 #调用是否碰撞到墙壁的一个方法
                eBullet.hitWalls()
                if MainGame.TANK_P1 and MainGame.TANK_P1.live:
                    eBullet.hitMytank()
            else:
                MainGame.Enemy_bullet_list.remove(eBullet)

    def displayEeplodes(self):
        for explode in MainGame.Explode_list:
            if explode.live:
                explode.displayExplode()
            else:
                MainGame.Explode_list.remove(explode)
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
                #点击ESC按键让我方坦克重生
                if event.key == pygame.K_ESCAPE and not MainGame.TANK_P1:
                    #调用创建我方坦克的方法
                    self.creatMytank()
                if MainGame.TANK_P1 and MainGame.TANK_P1.live:

                    # 具体是哪一个按键的处理
                    if event.key == pygame.K_LEFT:
                        print("坦克向左调头，移动")
                        # 修改坦克方向
                        MainGame.TANK_P1.direction = "L"
                        MainGame.TANK_P1.stop = False
                        # 完成移动操作（调用坦克的移动方法）
                        # MainGame.TANK_P1.move()
                    elif event.key == pygame.K_RIGHT:
                        print("坦克向右调头，移动")
                        MainGame.TANK_P1.direction = "R"
                        MainGame.TANK_P1.stop = False
                        # 完成移动操作（调用坦克的移动方法）
                        # MainGame.TANK_P1.move()
                    elif event.key == pygame.K_UP:
                        print("坦克向上调头，移动")
                        MainGame.TANK_P1.direction = "U"
                        MainGame.TANK_P1.stop = False
                        # 完成移动操作（调用坦克的移动方法）
                        # MainGame.TANK_P1.move()
                    elif event.key == pygame.K_DOWN:
                        print("坦克向下调头，移动")
                        MainGame.TANK_P1.direction = "D"
                        MainGame.TANK_P1.stop = False
                        # 完成移动操作（调用坦克的移动方法）
                        # MainGame.TANK_P1.move()
                    elif event.key == pygame.K_SPACE:
                        print("发射子弹")
                        if len(MainGame.Bullet_list) < 3:
                            # 产生一颗子弹
                            m = Bullet(MainGame.TANK_P1)
                            # 将子弹加入子弹列表
                            MainGame.Bullet_list.append(m)
                            music =Music("")
                        else:
                            print("子弹数量不足")
                        print("当前屏幕中子弹在数量为：%d" % len(MainGame.Bullet_list))


            if event.type == pygame.KEYUP:
                #松开的如果是方向键，才更改移动开关状态
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    if MainGame.TANK_P1 and MainGame.TANK_P1.live:
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
class BaseItem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.sprite.__init__(self)
class Tank(BaseItem):
    def __init__(self,left,top):
        self.images = {
            "U": pygame.image.load("D:\图片\\up6.png"),
            "D": pygame.image.load("D:\图片\\down5.png"),
            "L": pygame.image.load("D:\图片\\left5.png"),
            "R": pygame.image.load("D:\图片\\right5.png")

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
        #新增属性  live 用来记录，坦克是否活着
        self.live = True
        #新增属性，用来记录坦克的移动之前的坐标（用于坐标还原时使用）
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top

    #坦克的移动方法
    def move(self):
        #先记录移动之前的坐标
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top

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
    def stay(self):
        self.rect.left = self.oldLeft
        self.rect.top = self.oldTop
    #新增碰撞墙壁的方法
    def hitWalls(self):
        for wall in MainGame.Wall_list:
            if pygame.sprite.collide_rect(wall,self):
                self.stay()
    #坦克射击方法
    def shot(self):
        return Bullet(self)
    #展示方法（将坦克这个surface绘制到窗口中 blit()
    def displayTank(self):
        #1.重新设置坦克的图片
        self.image =  self.images[self.direction]
        #2.将坦克加入到窗口中
        MainGame.window.blit(self.image,self.rect)

class MyTank(Tank):
    def __init__(self,left,top):
        super(MyTank,self).__init__(left,top)
    #新增主动碰撞到敌方坦克的方法
    def hitEnemyTank(self):
        for eTank in MainGame.EnemyTank_List:
            if pygame.sprite.collide_rect(eTank,self):
                self.stay()


class EnemyTank(Tank):
    def __init__(self,left,top,speed):
        super(EnemyTank,self).__init__(left,top)
        #self.live = True
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
    def shot(self):
        num = random.randint(1,1000)
        if num <= 25:
            return Bullet(self)
    #碰撞我方坦克的方法
    def hitMyTank(self):
        if MainGame.TANK_P1 and MainGame.TANK_P1.live:
            if pygame.sprite.collide_rect(self,MainGame.TANK_P1):
                #让敌方坦克停下来
                 self.stay()


class Bullet(BaseItem):
    def __init__(self,tank):
    #图片
        self.image = pygame.image.load("D:\图片\\bullet5.png")
    #方向（取决于坦克的方向）
        self.direction = tank.direction
    #位置
        self.rect = self.image.get_rect()
    #速度
        self.speed = 7
        if self.direction == "U":
            self.rect.left = tank.rect.left + tank.rect.width/2 - self.rect.width/2
            self.rect.top = tank.rect.top - self.rect.height
        elif self.direction == "D":
            self.rect.left = tank.rect.left + tank .rect.width/2 - self.rect.width/2
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction == "L":
            self.rect.left = tank.rect.left - self.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.width/2 - self.rect.width / 2
        elif self.direction == "R":
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + tank.rect.width/2 - self.rect.width/2
        #速度
        speed = 7
        #用来记录子弹是否活着
        self.live = True


    #子弹的移动
    def bulletMove(self):
        if self.direction == "U":
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                #修改状态值
                self.live = False
        elif self.direction == "D":
            if self.rect.top < MainGame.SCREEN_HEIGHT - self.rect.height:
                self.rect.top += self.speed
            else:
                self.live = False
        elif self.direction == "L":
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                self.live = False
        elif self.direction == "R":
            if self.rect.left< MainGame.SCREEN_WIDTH - self.rect.width:
                self.rect.left += self.speed
            else:
                self.live = False

    #子弹的展视
    def displayBullet(self):
        MainGame.window.blit(self.image,self.rect)
    #新增我方子弹碰撞敌方坦克的方法
    def hitEnemyTank(self):
        for eTank in MainGame.EnemyTank_List:
            if pygame.sprite.collide_rect(eTank,self):
                #产生一个爆炸效果
                explode =Explode(eTank)
                #将爆炸效果加入爆炸效果列表中
                MainGame.Explode_list.append(explode)
                self.live = False
                eTank.live = False
    def hitMytank(self):
        if pygame.sprite.collide_rect(self,MainGame.TANK_P1):
            # 产生爆炸效果，并加入到爆炸效果列表中
            explode =Explode(MainGame.TANK_P1)
            MainGame.Explode_list.append(explode)

            #修改子弹状态
            self.live = False
            #修改我方坦克状态
            MainGame.TANK_P1.live = False
    #新增子弹与墙壁的碰撞
    def hitWalls(self):
        for wall in MainGame.Wall_list:
            if pygame.sprite.collide_rect(wall,self):
                #修改子弹的属性
                self.live = False
                wall.hp -= 1
                if wall.hp <= 0:
                    wall.live = False

class Explode():
    def __init__(self,tank):
        self.rect = tank.rect
        self.step = 0
        #加入子弹爆炸效果的过程图片
        self.images =[pygame.image.load("D:\图片\p1.png"),pygame.image.load("D:\图片\p2.png")]
        self.image = self.images[self.step]
        self.live = True
    #展视爆炸效果
    def displayExplode(self):
        if self.step < len(self.images):
            MainGame.window.blit(self.image,self.rect)
            self.image = self.images[self.step]
            self.step += 1


        else:
            self.live = False
            self.step = 0
class Wall():
    def __init__(self,left,top):
        self.image = pygame.image.load("D:\图片\\wall.png")
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        #用来决定墙壁是否应该在窗口中展示
        self.live = True
        #用来记录墙壁的生命值
        self.hp = 10
    #展示墙壁的方法
    def displayWall(self):
        MainGame.window.blit(self.image,self.rect)
class Music():
    def __init__(self,name,fileName):
        self.fileName = fileName
        #初始化混音器
        pygame.mixer.init()
        pygame.mixer.music.load(self.fileName)
    #开始播放音乐
    def play(self):
        pygame.mixer.music.play(loops = 0)
game = MainGame()
game.startGame()


