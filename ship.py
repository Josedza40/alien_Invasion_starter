"""
Program Name: Alien Invasion - Battle Mode
Author: Jose Daniel Zambrano
Purpose: Control the player's ship movement, position,
         firing methods, and collision detection.
Starter Code Links: https://github.com/RedBeard41/alien_Invasion_starter
Date Updated: November 14, 2026
"""


import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:
    """Represent the player's ship and manage its movements and weapons."""

    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal'):
        """Initialize the ship, its position, and weapon system."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.ship_w, self.settings.ship_h)
            )
        self.rect = self.image.get_rect()
        self._center_ship()
        self.moving_right = False
        self.moving_left = False
        self.arsenal = arsenal

    def _center_ship(self):
        """Position the ship at the bottom center of the screen."""
        self.rect.midbottom = self.boundaries.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """Update the ship's position and active bullets."""
        # updating the position of the ship
        self._update_ship_movement()
        self.arsenal.update_arsenal() 

    def _update_ship_movement(self):
        """Move the ship left or right within the screen boundaries."""
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        self.rect.x = self.x       

    def draw(self):
        """Draw the ship and its active bullets on the screen."""
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)    

    def fire(self):
        """Request a normal bullet from the arsenal."""
        return self.arsenal.fire_bullet()

    def fire_spread(self):
        """Tell the arsenal to fire a spread shot."""
        return self.arsenal.fire_spread_shot()

    # def check_collisions(self, other_group):
      #  """Check whether the ship has collided with an enemy."""
       # if pygame.sprite.spritecollideany(self, other_group): 
        #    self._center_ship()
         #   return True
        # return False
