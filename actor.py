# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 22:11:49 2023

@author: minmod
"""
import pygame

import math

class Actor:
    
    def __init__(self, ai_game):
        
        self.ai_game = ai_game
        
        self.screen = ai_game.screen
        
        self.screen_rect = ai_game.screen.get_rect()
        
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        self.rect.midbottom = self.screen_rect.midbottom
        
        self.moving_right = False
        
        self.moving_left = False
        
        self.x = float(self.rect.x)
        
        self.can_shoot = True
        
        self.bullets = []
        
    def set_position(self, screen_x, screen_y):
        
        self.rect.x = screen_x
        self.rect.y = screen_y
        
    def move(self):
        
        speed_x = 0.1*math.cos(self.ai_game.time)
        speed_y = 0.25
        
        self.x += speed_x
        
        if self.moving_right:
            self.x += speed_x
            
        if self.moving_left:
            self.x -= speed_x
        
        max_x = self.screen.get_width() - self.rect.width
        
        if self.x < 0: self.x = 0
        if self.x > max_x : self.x = max_x
    
    
    def update(self):
        self.move()

    
    def draw(self):
        # blit : draw one image onto another
        #self.rect.x = self.x
        self.screen.blit(self.image, self.rect)
        