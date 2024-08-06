import pygame
from globals import SCREEN_WIDTH, SCREEN_HEIGHT  

class GameOverScreen:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 55)
        self.game_over_text = self.font.render("Game Over", True, (255, 0, 0))
        self.restart_text = self.font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))
        
        self.overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        self.overlay.fill((0, 0, 0, 180)) 

    def display(self):
        self.screen.blit(self.overlay, (0, 0)) 
        self.screen.blit(self.game_over_text, (self.screen.get_width() // 2 - self.game_over_text.get_width() // 2, self.screen.get_height() // 2 - self.game_over_text.get_height() // 2 - 50))
        self.screen.blit(self.restart_text, (self.screen.get_width() // 2 - self.restart_text.get_width() // 2, self.screen.get_height() // 2 + 50))
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return "restart"
                elif event.key == pygame.K_q:
                    pygame.quit()
                    exit()
        return "continue"
