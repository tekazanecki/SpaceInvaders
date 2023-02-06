import pygame
from pygame.sprite import Sprite

class Invader(Sprite):
    """Klasa pojedynczego obcego w grze"""

    def __init__(self, game_settings, screen):
        "Inicjalizacja obcego w konkretnym miejscu"
        super(Invader, self).__init__()
        self.screen = screen
        self.game_settings = game_settings

        # obrazek obcego
        self.image = pygame.image.load('images/invader.png')
        self.rect = self.image.get_rect()

        # lokalizacja w obszarze górnego lewego rogu
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # dokładne położenie obcego
        self.x = float(self.rect.x)

    def blitme(self):
        """Wyświtlanie obcego w jego aktualnym położeniu"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Przesuniecie obcego"""
        self.x += (self.game_settings.invader_speed_factor * self.game_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Zwraca wartość True jeśli obcy znajduje się przy krawędzi ekranu"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
