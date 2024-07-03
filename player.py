import pygame
import math
import os

class Player:
    
    ImageSize = (100,100)

    
    def __init__(self,x,y,window):
        self.x = x
        self.y = y
        self.window = window
        
        self.playerWidth =  100
        self.playerHeight = 100
        self.moveDistance  = 5
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'player.png')
        self.imp = pygame.image.load(filename)
        self.imp = pygame.transform.scale(self.imp,(self.playerWidth,self.playerHeight))
        self.imp = pygame.transform.rotate(self.imp, 180)

        #self.blitRotateCenter(self.window,self.imp,(self.x,self.y),270)
        
    def blitRotateCenter(self, window, image, topleft, angle):

        rotated_image = pygame.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

        self.window.blit(rotated_image, new_rect)
             
    

    def move(self,keys):
        # if event.key == pygame.K_a:
        #     self.x -= self.moveDistance 
        # elif event.key == pygame.K_d:
        #     self.x += self.moveDistance
        # elif event.key == pygame.K_w:
        #     self.y += self.moveDistance
        # elif event.key == pygame.K_s:
        #     self.y -= self.moveDistance
        # else:
        #     pass

  
        if keys[pygame.K_a]:
            self.x -= self.moveDistance
        if keys[pygame.K_d]:
            self.x += self.moveDistance
        if keys[pygame.K_w]:
            self.y -= self.moveDistance
        if keys[pygame.K_s]:
            self.y += self.moveDistance

            
            
            
        
    def rotate_draw(self,HEALTH,scroll = [0,0]):
        Mouse_X , Mouse_Y = pygame.mouse.get_pos()
        distanceX = ((self.x + self.playerWidth/2 )- Mouse_X)
        distanceY = ((self.y + self.playerHeight/2) - Mouse_Y)
        
        
        angle = math.atan2(distanceY,distanceX)
        angle = -1 *( angle*180)/math.pi
        
        pygame.draw.rect(self.window,(0,200,0), (self.x,self.y+self.playerHeight,HEALTH,10))
        self.blitRotateCenter(self.window,self.imp,(self.x - scroll[0],self.y - scroll[1]),angle=angle)
    

    