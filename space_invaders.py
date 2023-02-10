import pygame
import sys
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
import game_functions as gf


def run_game():
    # rozpoczęcie gry i inicjalizacja ekranu
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Kosmiczna Inwazja")
    # statystyki gry
    game_stats = GameStats(game_settings)
    scoreboard = Scoreboard(game_settings, screen, game_stats)
    # utworzenie przycisku gry
    play_button = Button(game_settings, screen, "Gra")

    # statek kosmiczny
    ship = Ship(game_settings, screen)
    # przechowywanie pocisków
    bullets = Group()
    # flota obcych
    invaders = Group()
    gf.create_fleet(game_settings, screen, ship, invaders)

    # główna pętla
    while True:
        # obsługa przycisków
        gf.check_events(game_settings, game_stats, scoreboard,  screen, ship, invaders, bullets, play_button)
        if game_stats.game_active:
            ship.update()
            gf.update_bullets(game_settings, screen, game_stats, scoreboard,  ship, bullets, invaders)
            gf.update_invaders(game_settings, game_stats, scoreboard,  screen, ship,  invaders, bullets)
        # obsługa ekranu
        gf.update_screen(game_settings, game_stats, scoreboard, screen, ship, invaders, bullets, play_button)

run_game()
