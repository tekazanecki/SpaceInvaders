import sys

import pygame

def check_keydown_event(event, ship):
    """Reakcja na naciśnięcie klawisza"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_event(event, ship):
    """Reakcja na zwolnienie klawisza"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    """Reakcja na zdarzenia generowane przez klawiaturę i mysz"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)

def update_screen(game_settings, screen, ship):
    """Uaktualnianie ekranu"""
    # odświeżanie ekranu
    screen.fill(game_settings.bg_color)
    ship.blitme()

    # wyświetlanie ostatniego ekranu
    pygame.display.flip()