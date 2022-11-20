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
        self.bullet_speed_factor = 0.5
        self.bullet_width =  3
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 3
