from globals import *


class Boss_Health:
    def __init__(self):
        self.max_health = MAX_BOSS_HEALTH
        self.current_health = self.max_health

    def taking_damage(self, damage):
        self.current_health -= damage
        if self.current_health < 0:
            self.current_health = 0
        return self.current_health

    def heal_up(self, heal):
        self.current_health += heal
        if self.current_health > self.max_health:
            self.current_health = self.max_health

    def is_alive(self):
        return self.current_health > 0
