import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """Klasa przeznaczona do przedstawiania punktancji"""

    def __init__(self, game_settings, screen, game_stats):
        """Inicjalizacja atrybutów dotyczących punktacji"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.game_settings = game_settings
        self.game_stats = game_stats

        # ustalenie czcionki dla informacji o punktacji
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # obrazki do generowania
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
        """Przekształcenie punktacji na obraz"""
        rounded_score = int(round(self.game_stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.game_settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Przekształcenie najwyższego wyniku na obraz"""
        rounded_high_score = int(round(self.game_stats.high_score, -1))
        high_score = "{:,}".format(rounded_high_score)
        self.high_score_image = self.font.render(high_score, True, self.text_color, self.game_settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        """Przekształcenie poziomu gry na obraz"""
        self.level_image = self.font.render(str(self.game_stats.level), True, self.text_color, self.game_settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = 60

    def prep_ships(self):
        """Przekształcenie ilości statków na obraz"""
        self.ships = Group()
        for ship_number in range(self.game_stats.ships_left):
            ship = Ship(self.game_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width + 5 * ship_number
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """Wyświetlanie punktacji i statków na ekranie"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)