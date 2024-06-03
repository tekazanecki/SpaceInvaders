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
    """
    Initialize game and create a screen object, then start the main loop for the game.
    """
    # Initialize the game and create a screen object
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Space Invasion")

    # Create an instance to store game statistics and a scoreboard
    game_stats = GameStats(game_settings)
    scoreboard = Scoreboard(game_settings, screen, game_stats)

    # Make the Play button
    play_button = Button(game_settings, screen, "Play")

    # Create a ship, a group to store bullets, and a group to store invaders
    ship = Ship(game_settings, screen)
    bullets = Group()
    invaders = Group()
    gf.create_fleet(game_settings, screen, ship, invaders)

    # Start the main loop for the game
    while True:
        # Watch for keyboard and mouse events
        gf.check_events(game_settings, game_stats, scoreboard, screen, ship, invaders, bullets, play_button)

        if game_stats.game_active:
            ship.update()
            gf.update_bullets(game_settings, screen, game_stats, scoreboard, ship, bullets, invaders)
            gf.update_invaders(game_settings, game_stats, scoreboard, screen, ship, invaders, bullets)

        # Update the screen
        gf.update_screen(game_settings, game_stats, scoreboard, screen, ship, invaders, bullets, play_button)

run_game()
