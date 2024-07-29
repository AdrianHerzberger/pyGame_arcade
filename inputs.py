import pygame
from pygame.locals import *

class GameInputs:
    def __init__(self, player):
        self.player = player
        self.scroll = 0
        self.key = None
        self.light_attack_start = None
        self.heavy_attack_start = None
        self.jump_start = None

    def get_key_presses(self):
        self.key = pygame.key.get_pressed()
        return self.key

    def move_left_right(self):
        if self.player.is_dead:
            return self.scroll 
        self.key = self.get_key_presses()
        if self.key[pygame.K_LEFT] and self.scroll > 0:
            self.scroll -= 5
        if self.key[pygame.K_RIGHT] and self.scroll < 3000:
            self.scroll += 5
        return self.scroll
    
    def is_jumping(self):
        if self.player.is_dead:
            return False
        self.key = self.get_key_presses()
        current_time = pygame.time.get_ticks()
        if self.key[pygame.K_SPACE]:
            if self.jump_start is None:
                self.jump_start = current_time
                return self.player.on_ground
            elif current_time - self.jump_start > 1000:
                self.jump_start = current_time
                return self.player.on_ground
        else:
            self.jump_start = None
        return False
    
    def is_attacking_light(self):
        if self.player.is_dead:
            return False
        self.key = self.get_key_presses()
        current_time = pygame.time.get_ticks()
        if self.key[pygame.K_COMMA]:
            if self.light_attack_start is None:
                self.light_attack_start = pygame.time.get_ticks()
            elif current_time - self.light_attack_start > 500:  
                return True
        else:
            self.light_attack_start = None
        return False
    
    def is_attacking_heavy(self):
        if self.player.is_dead:
            return False
        self.key = self.get_key_presses()
        current_time = pygame.time.get_ticks()
        if self.key[pygame.K_PERIOD]:
            if self.heavy_attack_start is None:
                self.heavy_attack_start = pygame.time.get_ticks()
            elif current_time - self.heavy_attack_start > 500:  
                return True
        else:
            self.heavy_attack_start = None
        return False

    def is_running(self):
        self.key = self.get_key_presses()
        return self.key[pygame.K_LEFT] or self.key[pygame.K_RIGHT]
