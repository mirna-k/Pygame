import pygame
import os
from Support import *


class Block(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))


class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height, x_pos, y_pos, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos


class Player(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, speed, state):
        super().__init__()
        self.import_character_assets()
        self.currentSprite = 0
        self.animation_speed = 0.25
        self.image = self.animations['idle'][self.currentSprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x_pos, y_pos)
        
        self.speed = speed
        self.movement = 0
        self.state = state

        if self.state == 'idle':
            self.idle_state = True
            self.run_state = False

        if self.state == 'run':
            self.idle_state = False
            self.run_state = True

    def import_character_assets(self):
        path = 'raccoon/'
        self.animations = {'idle':[],'run':[],'jump':[]}
        
        for animation in self.animations.keys():
            full_path = path + animation
            self.animations[animation] = import_images_from_folder(full_path)


    def animation(self):






        if (self.idle_state == True):
            self.image = self.idle[self.currentSprite]
            
        elif (self.run_state == True):
            self.image = self.run[self.currentSprite]
            self.rect = self.image.get_rect()
            self.rect.bottomleft = (x_pos, y_pos)
        
    def update(self):
        self.rect.x += self.movement
        if self.rect.left > 900:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = 900


        if self.idle_state == True and int(self.currentSprite) >= len(self.idle):
            self.currentSprite = 0
        if self.run_state == True and int(self.currentSprite) >= len(self.run):
            self.currentSprite = 0

        if self.idle_state == True:
            self.image = self.idle[int(self.currentSprite)]
        if self.run_state == True:
            self.image = self.run[int(self.currentSprite)]
