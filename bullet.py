import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Klasa do zarządzania pociskami statku"""

    def __init__(self, game_settings, screen, ship):
        """Utworzenie pocisku w miejscu statku"""
        super(Bullet, self).__init__()
        self.screen = screen

        # pocisk w miejscu 0,0
        self.rect = pygame.Rect(0,0, game_settings.bullet_width, game_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor

    def update(self):
        """Poruszanie się pocisków"""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """Wyświetlanie pocisku na ekranie"""
        pygame.draw.rect(self.screen, self.color, self.rect)