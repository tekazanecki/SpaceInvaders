import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, game_settings, screen):
        """Inicjalizacja statku kosmicznego"""
        super(Ship, self).__init__()
        self.screen = screen
        self.game_settings = game_settings

        # obraz statku kosmicznego
        self.image = pygame.image.load('images/ship25x25.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # statek pojawia się na środku ekranu
        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Uaktualnienie położenia statku"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.game_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """Wyświetlanie statku kosmicznego"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Umieszczanie statku na środku dolnej krawędzi ekranu"""
        self.center = self.screen_rect.centerx