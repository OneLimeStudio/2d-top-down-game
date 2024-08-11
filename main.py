import game
import intro
import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
font = pygame.font.Font('freesansbold.ttf', 32)
clock = pygame.time.Clock()


while (1):
    GAME = game.Game(window,font,clock)
    GAME.GameLoop()
    if(GAME.GameQUIT == True):
        break
    if(GAME.gameEnd == True):
        LastScene = intro.gameIntro(window,font,clock)
    
        LastScene.Gameloop()
    if(LastScene.LastSceneQUIT == True):
        break