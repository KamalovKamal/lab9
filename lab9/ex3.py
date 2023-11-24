import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 25
BALL_DIAMETER = BALL_RADIUS * 2
BALL_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 100, 0)  
MOVE_AMOUNT = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

ball_x = WIDTH // 2
ball_y = HEIGHT // 2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and ball_y - MOVE_AMOUNT >= 0:
        ball_y -= MOVE_AMOUNT
    if keys[pygame.K_DOWN] and ball_y + BALL_DIAMETER + MOVE_AMOUNT <= HEIGHT:
        ball_y += MOVE_AMOUNT
    if keys[pygame.K_LEFT] and ball_x - MOVE_AMOUNT >= 0:
        ball_x -= MOVE_AMOUNT
    if keys[pygame.K_RIGHT] and ball_x + BALL_DIAMETER + MOVE_AMOUNT <= WIDTH:
        ball_x += MOVE_AMOUNT

    screen.fill(BACKGROUND_COLOR)

    pygame.draw.circle(screen, BALL_COLOR, (ball_x + BALL_RADIUS, ball_y + BALL_RADIUS), BALL_RADIUS)

    pygame.display.flip()

    clock.tick(60)
