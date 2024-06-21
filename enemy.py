import pygame

class Enemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), self.rect)

    @classmethod
    def create_enemies(cls):
        return [
            cls(200, 150),
            cls(400, 150),
            cls(600, 150)
        ]

    @staticmethod
    def draw_all(screen, enemies):
        for enemy in enemies:
            enemy.draw(screen)
