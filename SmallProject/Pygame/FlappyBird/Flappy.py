import pygame

pygame.init()
pygame.display.set_caption("Flappy Bird")

#Biến phụ
clock = pygame.time.Clock()
gravity = 0.25
bird_movement = 0

#Biến của game
SCREENLENGTH = 432
SCREENWIDTH = 768
screen = pygame.display.set_mode((SCREENLENGTH, SCREENWIDTH))
GRAY = (150,150,150)
WHITE = (255,255,255)
RED = (235, 52, 52)
BLACK = (0,0,0)
running = True


#Tạo nền
bg = pygame.image.load('assets/background-night.png').convert()
bg = pygame.transform.scale(bg, (SCREENLENGTH, SCREENWIDTH))

#Tạo Sàn
fl = pygame.image.load('assets/floor.png').convert()
fl = pygame.transform.scale2x(fl)
fl_x = 0

#Tạo Chim
bird = pygame.image.load('assets/yellowbird-midflap.png').convert()
bird_rect = bird.get_rect(center = (100, SCREENWIDTH / 2))

#Tạo ống
pipe_surface = pygame.image.load('assets/pipe-green.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 1200)
pipe_list = []

#Các hàm của trò chơi
def draw_floor():
    screen.blit(fl,(fl_x, SCREENWIDTH - 60))
    screen.blit(fl,(fl_x + SCREENLENGTH, SCREENWIDTH - 60))
def create_pipe():
    new_pipe = pipe_surface.get_rect(midtop = (SCREENLENGTH / 2, SCREENWIDTH / 2))
    return new_pipe
def move_pipe(pipe):
    for pipe in pipe:
        pipe.centerx -= 5
    return pipe

#Game LOOP
while running:
    screen.fill(WHITE)
    screen.blit(bg,(0,0))
    fl_x -= 1
    draw_floor()

    screen.blit(bird, bird_rect)
    bird_movement += gravity
    bird_rect.centery += bird_movement

    if fl_x <= -SCREENLENGTH:
        fl_x = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement = -10
        if event.type == spawnpipe:
            pipe_list.append(create_pipe())
            
    pygame.display.update()
    clock.tick(120)
pygame.quit()