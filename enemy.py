import pygame
from globals import *

class Enemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), self.rect)

    @classmethod
    def create_enemies(enm):
        return [
            enm(ENEMY_X_POS, ENEMY_Y_POS),
            enm(ENEMY_X_POS, ENEMY_Y_POS),
            enm(ENEMY_X_POS, ENEMY_Y_POS),
        ]

    @staticmethod
    def draw_all(screen, enemies):
        for enemy in enemies:
            enemy.draw(screen)
