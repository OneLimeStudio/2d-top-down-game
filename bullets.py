import pygame
import math
class Bullet:
    
    def __init__(self,x,y):
        self.x = x + 50
        self.y = y + 50
        self.BulletSize = 5
        self.SPEED = 25
        
        self.color = (0,255,0)
        self.MouseX , self.MouseY = pygame.mouse.get_pos()
        # if self.MouseX - self.x == 0:
        #     self.MouseX  = 0.0001
        # self.slope = (self.MouseY - self.y) / (self.MouseX - self.x)
        # self.c = self.y - self.x * self.slope
        # if(self.MouseX - self.x >= 0):
        #     self.step = self.SPEED
        # else:
        #     self.step = -self.SPEED
        distanceX = ((self.x  )- self.MouseX)
        distanceY = ((self.y ) - self.MouseY)
        BulletSound = pygame.mixer.Sound("bullet.wav")
        self.angle =   math.atan2(distanceY,distanceX)
        pygame.mixer.Sound.play(BulletSound)
        pygame.mixer.music.stop()
        #self.angle = ( self.angle*180)nceY/math.pi
    def draw(self,window,scroll = [0,0]):
        pygame.draw.circle(window,self.color,[self.x - scroll[0],self.y - scroll[1]],self.BulletSize,0 )
    
    def move(self):
        #self.x += self.step
        #self.y = self.slope * self.x  + self.c

        self.x += -1 *math.cos(self.angle) *self.SPEED
        self.y += -1 * math.sin(self.angle) * self.SPEED
    
        
