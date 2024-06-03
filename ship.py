import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """
    A class to manage the player's ship.
    """

    def __init__(self, game_settings, screen):
        """
        Initialize the ship and set its starting position.

        Args:
            game_settings: An instance of the settings class containing game settings.
            screen: The screen surface where the game is displayed.
        """
        super(Ship, self).__init__()
        self.screen = screen
        self.game_settings = game_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship25x25.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """
        Update the ship's position based on movement flags.
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.game_settings.ship_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """
        Draw the ship at its current location.
        """
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """
        Center the ship on the screen.
        """
        self.center = self.screen_rect.centerx
