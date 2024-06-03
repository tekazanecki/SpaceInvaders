import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    """
    A class to report scoring information.
    """

    def __init__(self, game_settings, screen, game_stats):
        """
        Initialize scorekeeping attributes.

        Args:
            game_settings: An instance of the settings class containing game settings.
            screen: The screen surface where the game is displayed.
            game_stats: An instance of the GameStats class to track game statistics.
        """
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.game_settings = game_settings
        self.game_stats = game_stats

        # Font settings for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score images
        self.score_image = ''
        self.score_rect = ''
        self.prep_score()

        self.high_score_image = ''
        self.high_score_rect = ''
        self.prep_high_score()

        self.level_image = ''
        self.level_rect = ''
        self.prep_level()

        self.ships = ''
        self.prep_ships()

    def prep_score(self):
        """
        Turn the score into a rendered image.
        """
        rounded_score = int(round(self.game_stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.game_settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """
        Turn the high score into a rendered image.
        """
        rounded_high_score = int(round(self.game_stats.high_score, -1))
        high_score_str = "{:,}".format(rounded_high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.game_settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        """
        Turn the level into a rendered image.
        """
        self.level_image = self.font.render(str(self.game_stats.level), True, self.text_color, self.game_settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = 60

    def prep_ships(self):
        """
        Show how many ships are left.
        """
        self.ships = Group()
        for ship_number in range(self.game_stats.ships_left):
            ship = Ship(self.game_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width + 5 * ship_number
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """
        Draw scores, level, and ships to the screen.
        """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
