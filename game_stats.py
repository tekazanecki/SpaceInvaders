class GameStats():
    """Monitorowanie danych statystycznych w grze SPACE INVIDERS"""

    def __init__(self, game_settings):
        """Inicjalizacja danych statystycznych"""
        self.game_settings = game_settings
        self.reset_status()
        self.game_active = False

        # wynik
        self.score = 0
        # najwyższy wynik
        self.high_score = 0

    def reset_status(self):
        """Inicjalizacja danych statystycznych"""
        self.ships_left = self.game_settings.ship_limit
        self.score = 0
        self.level = 1
