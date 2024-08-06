import pygame
import math
from pygame.locals import *
from globals import *
from inputs import GameInputs


class World:
    def __init__(self, screen, inputs):
        self.screen = screen
        self.inputs = inputs
        self.mountain = ["sky", "sky_far", "rock", "grass_far", "grass"]
        self.meadow = ["sky", "sky_far", "grass_far", "grass"]
        self.images_mountain = self.load_mountain()
        self.images_meadow = self.load_meadow()

    def load_mountain(self):
        imgs = {}
        for name in self.mountain:
            img = pygame.image.load(f"assets/terrain/mountain/{name}.png").convert_alpha()
            if name in ["sky", "rock", "grass_far", "grass"]:
                img = pygame.transform.scale(img, (img.get_width(), img.get_height() * 2))
            imgs[name] = img
        return imgs

    def load_meadow(self):
        imgs = {}
        for name in self.meadow:
            img = pygame.image.load(f"assets/terrain/meadow/{name}.png").convert_alpha()
            if name in ["sky", "grass_far", "grass"]:
                img = pygame.transform.scale(img, (img.get_width(), img.get_height() * 2))
            imgs[name] = img
        return imgs

    def draw_mountain(self, scroll, start_position):
        for name in self.mountain:
            img = self.images_mountain[name]
            bg_width = img.get_width()
            bg_height = img.get_height()
            tiles = math.ceil(SCREEN_WIDTH / bg_width)

            for i in range(tiles):
                x_position = (start_position - (i * bg_width + bg_width) - scroll)

                if x_position < -bg_width:
                    continue
                self.screen.blit(img, (x_position, 0))

    def draw_meadow(self, scroll):
        for name in self.meadow:
            img = self.images_meadow[name]
            bg_width = img.get_width()
            bg_height = img.get_height()
            tiles = math.ceil(SCREEN_WIDTH / bg_width)

            for l in range(tiles):
                x_position = (l * bg_width) - scroll
                self.screen.blit(img, (x_position, 0))

    def draw_world(self, scroll):
        meadow_width = self.images_meadow[self.meadow[0]].get_width() * len(self.meadow)
        if scroll <= 100:
            self.draw_meadow(scroll)
        else:
            self.draw_meadow(scroll)
            start_position = meadow_width
            self.draw_mountain(scroll, start_position)

