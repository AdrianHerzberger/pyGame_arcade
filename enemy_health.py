import pygame
from pygame.locals import *
from globals import *
from player_health import Player_Health


class Enemy_Health(Player_Health):
    def __init__(self):
        super().__init__()
        self.max_health = MAX_ENEMY_HEALTH
        self.current_health = self.max_health
    
        