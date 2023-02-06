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

        # ustawienia pocisku
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # ustawienia obcych
        self.invader_speed_factor = 1
        self.fleet_drop_speed = 10
        # kierunek 1 oznacza lewo, -1 oznacza prawo
        self.fleet_direction = 1