import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from globals import *
from inputs import GameInputs
from map import World
from character_animations import Character_Animation
from player import Player
from enemy import Enemy
from camera import Camera

clock = pygame.time.Clock()


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    inputs = GameInputs()
    world = World(screen, inputs)
    player = Player(screen)
    enemies = Enemy.create_enemies()
    camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                
        scroll = inputs.move_left_right()
        player.update(enemies, scroll)  
        world.draw_meadow(scroll)
        
        player_animation = player.get_current_animation()
        screen.blit(player_animation, (player.x_pos, player.y_pos))
        player.player_health_animation.draw_health_bar(player.player_health_meter_center, player.player_health_meter_right, player.player_health_meter_left)
        player.collision_handler.draw(screen)

        Enemy.draw_all(screen, enemies, scroll)

        pygame.display.flip()
        clock.tick(FPS)

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
