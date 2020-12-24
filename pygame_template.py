import sys, pygame
from pygame import *

class position:
    x = 0
    y = 0

    def moveUp(self):
        self.y -= 1
    
    def moveDown(self):
        self.y += 1

    def moveRight(self):
        self.x += 1

    def moveLeft(self):
        self.x -= 1

class App:
    windowWidth = 800
    windowHeight = 800
    color = 0,0,0
    pos = 0
    
    def __init__(self):
        self.running = True
        self.pos = position()
        self.screen = pygame.display.set_mode((App.windowWidth, App.windowHeight))
        self.block = pygame.image.load("block.jpg")
        pygame.display.set_caption("Template")

    def on_init(self):
        pygame.init()
        self.running = True

    def renderField(self):
        self.screen.fill(self.color)
        self.screen.blit(self.block, (self.pos.x, self.pos.y))
        pygame.display.flip()

    def quitEvent(self, event):
            self.running = False
            pygame.quit()
            sys.exit()

    def execute(self):
        if self.on_init() == False:
            self.running = False

        while self.running:
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            
            if(keys[K_RIGHT] and self.pos.x < self.windowWidth - self.block.get_rect().size[0]):
                self.pos.moveRight()
            elif(keys[K_LEFT] and self.pos.x > 0):
                self.pos.moveLeft()
            elif(keys[K_UP] and self.pos.y > 0):
                self.pos.moveUp()
            elif(keys[K_DOWN] and self.pos.y < self.windowHeight - self.block.get_rect().size[1]):
                self.pos.moveDown()

            self.renderField()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitEvent(event)


if __name__ == "__main__":
    App.windowWidth = 800
    App.windowHeight = 600
    app = App()
    app.execute()

    
