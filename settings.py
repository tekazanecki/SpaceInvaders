class Settings:
    """Klasa przeznaczona dla ustawień gry"""

    def __init__(self):
        """inicjalizacja ustawień gry"""
        # ustawienia ekranu
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ustawienia statku
        self.ship_speed_factor = 1.5