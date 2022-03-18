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


        # Idle sprites
        self.idle = []
        self.idle.append(pygame.image.load(
            os.path.join('raccoon/idle', '0001.png')))
        self.idle.append(pygame.image.load(
            os.path.join('raccoon/idle', '0003.png')))
        self.idle.append(pygame.image.load(
            os.path.join('raccoon/idle', '0005.png')))
        self.idle.append(pygame.image.load(
            os.path.join('raccoon/idle', '0007.png')))
        self.idle.append(pygame.image.load(
            os.path.join('raccoon/idle', '0009.png')))
        self.idle.append(pygame.image.load(
            os.path.join('raccoon/idle', '0011.png')))
        self.idle.append(pygame.image.load(
            os.path.join('raccoon/idle', '0013.png')))
        self.idle.append(pygame.image.load(
            os.path.join('raccoon/idle', '0015.png')))
        self.idle.append(pygame.image.load(
            os.path.join('raccoon/idle', '0017.png')))
        self.idle.append(pygame.image.load(
            os.path.join('raccoon/idle', '0019.png')))
        self.idle.append(pygame.image.load(
            os.path.join('raccoon/idle', '0021.png')))
        
        # Run sprites
        self.run = []
        self.run.append(pygame.image.load(
            os.path.join('raccoon/run', 'run0001.png')))
        self.run.append(pygame.image.load(
            os.path.join('raccoon/run', 'run0003.png')))
        self.run.append(pygame.image.load(
            os.path.join('raccoon/run', 'run0005.png')))
        self.run.append(pygame.image.load(
            os.path.join('raccoon/run', 'run0007.png')))
        self.run.append(pygame.image.load(
            os.path.join('raccoon/run', 'run0009.png')))
        self.run.append(pygame.image.load(
            os.path.join('raccoon/run', 'run0011.png')))
        self.run.append(pygame.image.load(
            os.path.join('raccoon/run', 'run0013.png')))
        self.run.append(pygame.image.load(
            os.path.join('raccoon/run', 'run0015.png')))
        self.run.append(pygame.image.load(
            os.path.join('raccoon/run', 'run0017.png')))
        self.run.append(pygame.image.load(
            os.path.join('raccoon/run', 'run0019.png')))
        self.run.append(pygame.image.load(
            os.path.join('raccoon/run', 'run0021.png')))
        self.run.append(pygame.image.load(
            os.path.join('raccoon/run', 'run0023.png')))

        if (self.idle_state == True):
            self.currentSprite = 0
            self.image = self.idle[self.currentSprite]
            self.rect = self.image.get_rect()
            self.rect.bottomleft = (x_pos, y_pos)
        elif (self.run_state == True):
            self.currentSprite = 0
            self.image = self.run[self.currentSprite]
            self.rect = self.image.get_rect()
            self.rect.bottomleft = (x_pos, y_pos)
        
    def update(self):
        self.rect.x += self.movement
        if self.rect.left > 900:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = 900

        self.currentSprite += 0.25

        if self.idle_state == True and int(self.currentSprite) >= len(self.idle):
            self.currentSprite = 0
        if self.run_state == True and int(self.currentSprite) >= len(self.run):
            self.currentSprite = 0

        if self.idle_state == True:
            self.image = self.idle[int(self.currentSprite)]
        if self.run_state == True:
            self.image = self.run[int(self.currentSprite)]
