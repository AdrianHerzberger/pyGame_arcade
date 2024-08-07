import pygame
from pygame.locals import *
from enemy_movable_animations import Enemy_Movable_Animations

class Enemy_Static_Animations(Enemy_Movable_Animations):
    def __init__(self):
        self.enemy_static_idle_sheet = pygame.image.load(
            "assets/enemy/static/idle.png"
        )
        self.enemy_static_dead_sheet = pygame.image.load(
            "assets/enemy/static/disguise.png"
        )
        self.enemy_static_attack_sheet = pygame.image.load(
            "assets/enemy/static/poison.png"
        )
        self.enemy_poison_attack_sheet = pygame.image.load(
            "assets/enemy/static/cloud_posion.png"
        )

        self.idle_animation = []
        self.dead_animation = []
        self.static_attack = []
        self.poison_attack = []

        self.idle_animation_steps = 5
        self.dead_animation_steps = 5
        self.static_attack_steps = 7
        self.poison_attack_steps = 9

        self.max_steps = max(
            self.idle_animation_steps,
            self.dead_animation_steps,
            self.static_attack_steps,
            self.poison_attack_steps,
        )

        self.current_animation_steps = 9
        self.current_frame = 0
        self.base_animation_delay = 800
        self.last_update_time = pygame.time.get_ticks()

        self.frame_width = 128
        self.frame_height = 128

        self.dead_animation_finished = False

        self.load_idle_animation()
        self.load_dead_animation()
        self.load_static_attack()

    def load_idle_animation(self):
        for frame in range(self.idle_animation_steps):
            idle_sprite = pygame.Surface(
                (self.frame_width, self.frame_height), pygame.SRCALPHA
            )
            idle_sprite.blit(
                self.enemy_static_idle_sheet,
                (0, 0),
                (frame * self.frame_width, 0, self.frame_width, self.frame_height),
            )
            self.idle_animation.append(idle_sprite)

    def load_dead_animation(self):
        for frame in range(self.dead_animation_steps):
            dead_sprite = pygame.Surface(
                (self.frame_width, self.frame_height), pygame.SRCALPHA
            )
            dead_sprite.blit(
                self.enemy_static_dead_sheet,
                (0, 0),
                (frame * self.frame_width, 0, self.frame_width, self.frame_height),
            )
            self.dead_animation.append(dead_sprite)

    def load_static_attack(self):
        for frame in range(self.static_attack_steps):
            static_attack_sprite = pygame.Surface(
                (self.frame_width, self.frame_height), pygame.SRCALPHA
            )
            static_attack_sprite.blit(
                self.enemy_static_attack_sheet,
                (0, 0),
                (frame * self.frame_width, 0, self.frame_height, self.frame_height),
            )
            self.static_attack.append(static_attack_sprite)

    def load_poison_attack(self):
        for frame in range(self.poison_attack_steps):
            poison_attack_sprite = pygame.Surface(
                (self.frame_width, self.frame_height), pygame.SRCALPHA
            )
            poison_attack_sprite.blit(
                self.enemy_poison_attack_sheet,
                (0, 0),
                (frame * self.frame_width, 0, self.frame_height, self.frame_height),
            )
            self.poison_attack.append(poison_attack_sprite)

    def get_current_idle_animation(self):
        self.set_current_animation(self.idle_animation_steps)
        self.update_animation()
        return self.idle_animation[self.current_frame]

    def get_current_static_attack_animation(self):
        self.set_current_animation(self.static_attack_steps)
        self.update_animation()
        return self.static_attack[self.current_frame]

    def get_current_poison_attack_animation(self):
        self.set_current_animation(self.poison_attack_steps)
        self.update_animation()
        return self.poison_attack[self.current_frame]

