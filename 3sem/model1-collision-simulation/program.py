import sys
import pygame

WIDTH = 1280
HEIGHT = 640
FPS = 400
BROWN = (192, 124, 84)
LEFT_WALL_RECT = (100, 200, 50, 250)
BOTTOM_WALL_RECT = (150, 400, 1150, 50)
LEFT_BORDER_PADDING = 150
SMALLER_FIGURE_PADDING = 16
BIGGER_FIGURE_PADDING = 42

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("Elastic central collision")
icon = pygame.Surface((50, 50))
icon.fill('black')
pygame.display.set_icon(icon)

font = pygame.font.SysFont('', 50)
figure_font = pygame.font.SysFont('', 20)

bottom_wall = pygame.Rect(BOTTOM_WALL_RECT)
left_wall = pygame.Rect(LEFT_WALL_RECT)


def exchange_velocity(v1, m1, v2, m2):
    return ((m1 - m2) * v1 + (2 * m2) * v2) / (m1 + m2)


def main_loop(_m1, _m2):
    m1 = int(_m1)
    m2 = int(_m2)
    v10 = 1

    if m1 > m2:
        side1, side2 = 100, 50
        m1_padding = BIGGER_FIGURE_PADDING
        m2_padding = SMALLER_FIGURE_PADDING
    elif m1 < m2:
        side1, side2 = 50, 100
        m1_padding = SMALLER_FIGURE_PADDING
        m2_padding = BIGGER_FIGURE_PADDING
    else:
        side1, side2 = 100, 100
        m1_padding = BIGGER_FIGURE_PADDING
        m2_padding = BIGGER_FIGURE_PADDING

    x1, y1 = 900, 400 - side1
    x2, y2 = 600, 400 - side2
    v1, v2 = v10, 0

    number_of_collisions = 0
    parity = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
    
        x1 -= v1
        if x2 + side2 > x1:
            v1, v2 = exchange_velocity(v1, m1, v2, m2), exchange_velocity(v2, m2, v1, m1)
            number_of_collisions += 1
    
        x2 -= v2
        if x2 <= LEFT_BORDER_PADDING:
            v2 *= -1
            number_of_collisions += 1
    
        t1 = x1 if x1 >= side2 + LEFT_BORDER_PADDING else side2 + LEFT_BORDER_PADDING
        t2 = x2 if x1 >= side2 + LEFT_BORDER_PADDING else LEFT_BORDER_PADDING + parity % 2
        parity += 1
    
        screen.fill('white')
        pygame.draw.rect(screen, 'red', (t1, y1, side1, side1))
        screen.blit(figure_font.render('m1', True, 'black'), (t1 + m1_padding, y1 + m1_padding))
        pygame.draw.rect(screen, 'green', (t2, y2, side2, side2))
        screen.blit(figure_font.render('m2', True, 'black'), (t2 + m2_padding, y2 + m2_padding))
        pygame.draw.rect(screen, BROWN, bottom_wall)
        pygame.draw.rect(screen, BROWN, left_wall)
        screen.blit(font.render('collisions: ' + str(number_of_collisions), True, 'black'), (10, 10))
    
        pygame.display.update()
        clock.tick(FPS)

