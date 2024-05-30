import pygame
import math
from pygame.locals import *
from globals import *

class World:
    def __init__(self, screen):
        self.screen = screen
        self.mountain = ["sky", "rocks"] 
        self.meadow = ["sky", "sky_far", "grass", "grass_far"]
        self.images_mountain = self.load_mountain()
        self.images_meadow = self.load_meadow()

    def load_mountain(self):
        imgs = {}
        for name in self.mountain:
            imgs[name] = pygame.image.load(f"assets/terrain/mountain/{name}.png").convert_alpha()  
        return imgs
    
    def load_meadow(self):
        imgs = {}
        for name in self.meadow:
            imgs[name] = pygame.image.load(f"assets/terrain/meadow/{name}.png").convert_alpha()
        return imgs
            
    def draw_mountain(self):
        for name in self.mountain:
            img = self.images_mountain[name]
            bg_width = img.get_width()
            bg_height = img.get_height()
            tiles = math.ceil(SCREEN_WIDTH / bg_width)
        
            for i in range(tiles):
                self.screen.blit(img, (i * bg_width, 0))


    def draw_meadow(self):
        for name in self.meadow:
            img = self.images_meadow[name]
            bg_width = 
            
        