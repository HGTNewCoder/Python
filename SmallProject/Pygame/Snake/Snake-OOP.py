import pygame
import random



pygame.init()
pygame.display.set_caption("Snake Game")
GRAY = (150,150,150)
WHITE = (255,255,255)
RED = (235, 52, 52)
BLACK = (0,0,0)

SCREEN_WIDTH = 800
SCREEN_LENGTH = 600

Start = True
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_LENGTH))
background = pygame.image.load('source/background.jpg').convert()
class Apple():
    def __init__(self):
        self.image = pygame.image.load('source/apple.jpg').convert()
        self.apple_x = random.randrange(40, 760, 40)
        self.apple_y = random.randrange(40, 560, 40)
    def GenerateXY(self):
        pass
class Snake():
    def __init__(self):
        self.image = pygame.image.load('source/block.jpg').convert()
        self.head_x = 40
        self.head_y = 40
        self.body = []
    def PosXY(self):
        return (self.head_x, self.head_y)
    def Draw(self):
        screen.blit(snake.image, (snake.head_x, snake.head_y))
class Wall():
    def __init__(self):
        self.image = pygame.image.load('source/block.jpg').convert()
        self.num_x = int(SCREEN_WIDTH / self.image.get_width())
        self.num_y = int(SCREEN_LENGTH / self.image.get_height())
    def Draw(self):
        for i in range (0, wall.num_x):
            k = i*40
            screen.blit(wall.image, (k,0))

        for i in range (0, wall.num_y):
            k = i*40
            screen.blit(wall.image, (0, k))

        for i in range (0, wall.num_x):
            k = i*40
            screen.blit(wall.image, (k, SCREEN_LENGTH - 40))

        for i in range (0, wall.num_y):
            k = i*40
            screen.blit(wall.image, (SCREEN_WIDTH - 40, k))
    # def Draw_2():
    #     wall_x = []
    #     wall_y = []
    #     wall_xy = []
    #     for i in range (1, 761):
    #         if i % 40 == 0:
    #             wall_x.append(i)
    #     for i in range (1, 561):
    #         if i % 40 == 0:
    #             wall_y.append(i)
    #     for x in wall_x:
    #         for y in wall_y:
    #             wall_xy.append([x, y])
    #     for i in range(0, len(wall_xy)):
    #         screen.blit(wall.image, (wall_xy[i]))

snake = Snake()
wall = Wall()
apple = Apple()
def GameOverFont():
    gFont = pygame.font.SysFont('consolas', 40)
    gSurf = gFont.render("Game Over!",True,RED)
    gRect = gSurf.get_rect()
    gRect.midtop = (360,100)
    screen.blit(gSurf, gRect)
    pygame.display.flip()
def GameOver():
    for i in range(0, SCREEN_LENGTH):
        if snake.PosXY() == (0, i):
            GameOverFont()
    for i in range(0, SCREEN_WIDTH):
        if snake.PosXY() == (i, 0):
            GameOverFont()
    for i in range(0, SCREEN_LENGTH):
        if snake.PosXY() == (760, i):
            GameOverFont()
    for i in range(0, SCREEN_WIDTH):
        if snake.PosXY() == (i, 560):
            GameOverFont()
def SnakeGrow():
    if snake.head_x == apple.apple_x and snake.head_y == apple.apple_y:
        # snake.body.append(snake.image)
        print("Snake Grow")

while Start:
    screen.fill(WHITE)
    screen.blit(background, (0, 0))
    screen.blit(apple.image, (apple.apple_x, apple.apple_y))

    wall.Draw()
    snake.Draw()
    GameOver()
    SnakeGrow()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Start = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Start = False
            if event.key == pygame.K_UP:
                snake.head_y = snake.head_y - 40
                print("K_UP")
            if event.key == pygame.K_DOWN:
                snake.head_y = snake.head_y + 40
                print("K_Down")
            if event.key == pygame.K_LEFT:
                snake.head_x = snake.head_x - 40
                print("K_LEFT")
            if event.key == pygame.K_RIGHT:
                snake.head_x = snake.head_x + 40
                print("K_RIGHT")
        

    pygame.display.flip()
pygame.quit()