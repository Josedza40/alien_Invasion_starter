import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Arsenal:
    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        self.arsenal.update()
        self._remove_bullets_off_screen()

    def _remove_bullets_off_screen(self):
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self):
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):
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