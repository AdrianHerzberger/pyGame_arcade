import pygame
import random
from pygame.locals import *
from globals import * 
from enemies_movable import Enemy_Movable
from enemy_boss_animations import Enemy_Boss_Animations
from boss_health import Boss_Health

class Enemy_Boss(Enemy_Movable):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.enemy_boss_animations = Enemy_Boss_Animations()
        self.enm_range_min = random.randint(200, SCREEN_WIDTH // 2)
        self.enm_range_max = random.randint(SCREEN_WIDTH // 2, SCREEN_WIDTH * 2)
        self.last_attack_time = pygame.time.get_ticks()
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

    def update(self):
        if self.boss_health.current_health == 0:
            self.is_dead = True
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

    def draw(self, screen, scroll):
        current_time = pygame.time.get_ticks()
        if self.is_dead:
            animation = self.enemy_boss_animations.get_current_dead_animation()
        elif current_time - self.last_attack_time < self.attack_duration:
            animation = self.enemy_boss_animations.get_current_attack_light_animation()
        elif current_time - self.last_attack_time > self.attack_light_interval:
            self.last_attack_time = current_time
            animation = self.enemy_boss_animations.get_current_attack_light_animation()
        elif current_time - self.last_attack_time > self.attack_heavy_interval:
            self.last_attack_time = current_time
            animation = self.enemy_boss_animations.get_current_attack_heavy_animation()
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
        return [cls(random.randint(0, BOSS_X_POS), BOSS_Y_POS)]

    @staticmethod
    def draw_boss(screen, boss, scroll):
        for b in boss:
            b.update()
            b.draw(screen, scroll)
