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
        self.frame_width = 24
        self.frame_height = 24
        self.scale = 3

        self.load_idle_animation()

    def load_idle_animation(self):
        for frame in range(self.idle_animation_steps):
            idle_sprite = pygame.Surface((self.frame_width, self.frame_height))
            idle_sprite.blit(
                self.character_idle_sheet,
                (frame * self.frame_width, 0, self.frame_width, self.frame_height),
            )
            idle_sprite = pygame.transform.scale(
                idle_sprite,
                (self.frame_width * self.scale, self.frame_height * self.scale),
            )
            self.idle_animation.append(idle_sprite)
            print(self.idle_animation)

    def get_current_idle_sprite(self):
        return self.idle_animation[self.current_frame]

    def update_animation(self):
        self.current_frame = (self.current_frame + 1) % self.idle_animation_steps

