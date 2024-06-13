import pygame
from pygame.locals import *

class GameInputs:
    def __init__(self):
        self.key = None
        self.scroll = 0
        self.jump_force = 0

    def move_left_right(self):
        self.key = pygame.key.get_pressed()
        if self.key[pygame.K_LEFT] and self.scroll > 0:
            self.scroll -= 5
        if self.key[pygame.K_RIGHT] and self.scroll < 3000:
            self.scroll += 5
        return self.scroll
    
    def jumping(self):
        self.key = pygame.key.get_pressed()
        if self.key[pygame.K_SPACE]:
            self.jump_force += 3.2
        else:
            self.jump_force = 0
        return self.jump_force
        

    