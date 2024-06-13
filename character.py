import pygame
from pygame.locals import *


class Character_Animation:
    def __init__(self):
        self.character_idle_sheet = pygame.image.load(
            "assets/character/player/idle.png"
        ).convert_alpha()
        self.character_running_sheet = pygame.image.load(
            "assets/character/player/run.png"
        )
        self.idle_animation = []
        self.running_animation = []
        self.idle_animation_steps = 6
        self.running_animation_steps = 8
        self.current_frame = 0
        self.frame_width = 128
        self.frame_height = 128
        self.scale = 3
        self.animation_delay = 400
        self.last_update_time = pygame.time.get_ticks()
        self.color = (0, 0, 0)

        self.load_idle_animation()

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
                self.character_idle_sheet,
                (0, 0),
                (frame * self.frame_width, 0, self.frame_width, self.frame_height),
            )
            self.running_animation.append(running_sprite)

    def get_current_idle_animation(self):
        self.update_animation()
        return self.idle_animation[self.current_frame]

    def get_current_running_animation(self):
        self.update_animation()
        return self.running_animation[self.current_frame]

    def update_animation(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update_time > self.animation_delay:
            self.current_frame = (self.current_frame + 1) % self.idle_animation_steps
            self.last_update_time = current_time


