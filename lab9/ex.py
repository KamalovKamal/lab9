import pygame
from datetime import datetime
import math
pygame.init()

WIDTH, HEIGHT = 1200, 800
H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2
RADIUS = H_HEIGHT - 50
radius_list = {'sec': RADIUS - 10, 'min': RADIUS - 55, 'hour': RADIUS - 100}
RADIUS_ARK = RADIUS + 8
pygame.init()
surface = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_icon(pygame.image.load("mickeyclock.jpeg"))



clock60 = dict(zip(range(60), range(0, 360, 6)))

font = pygame.font.SysFont('Verdana', 60)

def get_clock_pos(clock_dict, clock_hand, key):
    x = H_WIDTH + radius_list[key] * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = H_HEIGHT + radius_list[key] * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    return x, y

mickey_image = pygame.image.load('main-clock.png')
right_hand_image = pygame.image.load('right-hand.png')
left_hand_image = pygame.image.load('left-hand.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    surface.fill(pygame.Color('white'))

    t = datetime.now()
    hour, minute, second = ((t.hour % 12) * 5 + t.minute // 12) % 60, t.minute, t.second

    pygame.draw.circle(surface, pygame.Color('grey'), (H_WIDTH, H_HEIGHT), RADIUS)
    pygame.draw.line(surface, pygame.Color('blue'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, hour, 'hour'), 30)
    pygame.draw.line(surface, pygame.Color('green'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, minute, 'min'), 15)
    pygame.draw.line(surface, pygame.Color('red'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, second, 'sec'), 5)
    pygame.draw.circle(surface, pygame.Color('white'), (H_WIDTH, H_HEIGHT), 8)

    minutes_angle = math.radians(minute * 6 - 90)
    seconds_angle = math.radians(second * 6 - 90)

    rotated_right_hand = pygame.transform.rotate(right_hand_image, math.degrees(-minutes_angle))
    rotated_left_hand = pygame.transform.rotate(left_hand_image, math.degrees(-seconds_angle))

    right_hand_pos = (H_WIDTH - rotated_right_hand.get_width() // 2, H_HEIGHT - rotated_right_hand.get_height() // 2)
    left_hand_pos = (H_WIDTH - rotated_left_hand.get_width() // 2, H_HEIGHT - rotated_left_hand.get_height() // 2)

    surface.blit(mickey_image, (H_WIDTH - mickey_image.get_width() // 2, H_HEIGHT - mickey_image.get_height() // 2))
    surface.blit(rotated_right_hand, right_hand_pos)
    surface.blit(rotated_left_hand, left_hand_pos)

    time_render = font.render(f'{t:%H:%M:%S}', True, pygame.Color('yellow'), pygame.Color('black'))
    surface.blit(time_render, (0, 0))

    sec_angle = -math.radians(clock60[second]) + math.pi / 2
    pygame.draw.arc(surface, pygame.Color('red'),
                    (H_WIDTH - RADIUS_ARK, H_HEIGHT - RADIUS_ARK, 2 * RADIUS_ARK, 2 * RADIUS_ARK),
                    math.pi / 2, sec_angle, 50)

    pygame.display.flip()
    clock.tick(20)
