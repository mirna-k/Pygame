import pygame
import os

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
MAX_BULLETS = 5
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python game")
FONT = pygame.font.SysFont('comicsans', 40)
FONT2 = pygame.font.SysFont('comicsans', 100)

WHITE = (225, 225, 225)
BLACK = (0,0,0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PINK = (255, 20, 147)

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 42
BORDER = pygame.Rect(WIDTH//2 - 3, 0, 6, HEIGHT)

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

#YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP_IMAGE = pygame.image.load(\'spaceship_yellow.png')
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

BULLETHIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))

def window(yellow, red, yellow_bullets, red_bullets, red_health, yellow_health):
    WIN.blit(BACKGROUND, (0,0))
    pygame.draw.rect(WIN, BLACK, BORDER)

    red_health_txt = FONT.render("Health: " + str(red_health), 1, WHITE)
    yellow_health_txt = FONT.render("Helath: " + str(yellow_health), 1, WHITE)
    WIN.blit(red_health_txt, (WIDTH - red_health_txt.get_width() - 10, 10))
    WIN.blit(yellow_health_txt, (10, 10))

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    pygame.display.update()

def yellow_spaceship_movement(pressed_key, yellow):
    if pressed_key[pygame.K_a] and yellow.x - 5 > 0: #lijevo
        yellow.x -= 5
    if pressed_key[pygame.K_d] and yellow.x + 5 + yellow.width  - 15 < BORDER.x: #desno
        yellow.x += 5
    if pressed_key[pygame.K_w] and yellow.y - 5 > 0: #gore
        yellow.y -= 5
    if pressed_key[pygame.K_s] and yellow.y + 5 + yellow.height + 10 < HEIGHT: #dolje
        yellow.y += 5

def red_spaceship_movement(pressed_key, red):
    if pressed_key[pygame.K_LEFT] and red.x - 5 > BORDER.x: #lijevo <-
        red.x -= 5
    if pressed_key[pygame.K_RIGHT] and red.x + 5 + red.width - 15 < WIDTH: #desno ->
        red.x += 5
    if pressed_key[pygame.K_UP] and red.y - 5 > 0: #gore
        red.y -= 5
    if pressed_key[pygame.K_DOWN] and red.y + 5 + red.height + 10 < HEIGHT: #dolje
        red.y += 5

def handle_bullets(yellow, red, yellow_bullets, red_bullets):
    for bullet in yellow_bullets:
        bullet.x += 7
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= 7
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

def winning(text):
    draw_text = FONT2.render(text, 1, PINK)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow_bullets = []
    red_bullets = []
    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock()
    run = True;
    while run == True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2, 10, 5)
                    yellow_bullets.append(bullet)
                    FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2, 10, 5)
                    red_bullets.append(bullet)
                    FIRE_SOUND.play()

            if event.type == RED_HIT:
                red_health -= 1
                BULLETHIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLETHIT_SOUND.play()

        end_txt = ""
        if red_health < 0:
            end_txt = "YELLOW WINS!"
        
        if yellow_health < 0:
            end_txt = "RED WINS!"

        if end_txt != "":
            winning(end_txt)
            break

        print(red_bullets, yellow_bullets)
        pressed_key = pygame.key.get_pressed()

        window(yellow, red, yellow_bullets, red_bullets, red_health, yellow_health)
        yellow_spaceship_movement(pressed_key, yellow)
        red_spaceship_movement(pressed_key, red)
        handle_bullets(yellow, red, yellow_bullets, red_bullets)
            
    pygame.quit()

if __name__ == "__main__":
    main()