import pygame
import time
from random import randint

class Player:
    x=[]
    y=[]
    step=44
    direction=0
    length=3

    updateCountMax=2
    updateCount=0

    def __init__(self,length):
        self.length=length
        for i in range(0,2000):
            self.x.append(-100)
            self.y.append(-100)
        self.x[1]=1*44
        self.x[2]=2*44




    def update(self):
        self.updateCount=self.updateCount+1
        if self.updateCount > self.updateCountMax:
            for i in range(self.length-1,0,-1):
              
                self.x[i]=self.x[i-1]
                self.y[i]=self.y[i-1]



            if self.direction==0:
                self.x[0]=self.x[0]+self.step
            if self.direction==1:
                self.x[0]=self.x[0]-self.step
            if self.direction==2:
                self.y[0]=self.y[0]-self.step
            if self.direction==3:
                self.y[0]=self.y[0]+self.step
            self.updateCount=0


    def moveRight(self):
        self.direction=0

    def moveLeft(self):
        self.direction=1

    def moveUp(self):
        self.direction=2

    def moveDown(self):
        self.direction=3

    def draw(self,surface,image):
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i]))



class Apple:
    x=0
    y=0
    step=44

    def __init__(self,x,y):

        self.x=x*self.step
        self.y=y*self.step

    def draw(self,surface,image):
        surface.blit(image,(self.x,self.y))


class Game:
    def isCollision(self,x1,y1,x2,y2,bsize):
        if x1>=x2 and x1<=x2+bsize:
            if y1>=y2 and y1<=y2+bsize:
                return True
        return False

class App:
    displayWidth=800
    displayHeight=600
    player=0
    apple=0

    def __init__(self):
        self.running=True
        self.display=None
        self.image=None
        self.apples=None
        self.game=Game()
        self.player=Player(3)
        self.apple=Apple(5,5)
    def onInit(self):
        pygame.init()
        self.display=pygame.display.set_mode((self.displayWidth,self.displayHeight),pygame.HWSURFACE)
        pygame.display.set_caption('Snek gem')
        self.running=True
        self.image=pygame.image.load("snek.png").convert()
        self.apples=pygame.image.load("epl.png").convert()

    def onEvent(self,event):
        if event.type==QUIT:
            self.running=False
    

    def onLoop(self):
        self.player.update()
        #snek eat epl
        for i in range(0,self.player.length):
            if self.game.isCollision(self.apple.x,self.apple.y,self.player.x[i],self.player.y[i],44):
                self.apple.x=randint(2,9)*44
                self.apple.y=randint(2,9)*44
                self.player.length=self.player.length+1
        
        #snake eats itself
        for i in range(2,self.player.length):
            if self.game.isCollision(self.player.x[0],self.player.y[0],self.player.x[i],self.player.y[i],40):
                print("you lose")
                exit(0)
        pass
        

    def onRender(self):
        self.display.fill((0,0,0))
        self.player.draw(self.display,self.image)
        self.apple.draw(self.display,self.apples)
        pygame.display.flip()

    def onCleanup(self):
        pygame.quit()


    def onExec(self):
        if self.onInit()==False:
            self.running=False
        
        while (self.running):
            pygame.event.pump()
            keys=pygame.key.get_pressed()

            if (keys[pygame.K_RIGHT]):
                self.player.moveRight()
            if (keys[pygame.K_LEFT]):
                self.player.moveLeft()
            if (keys[pygame.K_UP]):
                self.player.moveUp()
            if (keys[pygame.K_DOWN]):
                self.player.moveDown()
            if (keys[pygame.K_ESCAPE]):
                self.running=False

            self.onLoop()
            self.onRender()


            time.sleep(50.0/1000.0)
        self.onCleanup()


app=App()
app.onExec()

