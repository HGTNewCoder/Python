import pygame
import random

GRAY = (150,150,150)
WHITE = (255,255,255)
RED = (235, 52, 52)
BLACK = (0,0,0)
SCREEN_WIDTH = 800
SCREEN_LENGTH = 600

pygame.init()
Start = True
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_LENGTH))

background = pygame.image.load('source/background.jpg').convert()
wall = pygame.image.load('source/block.jpg').convert()
wall_num_x = int(SCREEN_WIDTH / wall.get_width())
wall_num_y = int(SCREEN_LENGTH / wall.get_height())

snake = pygame.image.load('source/block.jpg').convert()
snake_x = 40
snake_y = 40

apple = pygame.image.load('source/apple.jpg').convert()
apple_x = random.randrange(40, 760, 40)
apple_y = random.randrange(40, 560, 40)

def GameOver():
    gFont = pygame.font.SysFont('consolas', 40)
    gSurf = gFont.render("Game Over!",True,RED)
    gRect = gSurf.get_rect()
    gRect.midtop = (360,100)
    screen.blit(gSurf, gRect)
    pygame.display.flip()

while Start:
    screen.fill(WHITE)
    screen.blit(background, (0, 0))
    screen.blit(apple, (apple_x, apple_y))


    for i in range (0, wall_num_x):
        k = i*40
        screen.blit(wall, (k,0))
    for i in range (0, wall_num_y):
        k = i*40
        screen.blit(wall, (0, k))
    for i in range (0, wall_num_x):
        k = i*40
        screen.blit(wall, (k, 560))
    for i in range (0, wall_num_y):
        k = i*40
        screen.blit(wall, (760, k))
    if snake_x == apple_x and snake_y == apple_y:
        GameOver()
    
    screen.blit(snake, (snake_x, snake_y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Start = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Start = False
            if event.key == pygame.K_UP:
                snake_y = snake_y - 40
                print("K_UP")
            if event.key == pygame.K_DOWN:
                snake_y = snake_y + 40
                print("K_Down")
            if event.key == pygame.K_LEFT:
                snake_x = snake_x - 40
                print("K_LEFT")
            if event.key == pygame.K_RIGHT:
                snake_x = snake_x + 40
                print("K_RIGHT")
        

    pygame.display.flip()
pygame.quit()