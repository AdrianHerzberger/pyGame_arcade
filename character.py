import pygame
from pygame.locals import *


class Character:
    def __init__(self):
        self.character_idle_sheet = pygame.image.load(
            "assets/character/idle.png"
        ).convert_alpha()
        self.idle_animation = []
        self.idle_animation_steps = 6
        self.current_frame = 0
        self.frame_width = 128
        self.frame_height = 128
        self.scale = 3
        self.animation_delay = 200
        self.last_update_time = pygame.time.get_ticks()
        self.color = (0, 0, 0)

        self.load_idle_animation()

    def load_idle_animation(self):
        for frame in range(self.idle_animation_steps):
            idle_sprite = pygame.Surface((self.frame_width, self.frame_height), pygame.SRCALPHA)
            idle_sprite.blit(
                self.character_idle_sheet,
                (0, 0),
                (frame * self.frame_width, 0, self.frame_width, self.frame_height),
            )
            self.idle_animation.append(idle_sprite)

    def get_current_idle_sprite(self):
        return self.idle_animation[self.current_frame]

    def update_animation(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update_time > self.animation_delay:
            print("Updating animation...")
            print("Current frame:", self.current_frame)
            self.current_frame = (self.current_frame + 1) % self.idle_animation_steps
            print("Updated frame:", self.current_frame)
            self.last_update_time = current_time
