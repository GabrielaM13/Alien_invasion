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
       
        self.initialize()

        # Start each new ship at the bottom center of the screen
        self.rect.midtop =  ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def initialize(self):
        if self.settings.bullet_type == "sprite":
            self.initialize_sprite()
        else:
            self.initialize_image()

    def initialize_sprite(self):
         # Create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)

    def initialize_image(self):
        # Load the ship image and set its rect
        if self.settings.bullet_type == "rock":
            img = "images/rock.bmp"
        elif self.settings.bullet_type == "heart":
            img = "images/heart.bmp"
        img_path = self.settings._get_relative_path(img)
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()

    def draw_bullet(self):
        if self.settings.bullet_type == "sprite":
           pygame.draw.rect(self.screen, self.color, self.rect)
        else:
            self.blitme()

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def blitme(self):
        """ Draw the ship at its current position """
        self.screen.blit(self.image, self.rect)