import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from globals import *
from inputs import GameInputs
from map import World
from character import Character_Animation
from player import Player
from enemy import Enemy

clock = pygame.time.Clock()


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    inputs = GameInputs()
    world = World(screen, inputs)
    player = Player()
    char = Character_Animation()
    enemies = Enemy.create_enemies()
    
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        world.draw_meadow()
        
        Enemy.draw_all(screen, enemies)
        current_player = player.update(enemies)
        current_character = player.get_current_animation()
        screen.blit(current_character, (CHAR_X_POS, current_player))

        pygame.display.flip()
        pygame.time.wait(10)
        clock.tick(FPS)

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
