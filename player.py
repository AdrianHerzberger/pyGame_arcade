import pygame
from pygame.locals import *
from globals import *
from inputs import GameInputs
from character_animations import Character_Animation
from player_health import Player_Health
from player_collision import Player_Collision
from health_bar_animations import Health_Bar_Animation


class Player:
    def __init__(self, screen):
        self.key = None
        self.jumping = False
        self.running = False
        self.facing_left = False
        self.attack_light = False
        self.on_ground = True
        self.is_hit = False
        self.jump_force = 0
        self.gravity = 5
        self.x_pos = CHAR_X_POS
        self.y_pos = CHAR_Y_POS
        self.inputs = GameInputs()
        self.character_animation = Character_Animation()
        self.collision_handler = Player_Collision(self)
        self.player_health = Player_Health()
        self.player_health_animation = Health_Bar_Animation(screen)
        self.player_health_meter_center = 50
        self.player_health_meter_right = 25
        self.player_health_meter_left = 25

    def update(self, enemies):
        self.key = pygame.key.get_pressed()
        if self.key[pygame.K_SPACE] and self.on_ground:
            self.jumping = True
            self.on_ground = False
            self.jump_force = 30

        if self.jumping:
            self.y_pos -= self.jump_force
            self.jump_force -= self.gravity

        if self.y_pos >= CHAR_Y_POS:
            self.y_pos = CHAR_Y_POS
            self.jumping = False
            self.jump_force = 0
            self.on_ground = True
        elif self.y_pos < CHAR_Y_POS and not self.jumping:
            self.y_pos += self.gravity

        if self.inputs.move_left_right():
            self.running = True
            self.running_direction()

        if self.inputs.attack_light():
            self.attack_light = True

        self.resolve_player_inputs()
        self.handle_collisions(enemies)

        if self.y_pos == CHAR_Y_POS:
            self.on_ground = True

        return self.y_pos

    def handle_collisions(self, enemies):
        enemy_collisions = self.collision_handler.get_hits(enemies)
        """
        player is currently able to take damage but not to heal.
        Implement healing timeout 
        """
        if enemy_collisions:
            self.is_hit = True
            self.update_player_health()
        else:
            self.is_hit = False

        if not self.jumping:
            self.on_ground = self.collision_handler.player.on_ground
            self.y_pos = self.collision_handler.player.y_pos

        if not self.player_health.is_alive():
            print("Player is dead!")
            
    def update_player_health(self):
        current_health = self.player_health.taking_damage(ENEMY_DAMAGE)
        if self.player_health_meter_center > 0:
            self.player_health_meter_center -= 1
        elif self.player_health_meter_right > 0:
            self.player_health_meter_right -= 1 
        elif self.player_health_meter_left > 0:
            self.player_health_meter_left -= 1
            if self.player_health_meter_center < 0:
                self.player_health_meter_center = 0
                self.player_health_meter_left = 0
                self.player_health_meter_right = 0
        
    def resolve_player_inputs(self):
        self.key = pygame.key.get_pressed()
        if not self.key[pygame.K_LEFT] and not self.key[pygame.K_RIGHT]:
            self.running = False
        if not self.key[pygame.K_COMMA]:
            self.attack_light = False
        if not self.key[pygame.K_SPACE]:
            self.jumping = False
        if not self.collision_handler:
            self.jumping = True

    def running_direction(self):
        self.key = pygame.key.get_pressed()
        if self.key[pygame.K_LEFT]:
            self.facing_left = True
        elif self.key[pygame.K_RIGHT]:
            self.facing_left = False

    def get_current_animation(self):
        if self.jumping:
            animation = self.character_animation.get_current_jumping_animation()
        elif self.running:
            animation = self.character_animation.get_current_running_animation()
        elif self.attack_light:
            animation = self.character_animation.get_current_attack_light_animation()
        elif self.is_hit:
            animation = self.character_animation.get_current_hurt_animation()
        else:
            animation = self.character_animation.get_current_idle_animation()

        if self.facing_left:
            animation = pygame.transform.flip(animation, True, False)

        return animation
