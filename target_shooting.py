# -*- coding: utf-8 -*-
"""
Spyder Editor

Target shooting project
"""

import sys

import pygame
import time

#from settings import Settings
from actor import Actor
from targeting import getTargetPosition, calcBulletDirection

from settings import Settings

class TargetShooting:
    """Overall class etc"""
    
    def __init__(self):
        """Initialize the game"""
        pygame.init()
        
        self.settings = Settings()
#        s = self.settings

        screen_width = self.settings.screen_width
        screen_height = self.settings.screen_height
        
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Target Shooting")
        
        self.bullet = Actor(self)
        #self.bullet.set_position(100, 100)
        self.target = Actor(self)
        
        self.time_start = time.time()
        self.time = 0
        
    def _check_events(self):
        running = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    
            return running
        
        #unused part with controls
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                if event.key == pygame.K_SPACE:
                    self.ship.fire_bullet()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
        return running
    
    def _update_screen(self):
        
        bg_color = (230,230,230)
        
        self.screen.fill(bg_color)
        #self.bullet.update()
        #screen_x, screen_y = getTargetPosition(time)
        
        bullet_x = int(self.settings.bullet_start_x + self.bulletVx*self.time)
        bullet_y = int(self.settings.bullet_start_y + self.bulletVy*self.time)
        
        #bullet_x = 500
        #bullet_y = 150
        
        self.bullet.set_position(bullet_x, bullet_y)
        self.bullet.draw()

        screen_x, screen_y = getTargetPosition(self.time)        
        #self.target.update()
        self.target.set_position(screen_x, screen_y)
        self.target.draw()
        
        pygame.display.flip()
        
        self.time = time.time() - self.time_start
        
    def run_game(self):
        """Game main loop"""
        
        kx, ky = calcBulletDirection()
        self.bulletVx = self.settings.bullet_speed*kx
        self.bulletVy = self.settings.bullet_speed*ky
        
        running = True
        while running:
            running = self._check_events()
            self._update_screen()
        pygame.quit()
            
if __name__ == '__main__':
    ai = TargetShooting()
    ai.run_game()
