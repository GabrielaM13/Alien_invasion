import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ This class deals with the logic behind shooting bullets """ 

    def __init__(self, ai_game):
        """ Create a bullet object at the ship's current position """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        """
        # Create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        """
       
        # Load the ship image and set its rect
        img_path = self.settings._get_relative_path("images/bullet.bmp")
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()


        # Start each new ship at the bottom center of the screen
        self.rect.midtop =  ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def draw_bullet(self):
        # pygame.draw.rect(self.screen, self.color, self.rect)
        self.blitme()

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def blitme(self):
        """ Draw the ship at its current position """
        self.screen.blit(self.image, self.rect)