#### Refactoring modules

import sys
import pygame

from bullets import Bullet
from alien import Alien
from ship import Ship


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
    # Key for exiting the game
    if event.key == pygame.K_q:
        sys.exit()





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
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)



def update_screen(ai_settings, screen, ship, bullets, aliens):
    """Updates images on the screen and flip to the new screen."""
    # Fill background color
    screen.fill(ai_settings.bg_color)
    # Method draws bullets behind Ship and Aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # Method below draws the ship onscreen
    ship.blitme()
    # Method draw() will draw the objects within group aliens
    # at positions defined by each objects rect. attribute
    aliens.draw(screen)
    # Make the most recent drawn screen visible.
    pygame.display.flip()


"""Refactoring create_fleet()"""

"""
#################### Revisit this block ####################
def get_number_aliens_x(ai_settings, screen ,ship, aliens):

    # Create one alien and find the number of aliens in one row
    alien = Alien(ai_settings, screen)

    # Store width of the alien
    alien_width = alien.rect.width
    # Store height of the alien
    alien_height = alien.rect.height

    # store ship height
    ship_height = ship.rect.height

    # calculate available space in one row
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    # calculate available space in one column

    available_space_y = ai_settings.screen_height - ( 3 * alien_height + ship_height )

    # Number of aliens in one row
    number_aliens_x = int( available_space_x / ( 2* alien_width) )

    # Number of rows
    number_of_rows = int(available_space_y / (2 * alien_height))
    # Creating a tuple
    alien_data = (number_aliens_x, alien_width, ship_height, number_of_rows, alien_height)

    return alien_data
"""

def get_number_aliens_x(ai_settings, alien_width):
    """ Determine the number of aliens in a row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in a row"""
    alien = Alien(ai_settings, screen)      # Instantiate Alien class
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, aliens ):
    """ Create a full fleet of aliens"""
    alien = Alien(ai_settings, screen)
    ship = Ship(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        # Outer loop creates the number of rows
        for alien_number in range(number_aliens_x):
            # Inner loop creates the number of aliens in one row
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
            # creates an alien

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that can fit on screen"""
    # Gets data from tuple of ship dimensions and alien dimensions
    available_space_y = (ai_settings.screen_height) - (3 * alien_height )  + ship_height
    # number of rows of aliens
    number_of_rows = int(available_space_y /(  2 * alien_height) )
    return number_of_rows


###### Functions to call alien movements
def update_aliens(aliens):
    """Update position of all aliens in the flwwt"""
    ### Call update() method in settings file
    aliens.update()

def check_fleet_edges(ai_settings, screen, alines):
    """respose to any aliens reaching an edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, screen, alines):
    """" Drop the enitre fleet and change fleet direction. """

    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, screen, aliens):
    check_fleet_edges(ai_settings, screen, aliens)
    aliens.update()



