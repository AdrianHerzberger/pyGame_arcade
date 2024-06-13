import pygame
from pygame.locals import *
from globals import *
from inputs import GameInputs
from character import Character_Animation


class Player:
    def __init__(self):
        self.jumping = False
        self.inputs = GameInputs()
        self.animation = Character_Animation()
        self.y_pos = CHAR_Y

    def update(self):
        if self.inputs.jumping():
            self.jumping = True
            self.inputs.jump_force = 10
        if self.jumping:
            self.y_pos -= self.inputs.jump_force
            self.inputs.jump_force -= 1
            if self.y_pos >= CHAR_Y:
                self.y_pos = CHAR_Y
                self.jumping = False
                self.inputs.jump_force = 0
        return self.y_pos
            
    def get_current_animation(self):
        if self.jumping:
            return self.animation.get_current_jumping_animation()
        else:
            return self.animation.get_current_idle_animation()
            
