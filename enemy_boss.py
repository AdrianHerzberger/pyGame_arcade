import pygame
from pygame.locals import *
from enemies_movable import Enemy_Movable

class Enemey_Boos(Enemy_Movable):
    def __init__(self, x, y):
        super().__init__(x, y)
        
    