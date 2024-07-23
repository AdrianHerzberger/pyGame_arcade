import pygame
from pygame.locals import *

class Camera:
    def __init__(self, screen_width, screen_height):
        self.offest_x = 0
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        
    def update(self, target_x):
        self.offset_x = target_x - self.screen_width // 2
        
        
    def apply(self, pos):
        return pos[0] - self.offest_x, pos[1]
    