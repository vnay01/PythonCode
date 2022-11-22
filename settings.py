#### Contains 'class' used throughout the game
#### Imported as module in main file

##### Creating Settings class

class Settings():
    """Class to store all settings for the game."""

    def __init__(self):
        """Initializa game's settings."""

        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        # Ship controls
        # Use it to change tempo of game!
        self.ship_speed_factor = 1.25

        # Ship Weapons
        ## Bullets
        self.bullet_speed_factor = 1
        self.bullet_width =  3
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 3000

        # Alien Settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def update(self):
        """Method will be used to move the fleet"""
        # Adds and Stores speed factor in a variable
        self.x += self.ai_settings.alien_speed_factor
        # Updates current 'x' position with speed factor
        self.rect.x = self.x
