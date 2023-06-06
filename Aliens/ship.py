#### Our Ship class to fight of aliens
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position at center of screen"""

        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image
        self.image = pygame.image.load('ship.bmp')
        # and get its rectangluar box attribute
        self.rect = self.image.get_rect()
        # Store screen's rect
        self.screen_rect = screen.get_rect()

        # Start each new ship at the botton center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a float value for the ship's center
        # Use this in update()
        self.h_center = float(self.rect.centerx)
        self.v_center = float(self.rect.centery)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        ## New feature
        self.moving_up = False
        self.moving_down = False



    def update(self):
        """Update ship's position based on movement flag."""

        # Block below updates ship's center value and not its rect. value
        if self.moving_right and (self.rect.right < self.screen_rect.right):
            self.h_center += self.ai_settings.ship_speed_factor

        if self.moving_left and (self.rect.left > 0):
            self.h_center -= self.ai_settings.ship_speed_factor

        if self.moving_down and (self.rect.bottom > 0) and (self.rect.bottom < self.screen_rect.bottom):
            self.v_center += self.ai_settings.ship_speed_factor

        if self.moving_up and (self.rect.top > self.screen_rect.top):
            self.v_center -= self.ai_settings.ship_speed_factor

        # Line below updates ship's rect. value
        # Stored as integer
        self.rect.centerx = self.h_center
        self.rect.centery = self.v_center

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)