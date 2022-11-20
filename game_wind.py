# Creating a Pygame Window and Responding to user input

#### Imports ####
import sys
import pygame
from pygame.sprite import Group

##### User created module import
import game_functions as gf
from settings import Settings
from ship import Ship
from bullets import Bullet



#### Function ####
def run_game():
    ## Initialize game and create a screen object.
    pygame.init()


    # Create instance of Settings class and store it in ai_settings
    ai_settings = Settings()
    ## Line below represents entire game window
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    #screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    # Set background color ( R, G, B )
    screen.fill(ai_settings.bg_color)


    # Make a ship
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets in.
    bullets = Group()

    ## Start main loop for the game.
    while True:

        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings,screen, ship, bullets)
        ship.update()
        bullets.update()

        # getting rid of used bullets
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        # Updates screen
        gf.update_screen(ai_settings, screen, ship, bullets)

#### Testing whether game screen code is correct ####
run_game()