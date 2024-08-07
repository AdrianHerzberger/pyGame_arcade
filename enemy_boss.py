import pygame
import random
from pygame.locals import *
from globals import * 
from enemies_movable import Enemy_Movable
from enemy_boss_animations import Enemy_Boss_Animations
from boss_health import Boss_Health
from player import Player

class Enemy_Boss(Enemy_Movable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.is_attacking = False
        self.enemy_boss_animations = Enemy_Boss_Animations()
        self.enm_range_min = x - random.randint(200, 300)
        self.enm_range_max = x + random.randint(300, 500)
        self.last_attack_light_time = pygame.time.get_ticks()
        self.last_attack_heavy_time = pygame.time.get_ticks()
        self.attack_light_interval = 5000
        self.attack_heavy_interval = 8000
        self.attack_duration = 2000
        self.scale_factor = 1.5
        self.original_size = (128, 128)
        self.scaled_size = (
            int(self.original_size[0] * self.scale_factor),
            int(self.original_size[1] * self.scale_factor),
        )
        self.enemy_collision_rect = pygame.Rect(self.enm_x_pos, self.enm_y_pos, 80, 120)
        self.boss_health = Boss_Health()
        self.player = Player(self)

    def update(self):
        current_time = pygame.time.get_ticks()
        if self.boss_health.current_health == 0:
            self.is_dead = True
        if not self.is_dead:
            if not self.is_attacking and current_time - self.last_attack_light_time > self.attack_light_interval:
                self.last_attack_light_time = current_time
                self.is_attacking = True
                self.attack_type = 'light'
            
            if not self.is_attacking and current_time - self.last_attack_heavy_time > self.attack_heavy_interval:
                self.last_attack_heavy_time = current_time
                self.is_attacking = True
                self.attack_type = 'heavy'
            
            if self.is_attacking:
                attack_start_time = self.last_attack_light_time if self.attack_type == 'light' else self.last_attack_heavy_time
                if current_time - attack_start_time > self.attack_duration:
                    self.is_attacking = False
                    self.attack_type = None 
                
                if self.attack_type == 'light':
                    pass 
            else:
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
                    

    def draw(self, screen, scroll):
        if self.is_dead:
            animation = self.enemy_boss_animations.get_current_dead_animation()
        elif self.is_attacking:
            if self.attack_type == 'light':
                animation = self.enemy_boss_animations.get_current_attack_light_animation()
                if self.player.is_hit:
                    current_player_health = self.player.player_health.taking_damage(BOSS_DAMGE_LIGHT)
            elif self.attack_type == 'heavy':
                animation = self.enemy_boss_animations.get_current_attack_heavy_animation()
                if self.player.is_hit:
                    current_player_health = self.player.player_health.taking_damage(BOSS_DAMAGE_HEAVY)
        else:
            animation = self.enemy_boss_animations.get_current_walking_animation()

        if self.facing_left:
            animation = pygame.transform.flip(animation, True, False)

        animation = pygame.transform.scale(animation, self.scaled_size)
        screen.blit(animation, (self.enm_x_pos - scroll, self.enm_y_pos))

        if not self.is_dead:
            adjust_x_pos = self.enm_x_pos - scroll
            pygame.draw.rect(
                screen,
                (0, 255, 0),
                pygame.Rect(
                    adjust_x_pos + 50,
                    self.enm_y_pos + 80,
                    self.enemy_collision_rect.width,
                    self.enemy_collision_rect.height,
                ),
                2,
            )

    @classmethod
    def create_enemy_boss(cls):
        return [cls(BOSS_X_POS, BOSS_Y_POS)]

    @staticmethod
    def draw_boss(screen, boss, scroll):
        for b in boss:
            b.update()
            b.draw(screen, scroll)
