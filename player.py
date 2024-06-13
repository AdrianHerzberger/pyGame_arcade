import pygame
from pygame.locals import *
from globals import *
from inputs import GameInputs


class Player:
    def __init__(self, inputs):
        self.jumping = True
        self.inputs = inputs

    def gravity(self):
        if self.jumping == True:
            player_jumping = self.inputs.jump()
