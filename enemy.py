import pygame
import random
from globals import *
from enemy_animations import Enemy_Animations


class Enemy:
    def __init__(self, x, y):
        self.facing_left = False
        self.enm_x_pos = ENEMY_X_POS
        self.enm_y_pos = ENEMY_Y_POS
        self.enm_range_min = random.randint(0, SCREEN_WIDTH // 2)
        self.enm_range_max = random.randint(SCREEN_WIDTH // 2, SCREEN_WIDTH)
        self.speed = 1
        self.direction = 1
        self.rect = pygame.Rect(x, y, 128, 128)
        self.enemy_animations = Enemy_Animations()

    def draw(self, screen):
        animation = self.enemy_animations.get_current_walking_animation()
        if self.facing_left:
            animation = pygame.transform.flip(animation, True, False)
        screen.blit(animation, self.rect.topleft)

    @classmethod
    def create_enemies(enm):
        return [
            enm(random.randint(0, SCREEN_WIDTH), ENEMY_Y_POS),
            enm(random.randint(0, SCREEN_WIDTH), ENEMY_Y_POS),
            enm(random.randint(0, SCREEN_WIDTH), ENEMY_Y_POS),
        ]

    def update(self):
        self.enm_x_pos += self.speed * self.direction

        if self.enm_x_pos > self.enm_range_max:
            self.enm_x_pos = self.enm_range_max
            self.direction *= -1
            self.facing_left = True
        elif self.enm_x_pos < self.enm_range_min:
            self.enm_x_pos = self.enm_range_min
            self.direction *= -1
            self.facing_left = False

        self.rect.x = self.enm_x_pos

    @staticmethod
    def draw_all(screen, enemies):
        for enemy in enemies:
            enemy.update()
            enemy.draw(screen)