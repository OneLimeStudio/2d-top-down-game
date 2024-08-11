import pygame
import os

SCREEN_WIDTH = 1280 
SCREEN_HEIGHT = 720

objects = []

class Button():
    def __init__(self, x, y, width, height,window, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.window = window
        font = pygame.font.SysFont('Arial', 40)
        self.onclickFunction = onclickFunction
        self.onePress = onePress

        self.fillColors = {
            'normal': '#f5fefd',
            'hover': '#86fbee',
            'pressed': '#f5fefd',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

        objects.append(self)

    def process(self):

        mousePos = pygame.mouse.get_pos()
        
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])

                if self.onePress:
                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        self.window.blit(self.buttonSurface, self.buttonRect)







class gameIntro:
    def  __init__(self,window, font,clock):
        self.window = window
        self.font = font
        self.clock = clock
        self.running = True
        self.LastSceneQUIT = False
        
        
    def _Clicked_Play_(self):
        self.running = False
        
    def IntroScene(self):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'GameIntro.png')
        bgImgae = pygame.image.load(filename)
        self.playButton = Button(30, 30, 400, 100,self.window, 'PLAY', self._Clicked_Play_)
        self.window.blit(bgImgae,(0,0))
        
    def Gameloop(self):
        while(self.running):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.LastSceneQUIT = True
                    
            
            self.IntroScene()
            for obj in objects:
                obj.process()
            pygame.display.update()        
        