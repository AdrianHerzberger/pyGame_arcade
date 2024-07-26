import pygame
import random
from pygame.locals import *
from globals import *
from player import Player


class Collectables:
    def __init__(self, x, y):
        self.heath_bottle_sheet = pygame.image.load("assets/collectables/health.png")

        self.bottle_x_pos = x
        self.bottle_y_pos = y

        self.frame_width = 32
        self.frame_height = 32

        self.bottle_min_range = random.randint(0, SCREEN_WIDTH // 2)
        self.bottle_max_range = random.randint(SCREEN_WIDTH // 2, SCREEN_WIDTH)

        self.is_bottle_collected = False

        self.bottle_collision_rect = pygame.Rect(
            self.bottle_x_pos, self.bottle_y_pos, 32, 32
        )
        self.player_collects = Player(self)

    def update(self):
        self.bottle_collision_rect.topleft = (self.bottle_x_pos, self.bottle_y_pos)
        if self.bottle_x_pos > self.bottle_max_range:
            self.bottle_x_pos = self.bottle_max_range
        elif self.bottle_x_pos < self.bottle_min_range:
            self.bottle_x_pos = self.bottle_min_range

    def draw(self, screen, scroll):
        health_bottle_sprite = pygame.Surface(
            (self.frame_width, self.frame_height), pygame.SRCALPHA
        )
        health_bottle_sprite.blit(
            self.heath_bottle_sheet,
            (0, 0),
            (0, 0, self.frame_width, self.frame_height),
        )

        adjust_x_pos = self.bottle_x_pos - scroll
        pygame.draw.rect(
            screen,
            (0, 200, 0),
            pygame.Rect(
                adjust_x_pos,
                self.bottle_y_pos,
                self.bottle_collision_rect.width,
                self.bottle_collision_rect.height,
            ),
            2,
        )

        screen.blit(health_bottle_sprite, (adjust_x_pos, self.bottle_y_pos))

    @classmethod
    def create_bottles(cls):
        return [
            cls(random.randint(0, SCREEN_WIDTH), BOTTLE_Y_POS),
            cls(random.randint(0, SCREEN_WIDTH), BOTTLE_Y_POS),
            cls(random.randint(0, SCREEN_WIDTH), BOTTLE_Y_POS),
        ]

    @staticmethod
    def draw_health_bottles(screen, bottles, scroll):
        for bottle in bottles:
            bottle.update()
            bottle.draw(screen, scroll)
