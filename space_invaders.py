import sys

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # rozpoczęcie gry i inicjalizacja ekranu
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Kosmiczna Inwazja")

    # statek kosmiczny
    ship = Ship(screen, game_settings)

    # główna pętla
    while True:

        # obsługa przycisków
        gf.check_events(ship)
        ship.update()
        # obsługa ekranu
        gf.update_screen(game_settings, screen, ship)

run_game()
