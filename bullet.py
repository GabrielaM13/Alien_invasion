import pygame

class Bullet:
    """ This class deals with the logic behind shooting bullets """ 

    def __init__(self, ship):
        self.screen = ship.screen
        self.screen_rect = ship.screen.get_rect()
        self.settings = ship.settings

        # Load the ship image and set its rect
        img_path = self.settings._get_relative_path("images/bullet.bmp")
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y = ship.rect.top

    def shoot(self):
        """ Shoots the bullet"""
        while self.rect.y < 1300:
            self.update()
            self.blitme()

    def update(self):
        self.rect.y += 1

    def blitme(self):
        """ Draw the ship at its current position """
        self.screen.blit(self.image, self.rect)