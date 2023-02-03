import sys

import pygame
from bullet import Bullet

def check_keydown_event(event, game_settings, screen, ship, bullets):
    """Reakcja na naciśnięcie klawisza"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)

def check_keyup_event(event, ship):
    """Reakcja na zwolnienie klawisza"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def fire_bullet(game_settings, screen, ship, bullets):
    """Wystrzelenie pocisku"""
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)

def check_events(game_settings, screen, ship, bullets ):
    """Reakcja na zdarzenia generowane przez klawiaturę i mysz"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, game_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)

def update_screen(game_settings, screen, ship, bullets):
    """Uaktualnianie ekranu"""
    # odświeżanie ekranu
    screen.fill(game_settings.bg_color)
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()

    # wyświetlanie ostatniego ekranu
    pygame.display.flip()

def update_bullets(bullets):
    """Uaktualnij położenie pocisków i usunięcie tych poza ekranem"""
    bullets.update()

    # usunięcie pocisków poza ekranem
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)