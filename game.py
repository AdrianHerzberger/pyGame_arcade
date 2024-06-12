import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from globals import *
from inputs import GameInputs
from map import World
from character import Character

clock = pygame.time.Clock()


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    inputs = GameInputs()
    world = World(screen, inputs)
    char = Character()

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        world.draw_meadow()
        char.update_animation()
        current_character = char.get_current_idle_sprite()
        screen.blit(current_character, (20, 35))

        pygame.display.flip()
        pygame.time.wait(10)
        clock.tick(FPS)

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
