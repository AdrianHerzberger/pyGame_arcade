import pygame
from pygame.locals import *
from globals import *


class PlayerHealth:
    def __init__(self, max_health):
        self.max_health = max_health
        self.current_health = max_health
        
    def taking_damage(self, damage):
        self.current_health -= damage
        if self.current_health < 0:
            self.current_health = 0
            
    def heal_up(self, heal):
        self.current_health += heal
        if self.current_health > self.max_health:
            self.current_health = self.max_health
            
    def is_alive(self):
        return self.current_health > 0
        
        
        
        
    