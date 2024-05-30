import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from map import World
from globals import * 

clock = pygame.time.Clock()

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    
    world = World(screen)

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            
        world.draw_mountain()

        pygame.display.flip()
        pygame.time.wait(10)
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
