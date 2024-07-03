import pygame
import random
import math
import os
class Enemy:
    
    def __init__(self,x,y) :
        self.x = x
        self.y = y
        self.Size = 30
        self.SPEED = 3
        self.isFlagged = False
        self.color = (0,90,0)
        
        #char = random.choice(["cherry.png","zoro.png","enemy.png","nier.png","saber.png"])
        #self.imp = pygame.image.load("/home/xd/projects/2dVampireSurvivor/char/"+char)

        #self.imp = pygame.transform.rotate(self.imp, 180)
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'enemy.png')
        self.imp = pygame.image.load(filename)
        
        self.imp = pygame.transform.scale(self.imp,(self.Size*3,self.Size*3))
        self.imp = pygame.transform.rotate(self.imp, 270)


    def blitRotateCenter(self, window, image, topleft, angle):

        rotated_image = pygame.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

        window.blit(rotated_image, new_rect)
             
           
    
    def rotate_draw(self,window ,Playerpos, scroll = [0,0],):
       
        distanceX = ((self.x + self.Size/2 )- Playerpos[0])
        distanceY = ((self.y + self.Size/2) - Playerpos[1])
        
        
        angle = math.atan2(distanceY,distanceX)
        angle = -1 *( angle*180)/math.pi
        self.blitRotateCenter(window,self.imp,(self.x - 2*self.Size - scroll[0],self.y - 2*self.Size - scroll[1]),angle=angle)
   
    def draw(self,window,scroll = [0,0]):
        #pygame.draw.circle(window,self.color,[self.x - scroll[0],self.y - scroll[1]],self.Size,0 )
        pass #draws hit box
    def move(self,Playerpos):
        distanceX = ((self.x  )- Playerpos[0])
        distanceY = ((self.y ) - Playerpos[1])
        self.angle =   math.atan2(distanceY,distanceX)
        self.x += -1 *math.cos(self.angle) *self.SPEED
        self.y += -1 * math.sin(self.angle) * self.SPEED


    
