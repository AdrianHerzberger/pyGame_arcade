import pygame
from pygame.locals import *
from character_animations import Character_Animation


class Enemy_Animations(Character_Animation):
    def __init__(self):
        super().__init__()
        self.enemy_idle_sheet = pygame.image.load("assets/enemy/idle.png")
        self.enemy_walk_sheet = pygame.image.load("assets/enemy/walk.png")
        self.enemy_attack_light_sheet = pygame.image.load("assets/enemy/attack_light.png")
        self.enemy_hurt_sheet = pygame.image.load("assets/enemy/hurt.png")
        self.enemy_dead_sheet = pygame.image.load("assets/enemy/dead.png")

        self.idle_animation = []
        self.walking_animation = []
        self.attack_light_animation = []
        self.hurt_animation = []
        self.enemy_dead_animation = []

        self.idle_animation_steps = 7
        self.walking_aniamtion_steps = 8
        self.attack_light_animation_steps = 4
        self.hurt_animations_steps = 3
        self.dead_animations_steps = 3
        
        self.max_steps = max(
            self.idle_animation_steps,
            self.walking_aniamtion_steps,
            self.attack_light_animation_steps,
            self.hurt_animations_steps,
            self.dead_animations_steps
        )
        
        self.current_animation_steps = 8
        self.current_frame = 0
        self.base_animation_delay = 800
        self.last_update_time = pygame.time.get_ticks()

        self.frame_width = 128
        self.frame_height = 128
        
        self.idle_animation = self.load_animation(self.enemy_idle_sheet, self.idle_animation_steps)
        self.attack_light_animation = self.load_animation(self.enemy_attack_light_sheet, self.attack_light_animation_steps)
        self.hurt_animation = self.load_animation(self.enemy_hurt_sheet, self.hurt_animations_steps)
        self.dead_animation = self.load_animation(self.enemy_dead_sheet, self.dead_animations_steps)
        self.load_walking_animation() 
        
        
    def load_walking_animation(self):
        for frame in range(self.walking_aniamtion_steps):
            walking_sprite = pygame.Surface(
                (self.frame_width, self.frame_height), pygame.SRCALPHA
            )
            walking_sprite.blit(
                self.enemy_walk_sheet, 
                (0, 0),
                (frame * self.frame_width, 0, self.frame_width, self.frame_height)
            )
            self.walking_animation.append(walking_sprite)
            
        
    def get_current_walking_animation(self):
        self.set_current_animation(self.walking_aniamtion_steps)
        self.update_animation()
        return self.walking_animation[self.current_frame]
            
        
    def load_animation(self, sheet, steps):
        animation = []
        for frame in range(steps):
            sprite = pygame.Surface((self.frame_width, self.frame_height), pygame.SRCALPHA)
            sprite.blit(sheet, (0, 0), (frame * self.frame_width, 0, self.frame_width, self.frame_height))
            animation.append(sprite)
        return animation
    


        

