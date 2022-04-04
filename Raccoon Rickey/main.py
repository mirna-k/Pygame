import pygame, sys, pymunk
from classes.ClassFile import *

pygame.init()
pygame.display.set_caption('Raccoon Rickey')

#GLOBALS
WIDTH, HEIGHT = 900, 750
FPS = 60
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

#COLORS
SKY = (135, 206, 235)
YELLOW = (255, 255, 0)
GRASS = (60,179,113)

#PLAYER
raccoon = Player(10, HEIGHT-38)
player_group = pygame.sprite.GroupSingle()
player_group.add(raccoon)

#INSTANCES
BLOCK = Platform(WIDTH, 40, 0, HEIGHT - 40, GRASS)
block_group = pygame.sprite.Group()
block_group.add(BLOCK)
   
def window():
    SCREEN.fill(SKY)
    block_group.draw(SCREEN)
    player_group.draw(SCREEN)
    pygame.display.update()

def main():
    global state
    clock = pygame.time.Clock()
    run = True
    while run == True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        window()
        player_group.update()

    pygame.quit()

if __name__ == "__main__":
    main()