## Class for making Aliens
## will contain the behavior of each alien

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ai_settings, screen):

        """Making one alien..."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load alien image
        self.image = pygame.image.load('alien.bmp')
        #get rect. attributes of the alien using get_rect() method
        self.rect = self.image.get_rect()

        # Position of one alien
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien's location
        self.x = float(self.rect.x)


    def blitme(self):
        """Function to draw aliens at its current location"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True is alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move aliens to right or left"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x