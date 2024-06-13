import pygame
from pygame.locals import *
from globals import *
from inputs import GameInputs
from character import Character_Animation


class Player:
    def __init__(self):
        self.key = None
        self.jumping = False
        self.running = False
        self.facing_left = False
        self.movement = False
        self.inputs = GameInputs()
        self.animation = Character_Animation()
        self.y_pos = CHAR_Y_POS

    def update(self):
        self.key = pygame.key.get_pressed()
        self.running = False

        if self.inputs.jumping():
            self.jumping = True
        if self.jumping:
            self.y_pos -= self.inputs.jump_force
            self.inputs.jump_force -= 1
            if self.y_pos >= CHAR_Y_POS:
                self.y_pos = CHAR_Y_POS
                self.jumping = False
                self.inputs.jump_force = 0
        if self.inputs.move_left_right():
            self.running = True
            self.running_direction()
        return self.y_pos

    def running_direction(self):
        self.key = pygame.key.get_pressed()
        self.movement = False
        
        if self.key[pygame.K_LEFT]:
            self.movement = True
            self.facing_left = True
        elif self.key[pygame.K_RIGHT]:
            self.movement = True
            self.facing_left = False   

    def get_current_animation(self):
        if self.jumping:
            animation = self.animation.get_current_jumping_animation()
        elif self.running:
            animation = self.animation.get_current_running_animation()
        else:
            animation = self.animation.get_current_idle_animation()
        if self.facing_left:
            animation = pygame.transform.flip(animation, True, False)
        return animation
