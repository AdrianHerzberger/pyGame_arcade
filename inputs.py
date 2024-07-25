import pygame
from pygame.locals import *

class GameInputs:
    def __init__(self, player):
        self.player = player
        self.key = None
        self.scroll = 0

    def move_left_right(self):
        if self.player.is_dead:
            return self.scroll 
        self.key = pygame.key.get_pressed()
        if self.key[pygame.K_LEFT] and self.scroll > 0:
            self.scroll -= 5
        if self.key[pygame.K_RIGHT] and self.scroll < 3000:
            self.scroll += 5
        return self.scroll
    
    def attack_light(self):
        if self.player.is_dead:
            return False
        self.key = pygame.key.get_pressed()
        return self.key[pygame.K_COMMA]
        

    