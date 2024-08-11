import pygame
import bullets
import random 
import enemy
import math
import player
import intro


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
class Game():
    def __init__(self,window,font,clock):
        self.SCORE = 0
        self.font = font
        self.GameQUIT = False
        self.clock = clock
        self.window = window
        
        self.gameEnd = False
        self.score = self.font.render( str(self.SCORE), True, (0,255,0), (0,0,0))
        self.scoreRect = self.score.get_rect()
        self.scoreRect.center = (SCREEN_WIDTH - SCREEN_HEIGHT/5, SCREEN_HEIGHT/10)

        
        self.Bullets = []
        self.Enemies = []
        self.remove = True
        self.scroll = [0,0]
        self.flag = 0
        self.health = 100
        self.difficulty = 60
        self.running = True
        self.mc = player.Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,window=window)
        self.allProgress=False
    
    def GameLoop(self):
        while(self.running):
            self.clock.tick(60)
            self.window.fill((100,100,100))
            self.score = self.font.render( str(self.SCORE), True, (0,255,0), (100,100,100))
            self.window.blit(self.score,self.scoreRect)
            
            if (self.flag == 0):
                Spawner = [random.randrange(-100,SCREEN_WIDTH + 100 ,30),random.choice([-100,SCREEN_HEIGHT+100])]
                self.Enemies.append(enemy.Enemy(Spawner[0], Spawner[1]))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.GameQUIT = True
                    break
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.Bullets.append(bullets.Bullet(self.mc.x,self.mc.y))
            
            
            keys = pygame.key.get_pressed()
            self.mc.move(keys=keys)
            
            for bullet in self.Bullets:
                bullet.move()
                bullet.draw(window = self.window)
                if(bullet.x > SCREEN_WIDTH or bullet.y < 0):
                    self.Bullets.remove(bullet)
                for enemyy in self.Enemies:
                    distance = (bullet.x - enemyy.x)**2  + (bullet.y - enemyy.y)**2
           
                    if(distance  <= (enemyy.Size**2)):
                        self.Enemies.remove(enemyy)
                        self.SCORE += 1
                        if(self.SCORE%10 == 0 and self.SCORE != 0 and self.difficulty > 10):
                            self.difficulty  -=  5
                        try:
                            self.Bullets.remove(bullet)
                        except ValueError as e:
                            pass  
    
            for enemyy in self.Enemies:
                enemyy.move([self.mc.x,self.mc.y])
                #enemyy.draw(window=window)
                
                enemyy.rotate_draw(self.window,[self.mc.x,self.mc.y])
                        
                EnemydistanceToPlayer = (self.mc.x - enemyy.x)**2  + (self.mc.y - enemyy.y)**2
                    
                if(EnemydistanceToPlayer <= (enemyy.Size**2) and enemyy.isFlagged == False):
                        
                    self.health -= 10     

                    enemyy.isFlagged = True
                    if(self.health == 0):
                        self.gameEnd = True
                        
                        self.health = 100
                        self.SCORE = 0
                        
                        
                        self.allProgrees = True  
                        return    
                        break          
                if(self.flag == 0):
                    enemyy.isFlagged =  False
            if self.allProgress:
                self.Enemies.clear()
                self.allProgress = False
            
            self.flag = (self.flag+1) % self.difficulty
            
            self.mc.rotate_draw(self.health)
            pygame.display.update()