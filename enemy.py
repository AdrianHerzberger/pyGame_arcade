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
        self.scale_factor = 0.8  
        self.original_size = (128, 128)
        self.scaled_size = (int(self.original_size[0] * self.scale_factor), int(self.original_size[1] * self.scale_factor))
        self.rect = pygame.Rect(x, y, *self.scaled_size)
        self.enemy_animations = Enemy_Animations()

    def draw(self, screen, camera):
        animation = self.enemy_animations.get_current_walking_animation()
        scaled_animation = pygame.transform.scale(animation, self.scaled_size)
        if self.facing_left:
            scaled_animation = pygame.transform.flip(scaled_animation, True, False)
        screen.blit(scaled_animation, camera.apply(self.rect.topleft))

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
    def draw_all(screen, enemies, camera):
        for enemy in enemies:
            enemy.update()
            enemy.draw(screen, camera)