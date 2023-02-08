import sys
from time import sleep
import pygame
from bullet import Bullet
from invader import Invader


def check_keydown_event(event, game_settings, screen, ship, bullets):
    """Reakcja na naciśnięcie klawisza"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

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

def check_events(game_settings, game_stats, screen, ship, invaders, bullets, play_button ):
    """Reakcja na zdarzenia generowane przez klawiaturę i mysz"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(game_settings, game_stats, screen, ship, invaders, bullets, play_button, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, game_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)

def check_play_button(game_settings, game_stats, screen, ship, invaders, bullets, play_button, mouse_x, mouse_y):
    """Rozpoczęcie nowej gry po kliknięciu przycisku Gra"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not game_stats.game_active:
        game_settings.initialize_dynamic_settings()
        run_new_game(game_settings, game_stats, screen, ship, invaders, bullets)

def run_new_game(game_settings, game_stats, screen, ship, invaders, bullets):
    pygame.mouse.set_visible(False)
    game_stats.reset_status()
    game_stats.game_active = True
    # usuwanie opcych i pocisków
    invaders.empty()
    bullets.empty()
    # utworzenie nowej floty i wyśrodkowanie statku
    create_fleet(game_settings, screen, ship, invaders)
def update_screen(game_settings, game_stats, screen, ship, invaders, bullets, play_button):
    """Uaktualnianie ekranu"""
    # odświeżanie ekranu
    screen.fill(game_settings.bg_color)
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    invaders.draw(screen)
    # wyświetlanie przycisku tylko gdy gra jest nieaktywna
    if not game_stats.game_active:
        play_button.draw_button()

    # wyświetlanie ostatniego ekranu
    pygame.display.flip()

def update_bullets(game_settings, screen, ship, bullets, invaders):
    """Uaktualnij położenie pocisków i usunięcie tych poza ekranem"""
    bullets.update()
    # usunięcie pocisków poza ekranem
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_invader_collision(game_settings, screen, ship, invaders, bullets)

def check_bullet_invader_collision(game_settings, screen, ship, invaders, bullets):
    # czy pocisk trafił obcego, jeśli tak usuwamy i pocisk i obcego
    collisions = pygame.sprite.groupcollide(bullets, invaders, True, True)
    # gdy wszyscy obcy znikną
    if len(invaders) == 0:
        # pozbycie się istniejących pocisków i wygenerowanie nowej floty
        bullets.empty()
        game_settings.incrace_speed()
        create_fleet(game_settings, screen, ship, invaders)

def update_invaders(game_settings, game_stats, screen, ship,  invaders, bullets):
    """Uaktualnienie położenia obcych"""
    check_fleet_edges(game_settings, invaders)
    invaders.update()
    # wykrycie zakończenia gry
    if pygame.sprite.spritecollideany(ship, invaders):
        ship_hit(game_settings, game_stats, screen, ship, invaders, bullets)
    check_invaders_bottom(game_settings, game_stats, screen, ship, invaders, bullets)

def ship_hit(game_settings, game_stats, screen, ship, invaders, bullets):
    """Reakcja na uderzenie obcego statku"""
    if game_stats.ships_left > 0:
        game_stats.ships_left -= 1
        # wyczyszczenie planszy
        invaders.empty()
        bullets.empty()
        # utworzenie nowej planszy
        create_fleet(game_settings, screen, ship, invaders)
        ship.center_ship()
        # czekanie pół sekundy
        sleep(0.5)
    else:
        game_stats.game_active = False
        pygame.mouse.set_visible(True)
def check_invaders_bottom(game_settings, game_stats, screen, ship, invaders, bullets):
    """Sprawdzenie czy którykolwiek statek obcych dotrarł do dolnej lini ekranu"""
    screen_rect = screen.get_rect()
    for invader in invaders:
        if invader.rect.bottom >= screen_rect.bottom:
            ship_hit(game_settings,game_stats, screen, ship, invaders,bullets)

def get_number_invader_x(game_settings, invader_width):
    """Ustalenie liczby obcych, którzy zmieszczą się w rzędzie"""
    available_space_x = game_settings.screen_width - 2 * invader_width
    number_invader_x = int(available_space_x / (2 * invader_width))
    return number_invader_x

def get_number_row(game_settings, ship_height, invader_height):
    """Ustalenie, ile rzędów obcych zmieści się na ekranie"""
    available_space_y = game_settings.screen_height - (3 * invader_height) - ship_height
    number_rows = int(available_space_y / (2 * invader_height))
    return number_rows

def create_invader(game_settings, screen, invaders, invader_number, row_number):
    """Stworzenie pojedynczego statku obcego"""
    invader = Invader(game_settings, screen)
    invader_width = invader.rect.width
    invader.x = invader_width + 2 * invader_width * invader_number
    invader.rect.x = invader.x
    invader.rect.y = invader.rect.height + 2 * invader.rect.height * row_number
    invaders.add(invader)
def create_fleet(game_settings, screen, ship, invaders):
    """Utworzenie floty obcych"""
    invader = Invader(game_settings, screen)
    invader_width = invader.rect.width
    number_invader_x = get_number_invader_x(game_settings, invader_width)
    number_rows = get_number_row(game_settings, ship.rect.height, invader.rect.height)

    for row_number in range(number_rows):
        for invader_number in range(number_invader_x):
            create_invader(game_settings, screen, invaders, invader_number, row_number)

def check_fleet_edges(game_settings, invaders):
    """Reakcja gdy obcy dotrze do krawędzi ekranu"""
    for invader in invaders.sprites():
        if invader.check_edges():
            change_fleet_direction(game_settings, invaders)
            break

def change_fleet_direction(game_settings, invaders):
    """Przesunięcie całej floty w dół i zmiana kierunku"""
    for invader in invaders.sprites():
        invader.rect.y += game_settings.fleet_drop_speed
    game_settings.fleet_direction *= -1

