import sys
import pygame
from time import sleep

from bullet import Bullet
# TIY 12.5
from bullet_side import BulletSide

from alien import Alien
import pdb

def check_events(ai_settings,
        screen,
        stats,
        ship,
        bullets,
        play_button):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            game_end_actions(stats)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,
                ai_settings,
                screen, 
                ship,
                bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if play_button.rect.collidepoint(mouse_x, mouse_y):
                stats.game_active = True


# TIY 125
def check_events125(ai_settings,
        screen,
        stats,
        ship,
        shipSide,
        bullets,
        bulletsSide,
        play_button):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            game_end_actions(stats)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events125(event,
                ai_settings,
                screen, 
                stats,
                ship,
                shipSide,
                bullets,
                bulletsSide)
        elif event.type == pygame.KEYUP:
            check_keyup_events125(event, ship, shipSide)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if play_button.rect.collidepoint(
                mouse_x, 
                mouse_y) and not stats.game_active:
                stats.game_active = True
                stats.game_end = False


def check_keydown_events(event, 
        ai_settings,
        screen,
        stats,
        ship,
        bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,
            screen,
            ship,
            bullets)
    elif event.key == pygame.K_p:
        stats.game_active = True
    elif event.key == pygame.K_q:
        game_end_actions(stats)


    ## TIY-1
    """
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    """

# TIY 125
def check_keydown_events125(event, 
        ai_settings,
        screen,
        stats,
        ship,
        shipSide,
        bullets,
        bulletsSide):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,
            screen,
            ship,
            bullets)
    elif event.key == pygame.K_UP:
        shipSide.moving_up = True
    elif event.key == pygame.K_DOWN:
        shipSide.moving_down = True
    elif event.key == pygame.K_k:
        fire_bullet_side(ai_settings,
            screen,
            shipSide,
            bulletsSide)
    elif event.key == pygame.K_p:
        stats.game_active = True
    elif event.key == pygame.K_q:
        game_end_actions(stats)


def game_end_actions(stats):
    """Actions to take when the game ends."""
    stats.write_all_time_high_score()
    sys.exit() 


def check_keyup_events(event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

    ## TIY-1
    """
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    """


# TIY 125
def check_keyup_events125(event, ship, shipSide):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        shipSide.moving_up = False
    elif event.key == pygame.K_DOWN:
        shipSide.moving_down = False


def update_screen(ai_settings, 
        screen, 
        ship,
        bullets,
        aliens):
    """Update images on the screen and flip to the new screen."""

    # Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    
    # Redraw all bullets behind ship and aliens
    for bullet in bullets:
        bullet.draw_bullet()

    ship.blitme()
    
    ship.update()

    aliens.update()
    # Make the most recently drawn screen visible
    pygame.display.flip()


# TIY 12.5
def update_screen125(ai_settings, 
        screen,
        stats, 
        ship,
        shipSide,
        bullets,
        bulletsSide,
        aliens,
        play_button,
        lose_button,
        scoreboard,
        star=''):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    
    # Redraw all bullets behind ship and aliens
    for bullet in bullets:
        bullet.draw_bullet()

    # Redraw all bullets behind ship and aliens
    for bullet in bulletsSide:
        bullet.draw_bullet()

    ship.blitme()
    ship.update()

    shipSide.blitme()
    shipSide.update()

    for alien in aliens:
        alien.blitme()

    # Turn on the star if it exists
    if star !='':
        star.blitme()

    if not stats.game_active:
        play_button.draw_button()
        pygame.mouse.set_visible(True)
    else:
        pygame.mouse.set_visible(False)

    if stats.game_end:
        lose_button.draw_button()

    scoreboard.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()


def check_and_repopulate_fleet(ai_settings,
                               screen,
                               stats,
                               ship,
                               aliens,
                               bullets,
                               bulletsSide):
    """Check if aliens are all hit and repopulate if so."""
    # Destroy existing bullets, speed up game and create new fleet.
    if len(aliens) == 0:
        bullets.empty()
        bulletsSide.empty()
        ai_settings.increase_speed()
        stats.level += 1
        create_fleet(ai_settings, screen, ship, aliens)


def update_bullets(ai_settings, 
                   screen,
                   stats,
                   ship, 
                   aliens, 
                   bullets, 
                   bulletsSide,
                   star=None):
    """Update position of bullets and get rid of the old bullets."""

    # Update bullet positions.
    bullets.update()

    # Get rid of bullets that have disappered
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    collisons = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(collisons) > 0:
        #print(collisons)
        stats.score += len(collisons)*ai_settings.alien_points

    if star:
        bulletHit = pygame.sprite.spritecollideany(star, bullets)
        if bulletHit:
            bullets.remove(bulletHit)

    check_and_repopulate_fleet(ai_settings,
                               screen,
                               stats,
                               ship,
                               aliens,
                               bullets,
                               bulletsSide)


def fire_bullet(ai_settings,
        screen,
        ship,
        bullets):
    """Fire a bullet if limit is not reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_bullets_side(ai_settings, 
                        screen, 
                        stats,
                        ship, 
                        aliens, 
                        bullets, 
                        bulletsSide,
                        star=None):
    """Update position of bullets and get rid of the old bullets."""

    # Update bullet positions.
    bulletsSide.update()

    # Get rid of bullets that have disappered
    for bullet in bulletsSide.copy():
        if bullet.rect.right <= 0:
            bulletsSide.remove(bullet)
    
    collisons = pygame.sprite.groupcollide(bulletsSide, aliens, True, True)

    if len(collisons) > 0:
        stats.score += len(collisons)*ai_settings.alien_points

    if star:
        bulletHit = pygame.sprite.spritecollideany(star, bulletsSide)
        if bulletHit:
            bulletsSide.remove(bulletHit)

    check_and_repopulate_fleet(ai_settings,
                               screen,
                               stats,
                               ship,
                               aliens,
                               bullets,
                               bulletsSide)


def fire_bullet_side(ai_settings,
        screen,
        shipSide,
        bulletsSide):
    """Fire a bullet if limit is not reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bulletsSide) < ai_settings.bullets_side_allowed:
        new_bullet = BulletSide(ai_settings, screen, shipSide)
        bulletsSide.add(new_bullet)


