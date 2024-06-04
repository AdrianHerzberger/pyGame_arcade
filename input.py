import pygame
from pygame.locals import *

class GameInputs:
    
    def __init__(self):
        self.key = None

    def move_left_right(self, scroll):
        self.key = pygame.key.get_pressed()
        if self.key[pygame.K_LEFT]:
            scroll -= 5
        if self.key[pygame.K_RIGHT]:
            scroll += 5
        return scroll

    