import pygame
import random
from enemies_movable import Enemy_Movable
from enemy_static_animations import Enemy_Static_Animations
from player import Player
from globals import *


class Enemy_Static:
    def __init__(self, x, y):
        self.enemy_instance = Enemy_Movable(x, y)
        self.enemy_animations = Enemy_Static_Animations()
        self.player_kill = Player(self)

        
    def update(self):
        if self.player_kill.enemy_health.current_health == 0:
            self.enemy_instance.is_dead = True
            
        if not self.enemy_instance.is_dead:
            self.enemy_instance.enemy_collision_rect.topleft = (self.enemy_instance.enm_x_pos, self.enemy_instance.enm_y_pos)
            if self.enemy_instance.enm_x_pos > self.enemy_instance.enm_range_max:
                self.enemy_instance.enm_x_pos = self.enemy_instance.enm_range_max
            elif self.enemy_instance.enm_x_pos < self.enemy_instance.enm_range_min:
                self.enemy_instance.enm_x_pos = self.enemy_instance.enm_range_min
                
                
    def draw(self, screen, scroll):
        if self.enemy_instance.is_dead:
            animation = self.enemy_animations.get_current_dead_animation()
            animation = pygame.transform.scale(animation, self.enemy_instance.scaled_size)
        else:
            animation = self.enemy_animations.get_current_idle_animation()
            animation = pygame.transform.scale(animation, self.enemy_instance.scaled_size)

        screen.blit(animation, (self.enemy_instance.enm_x_pos - scroll, self.enemy_instance.enm_y_pos))

        pygame.draw.rect(
            screen,
            (0, 255, 0),
            pygame.Rect(
                self.enemy_instance.enm_x_pos - scroll + 20,
                self.enemy_instance.enm_y_pos + 40,
                self.enemy_instance.enemy_collision_rect.width,
                self.enemy_instance.enemy_collision_rect.height,
            ),
            2,
        )
        
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
        