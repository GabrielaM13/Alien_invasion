import pygame
import os

class Ship:
    """ A class to manage the ship. """

    def __init__(self, ai_game):
        """ Initialize the ship and set its starting position """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and set its rect
        img_path = self.get_relative_path("images/ship.bmp")
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.rect.x += 1
        elif self.moving_left and self.rect.x > 0:
            self.rect.x -= 1

    def blitme(self):
        """ Draw the ship at its current position """
        self.screen.blit(self.image, self.rect)

    def get_relative_path(self, path):
        base_path = os.path.dirname(__file__)
        relative_path = os.path.join(base_path, path)
        return relative_path