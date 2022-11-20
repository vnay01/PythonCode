#### Refactoring modules

import sys
import pygame

from bullets import Bullet


"""Refactoring check_events()"""

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses"""
    if event.key == pygame.K_RIGHT:
        # Move ship to the right
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_SPACE:
        # Limiting the number of bullets
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)




def check_keyup_events(event, ship):
    """ Respond to key releases"""
    # Used to move ship in steps
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False
    if event.key == pygame.K_UP:
        ship.moving_up = False



def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)



def update_screen(ai_settings, screen, ship, bullets):
    """Updates images on the screen and flip to the new screen."""
    # Fill background color
    screen.fill(ai_settings.bg_color)
    # Method draws bullets behind Ship and Aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # Method below draws the ship onscreen
    ship.blitme()
    # Make the most recent drawn screen visible.
    pygame.display.flip()