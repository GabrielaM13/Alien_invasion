import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """ This class displays and a alien """

    def __init__(self, ai_game):
        """ A class to represent a single alien in the fleet """
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the ship image and set its rect
        img_path = self.settings._get_relative_path("images/alien.png")
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.is_moving_right = True
    
    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """ Return true if alien is at the edge of the screen """ 
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            return True
