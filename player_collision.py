import pygame
from pygame.locals import *
from globals import *

class Player_Collision:
    def __init__(self, player):
        self.player = player
        self.collision_rect = pygame.Rect(self.player.y_pos, CHAR_X_POS, 128, 128)
    
    def check_collisions(self, enemies):
        self.check_collisions_x(enemies)
        self.check_collisions_y(enemies)
    
    def get_hits(self, enemies):
        collisions = []
        for enemy in enemies:
            if self.collision_rect.colliderect(enemy.rect):
                collisions.append(enemy)
        return collisions
    
    def check_collisions_x(self, enemies):
        collisions = self.get_hits(enemies)
        for enemy in collisions:
            if self.collision_rect.right > enemy.rect.left and self.collision_rect.left < enemy.rect.right:
                if self.collision_rect.centerx > enemy.rect.centerx:
                    self.collision_rect.left = enemy.rect.right
                else:
                    self.collision_rect.right = enemy.rect.left
    
    def check_collisions_y(self, enemies):
        self.player.on_ground = False
        self.collision_rect.y = self.player.y_pos 
        collisions = self.get_hits(enemies)
        for enemy in collisions:
            if self.collision_rect.bottom > enemy.rect.top and self.collision_rect.top < enemy.rect.bottom:
                if self.collision_rect.centery > enemy.rect.centery:
                    self.collision_rect.top = enemy.rect.bottom
                    self.player.jump_force = 0
                else:
                    self.collision_rect.bottom = enemy.rect.top
                    self.player.on_ground = True
        self.player.y_pos = self.collision_rect.y
