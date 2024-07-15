import pygame
from pygame.locals import *


class Health_Bar_Animation:
    def __init__(self, screen):
        self.screen = screen
        self.health_bar = [
            "meter_icon_holder_red",
            "health_icon",
            "meter_bar_holder_left_edge_red",
            "meter_bar_holder_center-repeating_red_1",
            "meter_bar_holder_center-repeating_red_2",
            "meter_bar_holder_right_edge_red",
            "meter_bar_center-repeating_red",
            "meter_bar_left_edge_red",
            "meter_bar_right_edge_red",
        ]

        self.images_health_bar = self.load_health_bar(25, 15)
        self.health_bar_positions = self.define_health_bar_positions()

    def load_health_bar(self, width, height):
        imgs = {}
        for name in self.health_bar:
            img = pygame.image.load(
                f"assets/character/health_bar/{name}.png"
            ).convert_alpha()
            if name == "health_icon":
                scaled_image = self.scaled_image(img, 15, 15) 
            elif name == "meter_bar_center-repeating_red":
                scaled_image = self.scaled_image(img, 50, 25)
            else:
                scaled_image = self.scaled_image(img, 25, 25) 
            imgs[name] = scaled_image
        return imgs

    def scaled_image(self, img, width, height):
        return pygame.transform.scale(img, (width, height))

    def define_health_bar_positions(self):
        positions = {
            "meter_icon_holder_red": (25, 25),
            "health_icon": (30, 30),
            "meter_bar_holder_left_edge_red": (50, 25),
            "meter_bar_holder_center-repeating_red_1": (75, 25),
            "meter_bar_holder_center-repeating_red_2": (100, 25),
            "meter_bar_holder_right_edge_red": (125, 25),
            "meter_bar_center-repeating_red":(75, 25),
            "meter_bar_left_edge_red": (50, 25),
            "meter_bar_right_edge_red": (125, 25),
        }
        return positions

    def draw_health_bar(self):
        for name in self.health_bar:
            img = self.images_health_bar[name]
            pos = self.health_bar_positions[name]
            self.screen.blit(img, pos)
