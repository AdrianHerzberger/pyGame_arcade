import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from globals import *
from inputs import GameInputs
from map import World
from character_animations import Character_Animation
from player import Player
from enemies_movable import Enemy_Movable
from enemy_static import Enemy_Static
from collectables_health import Health_Bottles
from camera import Camera

clock = pygame.time.Clock()


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(screen)
    inputs = GameInputs(player)
    world = World(screen, inputs)
    enemies_movable = Enemy_Movable.create_enemies()
    enemies_static = Enemy_Static.create_enemies()
    bottles = Health_Bottles.create_bottles()
    camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        scroll = inputs.move_left_right()
        player.update(enemies_movable, bottles, scroll)
        world.draw_world(scroll)

        player_animation = player.get_current_animation()
        screen.blit(player_animation, (player.x_pos, player.y_pos))
        player.player_health_animation.draw_health_bar(
            player.player_health_meter_center,
            player.player_health_meter_right,
            player.player_health_meter_left,
        )
        player.collision_handler.draw(screen)
        player.collision_handler.draw_attack_collision_rect(screen)

        Enemy_Movable.draw_enemies(screen, enemies_movable, scroll)
        Enemy_Static.draw_enemies(screen, enemies_static, scroll)
        Health_Bottles.draw_health_bottles(screen, bottles, scroll)

        pygame.display.flip()
        clock.tick(FPS)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
