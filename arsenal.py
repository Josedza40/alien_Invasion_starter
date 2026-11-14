"""
Program Name: Alien Invasion - Battle Mode
Author: Jose Daniel Zambrano
Purpose: Manage the player's bullets, including normal firing,
         spread shots, rapid fire, and bullet cleanup.
Starter Code Links: https://github.com/RedBeard41/alien_Invasion_starter
Date Updated: November 14, 2026
"""

import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Arsenal:
    """Manage the creation, movement, and removal of player bullets."""
    def __init__(self, game: 'AlienInvasion'):
        """Initialize the arsenal, bullet group, and firing controls."""
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()
        self.last_rapid_shot = 0
        self.rapid_fire_active = False

    def update_arsenal(self):
        """Update the position and remove off-screen bullets."""
        self.arsenal.update()
        self._remove_bullets_off_screen()

    def _remove_bullets_off_screen(self):
        """Remove bullets that leave any side of the screen."""
        for bullet in self.arsenal.copy():
            if (
                bullet.rect.bottom <= 0
                or bullet.rect.right <= 0
                or bullet.rect.left >= self.settings.screen_w
            ):
                self.arsenal.remove(bullet)

    def draw(self):
        """Draw all active bullets on the game screen."""
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):
        """Fire a normal bullet if the bullet limit allows it."""
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False
    
    def fire_spread_shot(self):
        """Fire three bullets in different directions."""
        directions = [-1, 0, 1]

        if len(self.arsenal) + len(directions) <= self.settings.bullet_amount:
            for direction in directions:
                new_bullet = Bullet(self.game, direction_x=direction)
                self.arsenal.add(new_bullet)
            return True
        return False
    
    def update_rapid_fire(self):
        """Fire repeatedly while rapid fire is active."""
        if not self.rapid_fire_active:
            return False
        current_time = pygame.time.get_ticks()
        if current_time - self.last_rapid_shot >= self.settings.rapid_fire_delay:
            if self.fire_bullet():
                self.last_rapid_shot = current_time
                return True
        return False