def get_number_aliens_x(ai_settings, screen, alien):
    """Determine the number of aliens which fit in a row."""
    available_space_x = \
        ai_settings.screen_width - ai_settings.fleet_spacing_factor_x * alien.rect.width
    alien_spacing_x = ai_settings.fleet_spacing_factor_x * alien.rect.width
    return int(available_space_x / alien_spacing_x)


def get_number_aliens_y(ai_settings,
                        screen,
                        ship,
                        alien):
    """Determine the number of rows for aliens."""
    available_space_y = \
        ai_settings.screen_height - \
        ai_settings.fleet_spacing_factor_x * alien.rect.height - ship.rect.height
    alien_spacing_y = ai_settings.fleet_spacing_factor_y * alien.rect.height
    return int(available_space_y / alien_spacing_y)


def create_alien(ai_settings,
                screen, 
                aliens, 
                number_aliens_x,
                number_aliens_y):
    """Create an alien and place it in the row."""
    for j in range(number_aliens_y):
        for i in range(number_aliens_x):
            alien = Alien(ai_settings, screen)
            alien_width = alien.rect.width
            alien_height = alien.rect.height
            alien.x = \
                alien_width + i * ai_settings.fleet_spacing_factor_x * alien_width
            alien.y = \
                alien_height*2 + j * ai_settings.fleet_spacing_factor_y * alien_height
            alien.rect.x = alien.x
            alien.rect.y = alien.y
            aliens.add(alien) 


def create_fleet(ai_settings, screen, ship, aliens):
    """Create a fleet of aliens."""
    alien = Alien(ai_settings, screen)

    number_aliens_x = get_number_aliens_x(ai_settings,
        screen,
        alien)

    number_aliens_y = get_number_aliens_y(ai_settings,
        screen,
        ship,
        alien)

    create_alien(ai_settings, 
                screen,
                aliens,
                number_aliens_x,
                number_aliens_y)


def check_fleet_edges(ai_settings, aliens, shipSide=""):
    """Respond appropriately if any alien has reached the edge."""
    for alien in aliens.sprites():
        if alien.check_edges(shipSide):
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed

    ai_settings.fleet_direction *= -1


def ship_hit(
    ai_settings,
    screen,
    stats,
    aliens,
    ship, 
    bullets,
    shipSide='', 
    bulletsSide=''):
    """Handle the event when ship is hit."""

    # Subtract one ship
    if stats.ships_left > 0:
        stats.ships_left -= 1
    else:
        stats.game_active = False
        if stats.score > stats.high_score:
            stats.high_score = stats.score
        if stats.score > stats.all_time_high_score:
            stats.all_time_high_score = stats.score
        stats.game_end = True
        stats.reset_stats()
        ai_settings.initialize_dynamic_settings()

    # Destory all existing aliens
    aliens.empty()

    # Destory all bullets
    bullets.empty()
    if bulletsSide != '':
        bulletsSide.empty()

    create_fleet(
        ai_settings,
        screen,
        ship,
        aliens)

    ship.__init__(ai_settings, screen)
    if shipSide != '':
        shipSide.__init__(ai_settings, screen)

    # Freeze the screen for 1 sec to show the hit
    sleep(1)


def check_aliens_bottom(screen,
                        aliens):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()

    alien_hit_bottom = False

    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            alien_hit_bottom = True
    
    return alien_hit_bottom


def update_aliens(ai_settings, 
                  screen,
                  stats, 
                  aliens, 
                  ship, 
                  bullets, 
                  shipSide="",
                  bulletsSide=""):
    """
    Check if the fleet is at an edge,
    and update the position of all aliens in the fleet.
    """
    check_fleet_edges(ai_settings, aliens, shipSide)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens) or \
        check_aliens_bottom(screen, aliens):
        #print('before hit: '+str(stats.ships_left))
        ship_hit(ai_settings,
            screen,
            stats, 
            aliens, 
            ship, 
            bullets,
            shipSide,
            bulletsSide)
        #print('after hit: '+str(stats.ships_left))

