import pygame
from pygame.sprite import Sprite

class Invader(Sprite):
    """
    A class to represent a single invader in the game.
    """

    def __init__(self, game_settings, screen):
        """
        Initialize the invader and set its starting position.

        Args:
            game_settings: An instance of the settings class containing game settings.
            screen: The screen surface where the game is displayed.
        """
        super(Invader, self).__init__()
        self.screen = screen
        self.game_settings = game_settings

        # Load the invader image and set its rect attribute.
        self.image = pygame.image.load('images/invader.png')
        self.rect = self.image.get_rect()

        # Start each new invader near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the invader's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        """
        Draw the invader at its current location.
        """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """
        Move the invader right or left based on the game settings.
        """
        self.x += (self.game_settings.invader_speed_factor * self.game_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """
        Return True if invader is at edge of screen.

        Returns:
            bool: True if the invader is at the edge of the screen, False otherwise.
        """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        return False
