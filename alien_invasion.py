"""
Program Name: Alien Invasion - Battle Mode
Author: Jose Daniel Zambrano
Purpose: Run the main game loop, process keyboard input,
         update the ship and weapons, and draw the game screen.
Starter Code Links: https://github.com/RedBeard41/alien_Invasion_starter
Date Updated: November 14, 2026
"""



import sys
import pygame
from settings import Settings
# from game_stats import GameStats
from ship import Ship
from arsenal import Arsenal
# from alien import Alien
# from alien_fleet import AlienFleet
# from time import  sleep
# from button import Button
# from hud import HUD

class AlienInvasion:
    """Manage the main game loop, events, and game components."""
    def __init__(self):
        """Initialize the game and its main components.

    Set up Pygame, the game window, background, sounds,
    player ship, and weapon system for Milestone 1."""
        pygame.init()
        self.settings = Settings()
        self.settings.initialize_dynamic_settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w,self.settings.screen_h)
            )
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg,
            (self.settings.screen_w, self.settings.screen_h)
            )
        #Milestone2/Final: Game stats and HUD
        # self.game_stats = GameStats(self)
        # self.HUD = HUD(self)
        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7)

        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound.set_volume(0.7)

        self.ship = Ship(self, Arsenal(self))
        # Milestone 2: Alien Fleet
        # self.alien_fleet = AlienFleet(self)
        # self.alien_fleet.create_fleet()

        # Final Submission: Play Button and game states
        # self.play_button = Button(self, 'Play')
        self.game_active = True

    def run_game(self):
        """Run the main game loop and continuously update the screen."""
        #Game loop
        while self.running:
            self._check_events()
            if self.game_active:
                self.ship.update()

                if self.ship.arsenal.update_rapid_fire():
                    self.laser_sound.play()
                    self.laser_sound.fadeout(250)

                # Milestone 2: Fleet and collision logic
                # self.alien_fleet.update_fleet()
                # self._check_collisions()
                
                
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collisions(self):
        """Check collisions between the ship, aliens, and bullets."""
        #check collisions for ship 
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._check_game_status()
            #subtract one life if possible

        #check collisions for aliens and bottom of screen
        if self.alien_fleet.check_fleet_bottom():
            self._check_game_status()
        #check collisisons projectiles and aliens
        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)
            self.game_stats.update(collisions)
            self.HUD.update_scores()

        if self.alien_fleet.check_destroyed_status():
            self._reset_level()
            self.settings.increase_difficulty()
            # update game stats level
            self.game_stats.update_level()
            # update HUD view 
            self.HUD._update_level()   

    def _check_game_status(self):
        """Update remaining lives and determine whether the game ends."""
        if self.game_stats.ship_left > 0:
            self.game_stats.ship_left -= 1
            self._reset_level()
            # sleep(0.5)
        else:
            self.game_active = False    
        
        
        


    def _reset_level(self):
        """Clear existing bullets and rebuild the alien fleet."""
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()

    def restart_game(self):
        """Reset the game and begin a new session."""
        self.settings.initialize_dynamic_settings()
        self.game_stats.reset_stats()
        self.HUD.update_scores()
        self._reset_level()
        self.ship._center_ship()
        self.game_active = True
        pygame.mouse.set_visible(False)      



    def _update_screen(self):
        """Draw the Milestone 1 prototype."""
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        # Milestone 2: Alien Fleet
        # self.alien_fleet.draw()

        # Final Submission: HUD and Play Button 
        # self.HUD.draw()
        # if not self.game_active:
        #    self.play_button.draw()
        #    pygame.mouse.set_visible(True)

        pygame.display.flip()


    def _check_events(self):
        """Process keyboard, mouse, and window events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                # self.game_stats.save_scores()
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and self.game_active == True:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            # Final Submission: Play button    
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #    self._check_button_clicked() 

    def _check_button_clicked(self):
        """Check whether the player clicked the Play button."""
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos):
            self.restart_game()   

    def _check_keyup_events(self, event):
        """Stop movement or rapid fire when keys are released."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False 
        elif event.key == pygame.K_r:
            self.ship.arsenal.rapid_fire_active = False

    def _check_keydown_events(self, event):
        """Handle key presses for movement and weapon controls."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)
        elif event.key == pygame.K_s:
            if self.ship.fire_spread():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)
        elif event.key == pygame.K_r:
            self.ship.arsenal.rapid_fire_active = True                
        elif event.key == pygame.K_q:
            self.running = False
            # self.game_stats.save_scores()
            pygame.quit()
            sys.exit()    

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
