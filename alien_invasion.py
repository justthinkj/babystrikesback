## TIY 1 ship appears in center, moving towards 4 directions

import sys
import pygame

# Enable doublebuffering
from pygame.locals import *
import time

# Debug
import pdb

from pygame.sprite import Group

from settings import Settings
from game_stats import Gamestats
from button import Button
from scoreboard import Scoreboard

from ship import Ship
from star import Star

from alien import Alien

# TIY 12.5
from ship_side import ShipSide

import game_functions as gf

def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()

    # Doublebuffering
    flags = FULLSCREEN | DOUBLEBUF

    screen = pygame.display.set_mode(
        (ai_settings.screen_width,
         ai_settings.screen_height))
    
    # Check speed
    # t = pygame.time.Clock()

    # Turn off alpha
    # screen.set_alpha(None)

    pygame.display.set_caption("Alien Invasion")

    # Make the play button
    play_button = Button(
        ai_settings, 
        screen, 
        "Play",
        (0,30))
    lost_button = Button(
        ai_settings, 
        screen, 
        "You lost! The baby is crying now!",
        (0, -50),
        (500, 50))

    # Create an instance to store game stats
    stats = Gamestats(ai_settings)

    # Make a ship
    ship = Ship(ai_settings, screen)    
    # Make a group to store bullets in.
    bullets = Group()

    # TIY 12.5
    shipSide = ShipSide(ai_settings, screen)
    # Make a group to store bullets in.
    bulletsSide = Group()

    # Make a group to store aliens
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    # TIY 13.3
    star = Star(ai_settings, 
                screen,
                ship,
                shipSide)

    # Debug:
    # timer_alien_update = 0

    # Make scoreboard object
    scoreboard = Scoreboard(ai_settings, screen, stats)

    # Start the main loop for the game.
    while True:

        # gf.check_events(ai_settings, screen, ship, bullets)
        # TIY 12.5
        gf.check_events125(
            ai_settings, screen, stats,
            ship, shipSide, 
            bullets, bulletsSide, play_button)

        if stats.game_active:
            gf.update_bullets(ai_settings, screen, stats,
                ship, aliens, bullets, bulletsSide, star)

            # TIY 12.5
            gf.update_bullets_side(ai_settings, screen, stats,
                ship, aliens, bullets, bulletsSide, star)

            # debug: lower update frequency
            # if timer_alien_update < 100:
            #     timer_alien_update += 1
            # else:
            #     timer_alien_update = 0

            gf.update_aliens(
                ai_settings, 
                screen,
                stats, 
                aliens, 
                ship,
                bullets, 
                shipSide,
                bulletsSide)

        try:
            star.update()
        except:
            print("no star")

        # gf.update_screen(ai_settings, screen, ship, bullets)
        # TIY 12.5
        gf.update_screen125(
            ai_settings,
            screen,
            stats,
            ship, shipSide, 
            bullets, bulletsSide,
            aliens,
            play_button,
            lost_button,
            scoreboard,
            star)

        # Check speed
        # t.tick()
        # print(t.get_fps())
        
run_game()

