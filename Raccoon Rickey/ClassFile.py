from email.mime import image
import pygame
from classes.Support import import_images_from_folder

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
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.import_character_assets()
        self.currentSprite = 0
        self.animation_speed = 0.25
        self.image = self.sprite_dict['idle'][self.currentSprite]
        self.pos = (x_pos, y_pos)
        self.rect = self.image.get_rect(bottomleft = self.pos)

        #player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 3
        self.gravity = 0.8
        self.jump_speed = -16

        #player status
        self.state = 'idle'
        self.go_left = False

    def import_character_assets(self):
        path = 'raccoon/'
        self.sprite_dict = {'idle':[], 'walk':[], 'run':[],'jump':[]}
        
        for animation in self.sprite_dict.keys():
            full_path = path + animation
            self.sprite_dict[animation] = import_images_from_folder(full_path)


    def animate(self):
        animation = self.sprite_dict[self.state]
        self.currentSprite += self.animation_speed

        if self.currentSprite >= len(animation):
            self.currentSprite = 0
            
        self.image = animation[int(self.currentSprite)]

        if self.go_left:
            flipped_image = pygame.transform.flip(self.image,True,False)
            self.image = flipped_image
        #else:
            #self.image = self.image

    def jump(self):
        self.rect.y += self.gravity

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.go_left = False
            self.state = 'walk'
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.go_left = True
            self.state = 'walk'
        else: 
            self.direction.x = 0
            self.state = 'idle'
        
        if keys[pygame.K_UP]:
            self.jump()

    def update(self):
        self.get_input()
        self.animate()
        self.rect.x += self.direction.x * self.speed
        if self.rect.left > 900:
            self.rect.right = 0
        if self.rect.right < 0:
            self.rect.left = 900