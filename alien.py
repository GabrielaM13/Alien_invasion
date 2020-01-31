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
        """ 
        if self.is_moving_right and self.rect.x < self.screen_rect.right:
            self.x += self.settings.alien_speed
            self.rect.x = self.x
        elif (self.is_moving_right and self.rect.x == self.screen_rect.right) or (not self.is_moving_right and self.rect.x == 0):
            self.y += self.settings.alien_down_speed
            self.rect.y = self.y
            if self.is_moving_right:
                self.is_moving_right = False
            else:
                self.is_moving_right = True
        elif self.is_moving_right == False and self.rect.x > 0:
            self.x -= self.settings.alien_speed
            self.rect.x = self.x
        """