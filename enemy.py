import pygame
import random
from globals import *

class Enemy:
    def __init__(self, x, y):
        self.enm_x_pos = ENEMY_X_POS
        self.enm_y_pos = ENEMY_Y_POS
        self.enm_range_min = random.randint(0, SCREEN_WIDTH // 2)   
        self.enm_range_max = random.randint(SCREEN_WIDTH // 2, SCREEN_WIDTH)
        self.speed = 2
        self.direction = 1
        self.rect = pygame.Rect(x, y, 50, 50)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), self.rect)

    @classmethod
    def create_enemies(cls):
        return [
            cls(random.randint(0, SCREEN_WIDTH), ENEMY_Y_POS),
            cls(random.randint(0, SCREEN_WIDTH), ENEMY_Y_POS),
            cls(random.randint(0, SCREEN_WIDTH), ENEMY_Y_POS),
        ]
        
    def update(self):
        self.enm_x_pos += self.speed * self.direction
        
        if self.enm_x_pos > self.enm_range_max:
            self.enm_x_pos = self.enm_range_max
            self.direction *= -1
        elif self.enm_x_pos < self.enm_range_min:
            self.enm_x_pos = self.enm_range_min
            self.direction *= -1
            
        self.rect.x = self.enm_x_pos
        
        
    @staticmethod
    def draw_all(screen, enemies):
        for enemy in enemies:
            enemy.update()
            enemy.draw(screen)
