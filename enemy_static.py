import pygame
import random
from enemies_movable import Enemy_Movable
from enemy_static_animations import Enemy_Static_Animations
from player import Player
from globals import *


class Enemy_Static(Enemy_Movable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.enemy_animations = Enemy_Static_Animations()
        self.player_kill = Player(self)

        
    def update(self):
        if self.player_kill.enemy_health.current_health == 0:
            self.is_dead = True
            
        if not self.is_dead:
            self.enemy_collision_rect.topleft = (self.enm_x_pos, self.enm_y_pos)
            if self.enm_x_pos > self.enm_range_max:
                self.enm_x_pos = self.enm_range_max
            elif self.enm_x_pos < self.enm_range_min:
                self.enm_x_pos = self.enm_range_min
                
                
    def draw(self, screen, scroll):
        if self.is_dead:
            animation = self.enemy_animations.get_current_dead_animation()
            animation = pygame.transform.scale(animation, self.scaled_size)
        else:
            animation = self.enemy_animations.get_current_idle_animation()
            animation = pygame.transform.scale(animation, self.scaled_size)

        screen.blit(animation, (self.enm_x_pos - scroll, self.enm_y_pos))

        pygame.draw.rect(
            screen,
            (0, 255, 0),
            pygame.Rect(
                self.enm_x_pos - scroll + 20,
                self.enm_y_pos + 40,
                self.enemy_collision_rect.width,
                self.enemy_collision_rect.height,
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
        