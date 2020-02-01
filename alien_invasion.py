import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """ Overall class to manage game assets and behavior """

    def __init__(self):
        """ Initialize the game and creates game resources. """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def _create_fleet(self):
        """ Create the fleet of aliens """
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens = available_space_x // ( 2 * alien_width)

        available_space_y = self.settings.screen_height - (3 * alien_height) - self.ship.rect.height
        number_rows = available_space_y // (2 * alien_height)

        for row in range(number_rows):
            for alien_number in range(number_aliens):
                self._create_alien(alien_number, row)

    def _create_alien(self, alien_number, row_number):
        """ Create alien and add it in the row """ 
        fleet_alien = Alien(self)
        alien_width, alien_hieght = fleet_alien.rect.size
        fleet_alien.x = alien_width + 2 * alien_width * alien_number
        fleet_alien.y = alien_hieght + 2 * alien_hieght * row_number
        fleet_alien.rect.x = fleet_alien.x
        fleet_alien.rect.y = fleet_alien.y
        self.aliens.add(fleet_alien)

    def run_game(self):
        """ Start the main loop for the game """
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self.aliens.update()
            self._update_screen()
            self.delete_not_needed_bullets()
    
    def delete_not_needed_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_events(self):
        """ Respond to keypressed and mouse events """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
               self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
               self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """ Respond to keypresses """
        if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """" Redraw the screen during each pass trough the loop """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self._update_bullets()
        self._update_aliens()
        
        # Make the most recently drawn screen visible
        pygame.display.flip()

    def _update_bullets(self):
        for bullet in self.bullets:
            bullet.draw_bullet()
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # Check for any bullets that have hit aliens
        # If so, get rid of the bullets and of the aliens
        pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """ Updates the position of all aliens in the fleet """
        self._check_fleet_edges()
        self.aliens.draw(self.screen)
    
    def _check_fleet_edges(self):
        """ Respond appropriately if any aliens have reached an edge. """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """ Drop the entire ship and change the fleet's direction """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien_down_speed
        self.settings.fleet_direction *= -1 

    def set_fullscreen(self):
        """ Sets the game in fullscreen mode """
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

if __name__ == "__main__":
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()