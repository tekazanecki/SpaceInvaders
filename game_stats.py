class GameStats:
    """
    Track statistics for the game SPACE INVADERS.
    """

    def __init__(self, game_settings):
        """
        Initialize statistics.

        Args:
            game_settings: An instance of the settings class containing game settings.
        """
        self.game_settings = game_settings
        self.reset_status()
        self.game_active = False

        # Initialize score
        self.score = 0
        # Initialize high score
        self.high_score = 0

    def reset_status(self):
        """
        Initialize statistics that can change during the game.
        """
        self.ships_left = self.game_settings.ship_limit
        self.score = 0
        self.level = 1
