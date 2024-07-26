import pygame
from pygame.locals import *

class Character_Animation:
    def __init__(self):
        self.character_idle_sheet = pygame.image.load(
            "assets/character/player/idle.png"
        )
        self.character_running_sheet = pygame.image.load(
            "assets/character/player/run.png"
        )
        self.character_jumping_sheet = pygame.image.load(
            "assets/character/player/jump.png"
        )
        self.character_attack_light_sheet = pygame.image.load(
            "assets/character/player/attack_1.png"
        )
        self.character_attack_heavy_sheet = pygame.image.load(
            "assets/character/player/attack_2.png"
        )
        self.character_hurt_sheet = pygame.image.load(
            "assets/character/player/hurt.png"
        )
        
        self.character_dead_sheet = pygame.image.load(
            "assets/character/player/dead.png"
        )
    

        self.idle_animation = []
        self.running_animation = []
        self.jumping_animation = []
        self.attack_light_animation = []
        self.attack_heavy_animation = []
        self.hurt_animation = []
        self.dead_animation = []

        self.idle_animation_steps = 6
        self.running_animation_steps = 8
        self.jumping_animation_steps = 8
        self.attack_light_animation_steps = 5
        self.attack_heavy_animation_steps = 4
        self.hurt_animation_steps = 2
        self.dead_animation_steps = 4

        self.max_steps = max(
            self.idle_animation_steps,
            self.running_animation_steps,
            self.jumping_animation_steps,
            self.attack_light_animation_steps,
            self.attack_heavy_animation_steps,
            self.hurt_animation_steps,
            self.dead_animation_steps
        )
        
        self.current_animation_steps = 8
        self.current_frame = 0
        self.base_animation_delay = 800
        self.last_update_time = pygame.time.get_ticks()

        self.frame_width = 128
        self.frame_height = 128
        
        self.dead_animation_finished = False 

        self.load_idle_animation()
        self.load_running_animation()
        self.load_jumping_animation()
        self.load_attack_light_animation()
        self.load_attack_heavy_animation()
        self.load_hurt_animation()
        self.load_dead_animation()

    def load_idle_animation(self):
        for frame in range(self.idle_animation_steps):
            idle_sprite = pygame.Surface(
                (self.frame_width, self.frame_height), pygame.SRCALPHA
            )
            idle_sprite.blit(
                self.character_idle_sheet,
                (0, 0),
                (frame * self.frame_width, 0, self.frame_width, self.frame_height),
            )
            self.idle_animation.append(idle_sprite)

    def load_running_animation(self):
        for frame in range(self.running_animation_steps):
            running_sprite = pygame.Surface(
                (self.frame_width, self.frame_height), pygame.SRCALPHA
            )
            running_sprite.blit(
                self.character_running_sheet,
                (0, 0),
                (frame * self.frame_width, 0, self.frame_width, self.frame_height),
            )
            self.running_animation.append(running_sprite)

    def load_jumping_animation(self):
        for frame in range(self.jumping_animation_steps):
            jumping_sprite = pygame.Surface(
                (self.frame_width, self.frame_height), pygame.SRCALPHA
            )
            jumping_sprite.blit(
                self.character_jumping_sheet,
                (0, 0),
                (frame * self.frame_width, 0, self.frame_width, self.frame_height),
            )
            self.jumping_animation.append(jumping_sprite)

    def load_attack_light_animation(self):
        for frame in range(self.attack_light_animation_steps):
            attack_light_sprite = pygame.Surface(
                (self.frame_width, self.frame_height), pygame.SRCALPHA
            )
            attack_light_sprite.blit(
                self.character_attack_light_sheet,
                (0, 0),
                (frame * self.frame_width, 0, self.frame_width, self.frame_height),
            )
            self.attack_light_animation.append(attack_light_sprite)
            
    def load_attack_heavy_animation(self):
        for frame in range(self.attack_heavy_animation_steps):
            attack_heavy_sprite = pygame.Surface(
                (self.frame_width, self.frame_height), pygame.SRCALPHA
            )
            attack_heavy_sprite.blit(
                self.character_attack_heavy_sheet,
                (0, 0),
                (frame * self.frame_width, 0, self.frame_width, self.frame_height),
            )
            self.attack_heavy_animation.append(attack_heavy_sprite)

    def load_hurt_animation(self):
        for frame in range(self.hurt_animation_steps):
            hurt_sprite = pygame.Surface(
                (self.frame_width, self.frame_height), pygame.SRCALPHA
            )
            hurt_sprite.blit(
                self.character_hurt_sheet,
                (0, 0),
                (frame * self.frame_width, 0, self.frame_width, self.frame_height),
            )
            self.hurt_animation.append(hurt_sprite)
            
    def load_dead_animation(self):
        for frame in range(self.dead_animation_steps):
            dead_sprite = pygame.Surface(
                (self.frame_width, self.frame_height), pygame.SRCALPHA
            )
            dead_sprite.blit(
                self.character_dead_sheet,
                (0, 0),
                (frame * self.frame_width, 0, self.frame_width, self.frame_height),
            )
            self.dead_animation.append(dead_sprite)

    def set_current_animation(self, steps):
        if self.current_animation_steps != steps:
            self.current_frame = 0  
        self.current_animation_steps = steps    
        self.animation_delay = self.base_animation_delay / self.max_steps

    def get_current_idle_animation(self):
        self.set_current_animation(self.idle_animation_steps)
        self.update_animation()
        return self.idle_animation[self.current_frame]

    def get_current_running_animation(self):
        self.set_current_animation(self.running_animation_steps)
        self.update_animation()
        return self.running_animation[self.current_frame]

    def get_current_jumping_animation(self):
        self.set_current_animation(self.jumping_animation_steps)
        self.update_animation()
        return self.jumping_animation[self.current_frame]

    def get_current_attack_light_animation(self):
        self.set_current_animation(self.attack_light_animation_steps)
        self.update_animation()
        return self.attack_light_animation[self.current_frame]

    def get_current_attack_heavy_animation(self):
        self.set_current_animation(self.attack_heavy_animation_steps)
        self.update_animation()
        return self.attack_heavy_animation[self.current_frame]

    def get_current_hurt_animation(self):
        self.set_current_animation(self.hurt_animation_steps)
        self.update_animation()
        return self.hurt_animation[self.current_frame]
    
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
