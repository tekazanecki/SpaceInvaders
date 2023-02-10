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
        self.ship_limit = 3

        # ustawienia pocisku
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # ustawienia obcych
        self.invader_speed_factor = 1
        self.fleet_drop_speed = 10
        self.invader_points = 50

        # kierunek 1 oznacza lewo, -1 oznacza prawo
        self.fleet_direction = 1
        # łatwa zmiana szybkości gry
        self.speedup_scale = 1.1
        # łatwa zmiana punktacji
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicjalizacja ustawień, które ulegają zmianie w trakcie gry"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.invader_speed_factor = 1

        # kierunek 1 oznacza lewo, -1 oznacza prawo
        self.fleet_direction = 1

    def increese_speed(self):
        """Zmiana ustawień dotyczących szybkości"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.invader_speed_factor *= self.speedup_scale
        self.invader_points = int(self.invader_points * self.score_scale)
