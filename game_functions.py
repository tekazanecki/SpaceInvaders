import sys
from time import sleep
import pygame
from bullet import Bullet
from invader import Invader


def check_keydown_event(event, game_settings, screen, ship, bullets):
    """
    React to key presses.

    Args:
        event: The event object containing information about the key press.
        game_settings: An instance of the settings class containing game settings.
        screen: The screen surface where the game is displayed.
        ship: An instance of the Ship class representing the player's ship.
        bullets: A Group object to store all active bullets.
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_event(event, ship):
    """
    React to key releases.

    Args:
        event: The event object containing information about the key release.
        ship: An instance of the Ship class representing the player's ship.
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def fire_bullet(game_settings, screen, ship, bullets):
    """
    Fire a bullet if limit not reached yet.

    Args:
        game_settings: An instance of the settings class containing game settings.
        screen: The screen surface where the game is displayed.
        ship: An instance of the Ship class representing the player's ship.
        bullets: A Group object to store all active bullets.
    """
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)

def check_events(game_settings, game_stats, scoreboard, screen, ship, invaders, bullets, play_button):
    """
    Respond to keyboard and mouse events.

    Args:
        game_settings: An instance of the settings class containing game settings.
        game_stats: An instance of the GameStats class to track game statistics.
        scoreboard: An instance of the Scoreboard class to display the score.
        screen: The screen surface where the game is displayed.
        ship: An instance of the Ship class representing the player's ship.
        invaders: A Group object to store all active invaders.
        bullets: A Group object to store all active bullets.
        play_button: An instance of the Button class representing the Play button.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(game_settings, game_stats, scoreboard, screen, ship, invaders, bullets, play_button, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, game_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)

def check_play_button(game_settings, game_stats, scoreboard, screen, ship, invaders, bullets, play_button, mouse_x, mouse_y):
    """
    Start a new game when the Play button is clicked.

    Args:
        game_settings: An instance of the settings class containing game settings.
        game_stats: An instance of the GameStats class to track game statistics.
        scoreboard: An instance of the Scoreboard class to display the score.
        screen: The screen surface where the game is displayed.
        ship: An instance of the Ship class representing the player's ship.
        invaders: A Group object to store all active invaders.
        bullets: A Group object to store all active bullets.
        play_button: An instance of the Button class representing the Play button.
        mouse_x: The x-coordinate of the mouse click.
        mouse_y: The y-coordinate of the mouse click.
    """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not game_stats.game_active:
        game_settings.initialize_dynamic_settings()
        run_new_game(game_settings, game_stats, scoreboard, screen, ship, invaders, bullets)

def run_new_game(game_settings, game_stats, scoreboard, screen, ship, invaders, bullets):
    """
    Start a new game by resetting game settings and statistics, and creating a new fleet.

    Args:
        game_settings: An instance of the settings class containing game settings.
        game_stats: An instance of the GameStats class to track game statistics.
        scoreboard: An instance of the Scoreboard class to display the score.
        screen: The screen surface where the game is displayed.
        ship: An instance of the Ship class representing the player's ship.
        invaders: A Group object to store all active invaders.
        bullets: A Group object to store all active bullets.
    """
    pygame.mouse.set_visible(False)
    game_stats.reset_status()
    game_stats.game_active = True
    scoreboard.prep_score()
    scoreboard.prep_high_score()
    scoreboard.prep_level()
    invaders.empty()
    bullets.empty()
    create_fleet(game_settings, screen, ship, invaders)

def update_screen(game_settings, game_stats, scoreboard, screen, ship, invaders, bullets, play_button):
    """
    Update images on the screen and flip to the new screen.

    Args:
        game_settings: An instance of the settings class containing game settings.
        game_stats: An instance of the GameStats class to track game statistics.
        scoreboard: An instance of the Scoreboard class to display the score.
        screen: The screen surface where the game is displayed.
        ship: An instance of the Ship class representing the player's ship.
        invaders: A Group object to store all active invaders.
        bullets: A Group object to store all active bullets.
        play_button: An instance of the Button class representing the Play button.
    """
    screen.fill(game_settings.bg_color)
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    invaders.draw(screen)
    scoreboard.show_score()
    if not game_stats.game_active:
        play_button.draw_button()
    pygame.display.flip()

def update_bullets(game_settings, screen, game_stats, scoreboard, ship, bullets, invaders):
    """
    Update bullet positions and remove old bullets.

    Args:
        game_settings: An instance of the settings class containing game settings.
        screen: The screen surface where the game is displayed.
        game_stats: An instance of the GameStats class to track game statistics.
        scoreboard: An instance of the Scoreboard class to display the score.
        ship: An instance of the Ship class representing the player's ship.
        bullets: A Group object to store all active bullets.
        invaders: A Group object to store all active invaders.
    """
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_invader_collision(game_settings, screen, game_stats, scoreboard, ship, invaders, bullets)

def check_bullet_invader_collision(game_settings, screen, game_stats, scoreboard, ship, invaders, bullets):
    """
    Check for collisions between bullets and invaders.

    Args:
        game_settings: An instance of the settings class containing game settings.
        screen: The screen surface where the game is displayed.
        game_stats: An instance of the GameStats class to track game statistics.
        scoreboard: An instance of the Scoreboard class to display the score.
        ship: An instance of the Ship class representing the player's ship.
        invaders: A Group object to store all active invaders.
        bullets: A Group object to store all active bullets.
    """
    collisions = pygame.sprite.groupcollide(bullets, invaders, True, True)
    if collisions:
        for invaders in collisions.values():
            game_stats.score += game_settings.invader_points * len(invaders)
            scoreboard.prep_score()
        check_high_score(game_stats, scoreboard)
    if len(invaders) == 0:
        bullets.empty()
        game_settings.increase_speed()
        game_stats.level += 1
        scoreboard.prep_level()
        create_fleet(game_settings, screen, ship, invaders)

def update_invaders(game_settings, game_stats, scoreboard, screen, ship, invaders, bullets):
    """
    Update the positions of all invaders in the fleet.

    Args:
        game_settings: An instance of the settings class containing game settings.
        game_stats: An instance of the GameStats class to track game statistics.
        scoreboard: An instance of the Scoreboard class to display the score.
        screen: The screen surface where the game is displayed.
        ship: An instance of the Ship class representing the player's ship.
        invaders: A Group object to store all active invaders.
        bullets: A Group object to store all active bullets.
    """
    check_fleet_edges(game_settings, invaders)
    invaders.update()
    if pygame.sprite.spritecollideany(ship, invaders):
        ship_hit(game_settings, game_stats, scoreboard, screen, ship, invaders, bullets)
    check_invaders_bottom(game_settings, game_stats, scoreboard, screen, ship, invaders, bullets)

def ship_hit(game_settings, game_stats, scoreboard, screen, ship, invaders, bullets):
    """
    Respond to the ship being hit by an invader.

    Args:
        game_settings: An instance of the settings class containing game settings.
        game_stats: An instance of the GameStats class to track game statistics.
        scoreboard: An instance of the Scoreboard class to display the score.
        screen: The screen surface where the game is displayed.
        ship: An instance of the Ship class representing the player's ship.
        invaders: A Group object to store all active invaders.
        bullets: A Group object to store all active bullets.
    """
    if game_stats.ships_left > 0:
        game_stats.ships_left -= 1
        scoreboard.prep_ships()
        invaders.empty()
        bullets.empty()
        create_fleet(game_settings, screen, ship, invaders)
        ship.center_ship()
        sleep(0.5)
    else:
        game_stats.game_active = False
        pygame.mouse.set_visible(True)

def check_invaders_bottom(game_settings, game_stats, scoreboard, screen, ship, invaders, bullets):
    """
    Check if any invaders have reached the bottom of the screen.

    Args:
        game_settings: An instance of the settings class containing game settings.
        game_stats: An instance of the GameStats class to track game statistics.
        scoreboard: An instance of the Scoreboard class to display the score.
        screen: The screen surface where the game is displayed.
        ship: An instance of the Ship class representing the player's ship.
        invaders: A Group object to store all active invaders.
        bullets: A Group object to store all active bullets.
    """
    screen_rect = screen.get_rect()
    for invader in invaders:
        if invader.rect.bottom >= screen_rect.bottom:
            ship_hit(game_settings, game_stats, scoreboard, screen, ship, invaders, bullets)

def get_number_invader_x(game_settings, invader_width):
    """
    Determine the number of invaders that fit in a row.

    Args:
        game_settings: An instance of the settings class containing game settings.
        invader_width: The width of a single invader.

    Returns:
        int: The number of invaders that fit in a row.
    """
    available_space_x = game_settings.screen_width - 2 * invader_width
    number_invader_x = int(available_space_x / (2 * invader_width))
    return number_invader_x

def get_number_row(game_settings, ship_height, invader_height):
    """
    Determine the number of rows of invaders that fit on the screen.

    Args:
        game_settings: An instance of the settings class containing game settings.
        ship_height: The height of the player's ship.
        invader_height: The height of a single invader.

    Returns:
        int: The number of rows of invaders that fit on the screen.
    """
    available_space_y = game_settings.screen_height - (3 * invader_height) - ship_height
    number_rows = int(available_space_y / (2 * invader_height))
    return number_rows

def create_invader(game_settings, screen, invaders, invader_number, row_number):
    """
    Create a single invader and place it in the row.

    Args:
        game_settings: An instance of the settings class containing game settings.
        screen: The screen surface where the game is displayed.
        invaders: A Group object to store all active invaders.
        invader_number: The position number of the invader in the row.
        row_number: The position number of the row on the screen.
    """
    invader = Invader(game_settings, screen)
    invader_width = invader.rect.width
    invader.x = invader_width + 2 * invader_width * invader_number
    invader.rect.x = invader.x
    invader.rect.y = invader.rect.height + 2 * invader.rect.height * row_number
    invaders.add(invader)

def create_fleet(game_settings, screen, ship, invaders):
    """
    Create a fleet of invaders.

    Args:
        game_settings: An instance of the settings class containing game settings.
        screen: The screen surface where the game is displayed.
        ship: An instance of the Ship class representing the player's ship.
        invaders: A Group object to store all active invaders.
    """
    invader = Invader(game_settings, screen)
    invader_width = invader.rect.width
    number_invader_x = get_number_invader_x(game_settings, invader_width)
    number_rows = get_number_row(game_settings, ship.rect.height, invader.rect.height)

    for row_number in range(number_rows):
        for invader_number in range(number_invader_x):
            create_invader(game_settings, screen, invaders, invader_number, row_number)

def check_fleet_edges(game_settings, invaders):
    """
    Respond if any invaders have reached an edge.

    Args:
        game_settings: An instance of the settings class containing game settings.
        invaders: A Group object to store all active invaders.
    """
    for invader in invaders.sprites():
        if invader.check_edges():
            change_fleet_direction(game_settings, invaders)
            break

def change_fleet_direction(game_settings, invaders):
    """
    Move the entire fleet down and change the fleet's direction.

    Args:
        game_settings: An instance of the settings class containing game settings.
        invaders: A Group object to store all active invaders.
    """
    for invader in invaders.sprites():
        invader.rect.y += game_settings.fleet_drop_speed
    game_settings.fleet_direction *= -1

def check_high_score(game_stats, scoreboard):
    """
    Check if there's a new high score.

    Args:
        game_stats: An instance of the GameStats class to track game statistics.
        scoreboard: An instance of the Scoreboard class to display the score.
    """
    if game_stats.score > game_stats.high_score:
        game_stats.high_score = game_stats.score
        scoreboard.prep_high_score()
