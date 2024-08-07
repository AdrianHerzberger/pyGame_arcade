import pygame
from pygame.locals import *


class Enemy_Movable_Animations:
    def __init__(self):
        self.enemy_movable_walk_sheet = pygame.image.load("assets/enemy/movable/walk.png")
        self.enemy_movable_dead_sheet = pygame.image.load("assets/enemy/movable/dead.png")
        
        self.walking_animation = []
        self.dead_animation = []

        self.walking_aniamtion_steps = 8
        self.dead_animation_steps = 3
        
        self.max_steps = max(
            self.walking_aniamtion_steps,
            self.dead_animation_steps
        )
        
        self.current_animation_steps = 8
        self.current_frame = 0
        self.base_animation_delay = 800
        self.last_update_time = pygame.time.get_ticks()

        self.frame_width = 128
        self.frame_height = 128
        
        self.dead_animation_finished = False 
        
        self.load_walking_animation() 
        self.load_dead_animation()
        
    def set_current_animation(self, steps):
        if self.current_animation_steps != steps:
            self.current_frame = 0  
        self.current_animation_steps = steps    
        self.animation_delay = self.base_animation_delay / self.max_steps
        
        
    def load_walking_animation(self):
        for frame in range(self.walking_aniamtion_steps):
            walking_sprite = pygame.Surface(
                (self.frame_width, self.frame_height), pygame.SRCALPHA
            )
            walking_sprite.blit(
                self.enemy_movable_walk_sheet, 
                (0, 0),
                (frame * self.frame_width, 0, self.frame_width, self.frame_height)
            )
            self.walking_animation.append(walking_sprite)
            
    def load_dead_animation(self):
        for frame in range(self.dead_animation_steps):
            dead_sprite = pygame.Surface(
                (self.frame_width, self.frame_height), pygame.SRCALPHA
            )
            dead_sprite.blit(
                self.enemy_movable_dead_sheet, 
                (0, 0),
                (frame * self.frame_width, 0, self.frame_width, self.frame_height)
            )
            self.dead_animation.append(dead_sprite)
            
        
    def get_current_walking_animation(self):
        self.set_current_animation(self.walking_aniamtion_steps)
        self.update_animation()
        return self.walking_animation[self.current_frame]
    
    
    def get_current_dead_animation(self):
        if not self.dead_animation_finished:
            self.set_current_animation(self.dead_animation_steps)
            self.update_animation()
            if self.current_frame == self.dead_animation_steps - 1:
                self.dead_animation_finished = True 
            return self.dead_animation[self.current_frame]
        else:
            return self.get_dead_static_frame()
        
    def get_dead_static_frame(self):
        return self.dead_animation[-1]
    
    
    def update_animation(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update_time > self.animation_delay:
            self.current_frame = (self.current_frame + 1) % self.current_animation_steps
            self.last_update_time = current_time
            

            



        

