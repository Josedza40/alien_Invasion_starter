"""
Program Name: Alien Invasion - Battle Mode
Author: Jose Daniel Zambrano
Purpose: Manage bullet creation, movement, and drawing
         for normal and spread-shot firing modes.
Starter Code Links: https://github.com/RedBeard41/alien_Invasion_starter
Date Updated: November 14, 2026
"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    """Represent a projectile fired by the player's ship."""
    def __init__(self, game: 'AlienInvasion', direction_x = 0):
        """Initialize the bullet's position and settings."""
        super().__init__()
            
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image,
        (self.settings.bullet_w, self.settings.bullet_h)
        )
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.direction_x = direction_x


    def update(self):
            """Update the bullet's horizontal and vertical position."""
            self.y -= self.settings.bullet_speed
            self.x += self.direction_x * self.settings.spread_shot_speed
            
            self.rect.y = round(self.y)
            self.rect.x = round(self.x)

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)