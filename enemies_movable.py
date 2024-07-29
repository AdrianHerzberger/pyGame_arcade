import pygame
import random
from globals import *
from enemy_movable_animations import Enemy_Movable_Animations
from player import Player
from inputs import GameInputs


class Enemy_Movable:
    def __init__(self, x, y):
        self.facing_left = False
        self.is_dead = False
        self.enm_x_pos = x
        self.enm_y_pos = y
        self.enm_range_min = random.randint(0, SCREEN_WIDTH // 2)
        self.enm_range_max = random.randint(SCREEN_WIDTH // 2, SCREEN_WIDTH * 3)
        self.speed = 1
        self.direction = 1
        self.scale_factor = 0.8
        self.original_size = (128, 128)
        self.scaled_size = (
            int(self.original_size[0] * self.scale_factor),
            int(self.original_size[1] * self.scale_factor),
        )
        self.enemy_collision_rect = pygame.Rect(self.enm_x_pos, self.enm_y_pos, 60, 70)
        self.enemy_animations = Enemy_Movable_Animations()
        self.player_kill = Player(self)

    def update(self):
        if self.player_kill.enemy_health.current_health == 0:
            self.is_dead = True
            #print(f"Status enemy dead flag: {self.is_dead}")
            
        if not self.is_dead:
            self.enm_x_pos += self.speed * self.direction
            self.enemy_collision_rect.topleft = (self.enm_x_pos, self.enm_y_pos)
            if self.enm_x_pos > self.enm_range_max:
                self.enm_x_pos = self.enm_range_max
                self.direction *= -1
                self.facing_left = True
            elif self.enm_x_pos < self.enm_range_min:
                self.enm_x_pos = self.enm_range_min
                self.direction *= -1
                self.facing_left = False

            #print(f"Enemy updated position: {self.enm_x_pos}, {self.enm_y_pos}")

    def draw(self, screen, scroll):
        if self.is_dead:
            animation = self.enemy_animations.get_current_dead_animation()
            animation = pygame.transform.scale(animation, self.scaled_size)
            if self.facing_left:
                animation = pygame.transform.flip(animation, True, False)
            screen.blit(animation, (self.enm_x_pos - scroll, self.enm_y_pos))
        else:
            adjust_x_pos = self.enm_x_pos - scroll
            pygame.draw.rect(
                screen,
                (0, 255, 0),
                pygame.Rect(
                    adjust_x_pos + 20,
                    self.enm_y_pos + 40,
                    self.enemy_collision_rect.width,
                    self.enemy_collision_rect.height,
                ),
                2,
            )
            animation = self.enemy_animations.get_current_walking_animation()
            animation = pygame.transform.scale(animation, self.scaled_size)
            if self.facing_left:
                animation = pygame.transform.flip(animation, True, False)
            screen.blit(animation, (self.enm_x_pos - scroll, self.enm_y_pos))
            

    @classmethod
    def create_enemies(cls):
        return [
            cls(random.randint(0, SCREEN_WIDTH), ENEMY_Y_POS),
            cls(random.randint(0, SCREEN_WIDTH), ENEMY_Y_POS),
            cls(random.randint(0, SCREEN_WIDTH), ENEMY_Y_POS),
        ]

    @staticmethod
    def draw_enemies(screen, enemies, scroll):
        for enemy in enemies:
            enemy.update()
            enemy.draw(screen, scroll)
