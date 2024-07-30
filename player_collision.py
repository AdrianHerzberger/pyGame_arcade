import pygame
from pygame.locals import *
from globals import *

class Player_Collision:
    def __init__(self, player):
        self.player = player
        self.offset_x = OFFSET_X
        self.offset_y = OFFSET_Y
        self.player_collision_rect = pygame.Rect(self.player.x_pos + self.offset_x, self.player.y_pos + self.offset_y, 60, 90)
        self.attack_collision_rect = pygame.Rect(self.player.x_pos + self.offset_x, self.player.y_pos + self.offset_y, 75, 25)
        
    def draw(self, screen):
        self.player_collision_rect.topleft = (self.player.x_pos + self.offset_x, self.player.y_pos + self.offset_y)
        pygame.draw.rect(screen, (0, 255, 0), self.player_collision_rect, 2)
        
    def draw_attack_collision_rect(self, screen):
        if self.player.facing_left:
            self.attack_collision_rect.topleft = (self.player.x_pos - 10, self.player.y_pos + 80)
        else:
            self.attack_collision_rect.topleft = (self.player.x_pos + 70, self.player.y_pos + 80) 
        
        if self.player.attack_light:
            pygame.draw.rect(screen, (255, 0, 0), self.attack_collision_rect, 2)
            
        if self.player.attack_heavy:
            pygame.draw.rect(screen, (255, 0, 0), self.attack_collision_rect, 2)
    
    def check_collisions(self, enemies):
        self.check_collisions_x(enemies)
        self.check_collisions_y(enemies)
    
    def get_hits(self, enemies, scroll):
        collisions = []
        for enemy in enemies:
            enemy_rect = pygame.Rect(enemy.enm_x_pos - scroll, enemy.enm_y_pos, enemy.enemy_collision_rect.width, enemy.enemy_collision_rect.height)
            #print(f"Player Rect: {self.player_collision_rect}, Enemy Rect: {enemy_rect}")  
            if self.player_collision_rect.colliderect(enemy_rect):  
                collisions.append(enemy)
        #print(f"Current collision status: {collisions}")
        return collisions
    
    def get_attack_hits(self, enemies, scroll):
        collisions = []
        for enemy in enemies:
            enemy_rect = pygame.Rect(enemy.enm_x_pos - scroll, enemy.enm_y_pos, enemy.enemy_collision_rect.width, enemy.enemy_collision_rect.height)
            if self.attack_collision_rect.colliderect(enemy_rect):  
                collisions.append(enemy)
        return collisions
    
    def get_bottle_hits(self, bottles, scroll):
        collisions = []
        for bottle in bottles:
            bottle_rect = pygame.Rect(bottle.bottle_x_pos - scroll, bottle.bottle_y_pos, bottle.bottle_collision_rect.width, bottle.bottle_collision_rect.height)
            if self.player_collision_rect.colliderect(bottle_rect):  
                collisions.append(bottle)
        return collisions
            
    def check_collisions_x(self, enemies, scroll):
        collisions = self.get_hits(enemies, scroll)
        for enemy in collisions:
            enemy_rect = pygame.Rect(enemy.enm_x_pos - scroll, enemy.enm_y_pos, enemy.enemy_collision_rect.width, enemy.enemy_collision_rect.height)
            if self.player_collision_rect.right > enemy_rect.left and self.player_collision_rect.left < enemy_rect.right:  
                if self.player_collision_rect.centerx > enemy_rect.centerx:  
                    self.player_collision_rect.left = enemy_rect.right  
                else:
                    self.player_collision_rect.right = enemy_rect.left 
        self.player.x_pos = self.player_collision_rect.x - self.offset_x + scroll

    def check_collisions_y(self, enemies, scroll):
        self.player.on_ground = False
        self.player_collision_rect.topleft = (self.player.x_pos + self.offset_x - scroll, self.player.y_pos + self.offset_y)
        #print(f"Current y-pos: {self.player_collision_rect.y}")
        collisions = self.get_hits(enemies, scroll)
        #print(f"Current collision status: {collisions}")
        for enemy in collisions:
            enemy_rect = pygame.Rect(enemy.enm_x_pos - scroll, enemy.enm_y_pos, enemy.enemy_collision_rect.width, enemy.enemy_collision_rect.height)
            if self.player_collision_rect.bottom > enemy_rect.top and self.player_collision_rect.top < enemy_rect.bottom:  
                if self.player_collision_rect.centery > enemy_rect.centery:  
                    self.player_collision_rect.top = enemy_rect.bottom  
                    self.player.jump_force = 0
                else:
                    self.player_collision_rect.bottom = enemy_rect.top  
                    self.player.on_ground = True
        self.player.y_pos = self.player_collision_rect.y - self.offset_y

