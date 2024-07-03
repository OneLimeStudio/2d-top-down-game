import pygame
import bullets
import random 
import enemy
import math
import player


#CONSTANTS

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

SCORE = 0

pygame.init()
window  = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
font = pygame.font.Font('freesansbold.ttf', 32)
score = font.render( str(SCORE), True, (0,255,0), (0,0,0))
scoreRect = score.get_rect()
scoreRect.center = (SCREEN_WIDTH - SCREEN_HEIGHT/5, SCREEN_HEIGHT/10)

Bullets = []
Enemies = []
remove = True
scroll = [0,0]
flag = 0
pygame.init()

#Variable
health = 100


difficulty = 60

running = True


mc = player.Player(0,0,window=window)

clock = pygame.time.Clock()
allProgress=False
while running:
    print(difficulty)
    clock.tick(60)
    window.fill((100,100,100))
    score = font.render( str(SCORE), True, (0,255,0), (100,100,100))
    window.blit(score,scoreRect)
    scroll[0] += ((mc.x+mc.playerWidth/2 - SCREEN_WIDTH)/2 - scroll[0]) / 30
    scroll[1] += ((mc.x+mc.playerHeight/2 - SCREEN_HEIGHT)/2 - scroll[1]) / 30
    
    


    
    
    if (flag == 0):
        Spawner = [random.randrange(-100,SCREEN_WIDTH + 100 ,30),random.choice([-100,SCREEN_HEIGHT+100])]
        Enemies.append(enemy.Enemy(Spawner[0], Spawner[1]))
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.MOUSEBUTTONUP:
            Bullets.append(bullets.Bullet(mc.x,mc.y))
    keys = pygame.key.get_pressed()
    mc.move(keys=keys)
    for bullet in Bullets:
        bullet.move()
        
        bullet.draw(window=window)
        
        if(bullet.x > SCREEN_WIDTH or bullet.y < 0):
            Bullets.remove(bullet)
        for enemyy in Enemies:
            distance = (bullet.x - enemyy.x)**2  + (bullet.y - enemyy.y)**2
            #print((mc.x - enemyy.x)**2  + (mc.y - enemyy.y)**2)
            if(distance  <= (enemyy.Size**2)):
                Enemies.remove(enemyy)
                SCORE += 1
                if(SCORE%10 == 0 and SCORE != 0 and difficulty > 10):
                    difficulty  -=  5
                try:
                    Bullets.remove(bullet)
                except ValueError as e:
                    pass  
    


    for enemyy in Enemies:
        enemyy.move([mc.x,mc.y])
        #enemyy.draw(window=window)
        
        enemyy.rotate_draw(window,[mc.x,mc.y])
                
        EnemydistanceToPlayer = (mc.x - enemyy.x)**2  + (mc.y - enemyy.y)**2
            
        if(EnemydistanceToPlayer <= (enemyy.Size**2) and enemyy.isFlagged == False):
                
            health -= 10     

            enemyy.isFlagged = True
            if(health == 0):
                health = 100
                SCORE = 0
                
                allProgrees = True      
                break          
        if(flag == 0):
            enemyy.isFlagged =  False

    if allProgress:
        Enemies.clear()
        allProgress = False
    
    
    # print(flag,difficulty)
    flag = (flag+1) % difficulty
    
    
    mc.rotate_draw(health)
    pygame.display.update()
