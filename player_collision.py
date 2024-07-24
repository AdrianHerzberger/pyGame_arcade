import pygame
from pygame.locals import *
from globals import *

class Player_Collision:
    def __init__(self, player):
        self.player = player
        self.offset_x = OFFSET_X
        self.offset_y = OFFSET_Y
        self.player_collision_rect = pygame.Rect(self.player.x_pos + self.offset_x, self.player.y_pos + self.offset_y, 60, 90)
        
    def draw(self, screen):
        self.player_collision_rect.topleft = (self.player.x_pos + self.offset_x, self.player.y_pos + self.offset_y)
        pygame.draw.rect(screen, (0, 255, 0), self.player_collision_rect, 2)
    
    def check_collisions(self, enemies):
        self.check_collisions_x(enemies)
        self.check_collisions_y(enemies)
    
    def get_hits(self, enemies):
        collisions = []
        for enemy in enemies:
            if self.player_collision_rect.colliderect(enemy.enemy_collision_rect):  
                collisions.append(enemy)
        print(f"Current collision status: {collisions}")
        return collisions

    def check_collisions_x(self, enemies):
        collisions = self.get_hits(enemies)
        for enemy in collisions:
            if self.player_collision_rect.right > enemy.enemy_collision_rect.left and self.player_collision_rect.left < enemy.enemy_collision_rect.right: 
                if self.player_collision_rect.centerx > enemy.enemy_collision_rect.centerx:  
                    self.player_collision_rect.left = enemy.enemy_collision_rect.right  
                else:
                    self.player_collision_rect.right = enemy.enemy_collision_rect.left  
        self.player.x_pos = self.player_collision_rect.x - self.offset_x

    def check_collisions_y(self, enemies):
        self.player.on_ground = False
        self.player_collision_rect.topleft = (self.player.x_pos + self.offset_x, self.player.y_pos + self.offset_y)
        print(f"Current y-pos: {self.player_collision_rect.y}")
        collisions = self.get_hits(enemies)
        print(f"Current collision status: {collisions}")
        for enemy in collisions:
            if self.player_collision_rect.bottom > enemy.enemy_collision_rect.top and self.player_collision_rect.top < enemy.enemy_collision_rect.bottom: 
                if self.player_collision_rect.centery > enemy.enemy_collision_rect.centery: 
                    self.player_collision_rect.top = enemy.enemy_collision_rect.bottom 
                    self.player.jump_force = 0
                else:
                    self.player_collision_rect.bottom = enemy.enemy_collision_rect.top  
                    self.player.on_ground = True
        self.player.y_pos = self.player_collision_rect.y - self.offset_y

