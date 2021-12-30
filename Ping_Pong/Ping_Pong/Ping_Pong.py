import pygame
import sys
import random

pygame.init()
clock = pygame.time.Clock()

WIDTH = 1280
HEIGHT = 760
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ping Pong')

# SHAPES
BALL = pygame.Rect(WIDTH/2 - 15, HEIGHT/2 - 15, 30, 30)
BALL_SPEED_X, BALL_SPEED_Y = 7 * random.choice((1, -1)), 7 * random.choice((1, -1))
PLAYER = pygame.Rect(WIDTH - 20, HEIGHT/2 - 70, 10, 140)
OPPONENT = pygame.Rect(10, HEIGHT/2 - 70, 10, 140)
PLAYER_SPEED = 8
score_time = True

# COLORS
DARK_GREEN = (0, 51, 0)
LIGHT_GREEN = (178, 255, 102)
PURPLE = (77, 0, 77)
DARK_GRAY = (167, 167, 167)
WHITE = (255, 255, 255)
ORANGE = (255, 153, 0)

# TEXT VARIABLES
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)

# PROZOR
def window():
    SCREEN.fill(DARK_GREEN)
    pygame.draw.ellipse(SCREEN, WHITE, BALL)
    pygame.draw.rect(SCREEN, ORANGE, PLAYER)
    pygame.draw.rect(SCREEN, PURPLE, OPPONENT)
    pygame.draw.aaline(SCREEN, WHITE, (WIDTH/2, 0), (WIDTH/2, HEIGHT))
    player_score_txt = game_font.render(f"{player_score}", 1, WHITE)
    SCREEN.blit(player_score_txt, (WIDTH/2 + 20, HEIGHT/2 - 10))
    opponent_score_txt = game_font.render(f"{opponent_score}", 1, WHITE)
    SCREEN.blit(opponent_score_txt, (WIDTH/2 - 35, HEIGHT/2 - 10))
    if score_time:
        ball_start(BALL)
    pygame.display.update()


# LOPTA
def ball_movement(ball):
    global BALL_SPEED_X, BALL_SPEED_Y, player_score, opponent_score, score_time

    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        BALL_SPEED_Y *= -1

    if ball.left <= 10:
        #ball_restart(ball)
        player_score += 1
        score_time = pygame.time.get_ticks()

    if ball.right >= WIDTH - 10:
        #ball_restart(ball)
        opponent_score += 1
        score_time = pygame.time.get_ticks()

    if ball.colliderect(PLAYER) or ball.colliderect(OPPONENT):
        BALL_SPEED_X *= -1


def ball_start(ball):
    global BALL_SPEED_X, BALL_SPEED_Y, score_time
    current_time = pygame.time.get_ticks()

    ball.center = (WIDTH/2, HEIGHT/2)

    if current_time - score_time < 700:
        num3 = game_font.render("3", False, WHITE)
        SCREEN.blit(num3, (WIDTH/2 - 10, HEIGHT/2 + 20))

    if 700 < current_time - score_time < 1400:
        num2 = game_font.render("2", 1, WHITE)
        SCREEN.blit(num2, (WIDTH/2 - 10, HEIGHT/2 + 20))

    if 1400 < current_time - score_time < 2100:
        num1 = game_font.render("1", 1, WHITE)
        SCREEN.blit(num1, (WIDTH/2 - 10, HEIGHT/2 + 20))

    if current_time - score_time < 2100:
        BALL_SPEED_X, BALL_SPEED_Y = 0,0
    else:
        BALL_SPEED_X = 7 * random.choice((1, -1))
        BALL_SPEED_Y = 7 * random.choice((1, -1))
        score_time = None


# IGRAC i OPPONENT
def player_movement(player, pressed_key):
    if pressed_key[pygame.K_DOWN] and player.bottom <= HEIGHT:
        player.y += PLAYER_SPEED
    if pressed_key[pygame.K_UP] and player.top >= 0:
        player.y -= PLAYER_SPEED

def opponent_movement(opponent, pressed_key):
    if pressed_key[pygame.K_s] and opponent.bottom <= HEIGHT:
        opponent.y += PLAYER_SPEED
    if pressed_key[pygame.K_w] and opponent.top >= 0:
        opponent.y -= PLAYER_SPEED

def main():
    global PLAYER_SPEED
    run = True;
    while run == True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pressed_key = pygame.key.get_pressed()

        window()
        ball_movement(BALL)
        player_movement(PLAYER, pressed_key)
        opponent_movement(OPPONENT, pressed_key)



    pygame.quit()

if __name__ == "__main__":
    main()