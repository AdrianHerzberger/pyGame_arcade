import pygame
from pygame.locals import *
from globals import *
from inputs import GameInputs
from character_animations import Character_Animation
from health_bar_animations import Health_Bar_Animation
from player_health import Player_Health
from player_collision import Player_Collision
from game_over_screen import GameOverScreen
from time import time


class Player:
    def __init__(self, screen):
        self.key = None
        self.jumping = False
        self.running = False
        self.facing_left = False
        self.attack_light = False
        self.attack_heavy = False
        self.on_ground = True
        self.is_hit = False
        self.is_dead = False
        self.dead_animation_played = False
        self.dead_animation_duration = 2.0
        self.dead_animation_start_time = None
        self.jump_force = 0
        self.gravity = 5
        self.screen = screen
        self.x_pos = PLAYER_X_POS
        self.y_pos = PLAYER_Y_POS
        self.inputs = GameInputs(self)
        self.character_animation = Character_Animation()
        self.collision_handler = Player_Collision(self)
        self.player_health = Player_Health()
        self.player_health_animation = Health_Bar_Animation(screen)
        self.game_over_screen = GameOverScreen(screen)
        self.player_health_meter_center = 50
        self.player_health_meter_right = 25
        self.player_health_meter_left = 25

    def update(self, enemies, bottles, scroll):
        if self.inputs.is_jumping():
            self.jumping = True
            self.on_ground = False
            self.jump_force = 55

        if self.jumping:
            self.y_pos -= self.jump_force
            self.jump_force -= self.gravity

        if self.y_pos >= PLAYER_Y_POS:
            self.y_pos = PLAYER_Y_POS
            self.jumping = False
            self.jump_force = 0
            self.on_ground = True
        elif self.y_pos < PLAYER_Y_POS and not self.jumping:
            self.y_pos += self.gravity

        if self.inputs.move_left_right():
            self.running = True
            self.running_direction()

        if self.inputs.is_attacking_light():
            self.attack_light = True
            self.kill_enemy(enemies, scroll)
        else:
            self.attack_light = False
            
        if self.inputs.is_attacking_heavy():
            self.attack_heavy = True
            self.kill_enemy(enemies, scroll)
        else: 
            self.attack_heavy = False

        self.resolve_player_inputs()
        self.handle_collisions(enemies, scroll)
        
        if not self.player_health.current_health >= MAX_PLAYER_HEALTH:
            self.collect_health_bottles(bottles, scroll)

        if self.y_pos == PLAYER_Y_POS:
            self.on_ground = True

        return self.y_pos
    
    def collect_health_bottles(self, bottles, scroll):
        bottle_collisions = self.collision_handler.get_bottle_hits(bottles, scroll)
        for bottle in bottle_collisions:
            if bottle_collisions:
                bottle.is_bottle_collected = True
                bottles.remove(bottle)
                self.player_health.heal_up(BOTTLE_HEAL)
                self.gain_player_health()

    def gain_player_health(self):
        if self.player_health_meter_right > 0:
            self.player_health_meter_right += 1
        elif self.player_health_meter_left > 0:
            self.player_health_meter_left += 1
            if self.player_health_meter_center < 0:
                self.player_health_meter_center = 0
                self.player_health_meter_left = 0
                self.player_health_meter_right = 0
        elif self.player_health_meter_center > 0:
            self.player_health_meter_center += 1

    
    def kill_enemy(self, enemies, scroll):
        from enemy_boss import Enemy_Boss 
        player_hit_enemies = self.collision_handler.get_hits(enemies, scroll)
        for enemy in player_hit_enemies:
            if self.attack_light:
                if isinstance(enemy, Enemy_Boss):
                    enemy_health = enemy.boss_health.taking_damage(PLAYER_DAMAGE_LIGHT)
                else:
                    enemy_health = enemy.enemy_health.taking_damage(PLAYER_DAMAGE_LIGHT)
            if self.attack_heavy:
                if isinstance(enemy, Enemy_Boss):
                    enemy_health = enemy.boss_health.taking_damage(PLAYER_DAMAGE_HEAVY)
                else:
                    enemy_health = enemy.enemy_health.taking_damage(PLAYER_DAMAGE_HEAVY)
            if enemy_health <= 0:
                enemy.is_dead = True

    def handle_collisions(self, enemies, scroll):
        from boss_health import Boss_Health 
        alive_enemies = self.is_enemy_alive(enemies)

        enemy_collisions = self.collision_handler.get_hits(alive_enemies, scroll)
        if enemy_collisions:
            self.is_hit = True
            self.drain_player_health()
        else:
            self.is_hit = False

        if not self.jumping:
            self.on_ground = self.collision_handler.player.on_ground
            self.y_pos = self.collision_handler.player.y_pos

        if not self.player_health.is_alive():
            self.is_dead = True
            if self.dead_animation_start_time is None:
                self.dead_animation_start_time = time()
            self.game_over()

    def is_enemy_alive(self, enemies):
        alive_enemies = [enemy for enemy in enemies if not enemy.is_dead]
        return alive_enemies
    
    
    def game_over(self):
        if self.dead_animation_start_time:
            elapsed_time = time() - self.dead_animation_start_time
            if elapsed_time < self.dead_animation_duration:
                animation = self.get_current_animation()
                self.screen.blit(animation, (self.x_pos, self.y_pos))  
                pygame.display.flip()
                return
            
        self.game_over_screen.display()
        while True:
            action = self.game_over_screen.handle_events()
            if action == "restart":
                self.reset_game()
                break
            elif action == "quit":
                pygame.quit()
                exit()
                
    def reset_game(self):
        self.player_health.reset() 
        self.x_pos = PLAYER_X_POS
        self.y_pos = PLAYER_Y_POS
        self.is_dead = False
        self.dead_animation_start_time = None

    def drain_player_health(self):
        if self.is_hit:
            current_player_health = self.player_health.taking_damage(ENEMY_DAMAGE)
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
        if not self.inputs.is_running():
            self.running = False
        if not self.inputs.is_attacking_light():
            self.attack_light = False
        if not self.key[pygame.K_SPACE]:
            self.jumping = False
        if not self.collision_handler:
            self.jumping = True
            
        if self.inputs.is_running():
            self.attack_light = False
            self.attack_heavy = False


    def running_direction(self):
        self.key = self.inputs.get_key_presses()
        if self.key[pygame.K_LEFT]:
            self.facing_left = True
        elif self.key[pygame.K_RIGHT]:
            self.facing_left = False

    def get_current_animation(self):
        if self.is_dead:
            if not self.dead_animation_played:
                animation = self.character_animation.get_current_dead_animation()
                if self.facing_left:
                    animation = pygame.transform.flip(animation, True, False)
                    self.dead_animation_played = True
                return animation
            else:
                return self.character_animation.get_dead_static_frame()

        if self.jumping:
            animation = self.character_animation.get_current_jumping_animation()
        elif self.running:
            animation = self.character_animation.get_current_running_animation()
        elif self.attack_light:
            animation = self.character_animation.get_current_attack_light_animation()
        elif self.attack_heavy:
            animation = self.character_animation.get_current_attack_heavy_animation()
        elif self.is_hit:
            animation = self.character_animation.get_current_hurt_animation()
        else:
            animation = self.character_animation.get_current_idle_animation()

        if self.facing_left:
            animation = pygame.transform.flip(animation, True, False)

        return animation
