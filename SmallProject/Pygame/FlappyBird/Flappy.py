import pygame
SCREENWIDTH = 600
SCREENLENGTH = 500
GRAY = (150,150,150)
WHITE = (255,255,255)
RED = (235, 52, 52)
BLACK = (0,0,0)
running = True

pygame.init()
pygame.display.set_caption("Flappy Bird2")
screen = pygame.display.set_mode((SCREENLENGTH, SCREENWIDTH))

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()