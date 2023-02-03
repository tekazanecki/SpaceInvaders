import sys

import pygame
from pygame.sprite import Group
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
    # przechowywanie pocisków
    bullets = Group()

    # główna pętla
    while True:

        # obsługa przycisków
        gf.check_events(game_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        # obsługa ekranu
        gf.update_screen(game_settings, screen, ship, bullets)

run_game()
