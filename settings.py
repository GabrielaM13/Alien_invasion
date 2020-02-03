import os


class Settings:
    """ A class that stores all settings for Alien Invasion """

    def __init__(self):
        """ Intialize the game"s static settings """

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_limit = 3

        # Bullet settings
        self.bullet_types = ["sprite", "rock", "heart"]
        self.bullet_type = "heart"
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_down_speed = 10 

        # How quickly the game speeds up
        self.speed_up_scale = 1.5
        self.initialize_dynamic_settings()

        # How quickly the alien point values increase
        self.score_scole = 1.5

    def _get_relative_path(self, path):
        base_path = os.path.dirname(__file__)
        relative_path = os.path.join(base_path, path)
        return relative_path

    def initialize_dynamic_settings(self):
        """ Initialize settings that change throughout the game """
        self.ship_speed = 1.5
        self.bullet_speed = 1.0
        self.alien_speed = 0.5

        # fleet direction of 1 represent right: -1 represents left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """ Increade speed settings and alien point values """
        self.ship_speed *= self.speed_up_scale
        self.bullet_speed *= self.speed_up_scale
        self.alien_speed *= self.speed_up_scale
        self.alien_points = int(self.alien_points * self.score_scole)