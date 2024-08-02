import pygame
import random
from enemies_movable import Enemy_Movable
from enemy_static_animations import Enemy_Static_Animations
from globals import *


class Enemy_Static(Enemy_Movable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.enemy_animations = Enemy_Static_Animations()
        self.last_updated_time = pygame.time.get_ticks()
        self.last_attack_time = pygame.time.get_ticks()
        self.attack_interval = 5000 
        self.attack_duration = 2000
        self.scale_factor = 0.6
        self.original_size = (128, 128)
        self.scaled_size = (
            int(self.original_size[0] * self.scale_factor),
            int(self.original_size[1] * self.scale_factor),
        )
        self.enemy_collision_rect = pygame.Rect(self.enm_x_pos, self.enm_y_pos, 60, 100)

        
    def update(self):
        if self.enemy_health.current_health == 0:
            self.is_dead = True
            
        if not self.is_dead:
            self.enemy_collision_rect.topleft = (self.enm_x_pos, self.enm_y_pos)
            if self.enm_x_pos > self.enm_range_max:
                self.enm_x_pos = self.enm_range_max
            elif self.enm_x_pos < self.enm_range_min:
                self.enm_x_pos = self.enm_range_min
                
                
    def draw(self, screen, scroll):
        current_time = pygame.time.get_ticks()
        if self.is_dead:
            animation = self.enemy_animations.get_current_dead_animation()
        elif current_time - self.last_attack_time > self.attack_interval:
            animation = self.enemy_animations.get_current_static_attack_animation()
            self.last_attack_time = current_time
            self.last_updated_time = current_time  
        elif current_time - self.last_updated_time < self.attack_duration:
            animation = self.enemy_animations.get_current_static_attack_animation()
        elif current_time > self.last_updated_time:
            animation = self.enemy_animations.get_current_idle_animation()
        else:
            animation = self.enemy_animations.get_current_idle_animation()
            animation = pygame.transform.scale(animation, self.scaled_size)

        screen.blit(animation, (self.enm_x_pos - scroll, self.enm_y_pos))

        if not self.is_dead: 
            pygame.draw.rect(
                screen,
                (0, 255, 0),
                pygame.Rect(
                    self.enm_x_pos - scroll + 32,
                    self.enm_y_pos + 40,
                    self.enemy_collision_rect.width,
                    self.enemy_collision_rect.height,
                ),
                2,
            )
        
    @classmethod
    def create_enemies(cls):
        return [
            cls(random.randint(0, SCREEN_WIDTH), ENEMY_Y_POS - 30),
            cls(random.randint(0, SCREEN_WIDTH), ENEMY_Y_POS - 30),
            cls(random.randint(0, SCREEN_WIDTH), ENEMY_Y_POS - 30),
        ]


    @staticmethod
    def draw_enemies(screen, enemies, scroll):
        for enemy in enemies:
            enemy.update()
            enemy.draw(screen, scroll)
        