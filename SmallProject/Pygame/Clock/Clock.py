from ast import While
import pygame
import time

pygame.init()

screen = pygame.display.set_mode((500,600))

# RGB CODE
GRAY = (150,150,150)
WHITE = (255,255,255)
RED = (235, 52, 52)
total_sec = 0


running = True

while running:
    screen.fill(GRAY)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    # print(mouse_x, mouse_y)
    pygame.draw.rect(screen, WHITE, (100, 100, 50, 50)) # - Minutes
    pygame.draw.rect(screen, WHITE, (200, 100, 50, 50)) # + Minutes
    pygame.draw.rect(screen, WHITE, (100, 200, 50, 50)) # - Seconds
    pygame.draw.rect(screen, WHITE, (200, 200, 50, 50)) # + Seconds
    pygame.draw.rect(screen, WHITE, (300, 100, 100, 50)) # Start
    pygame.draw.rect(screen, WHITE, (300, 200, 100, 50)) # Reset
    pygame.draw.line(screen, RED, (105, 125), (145, 125)) # Minus Symbol
    pygame.draw.line(screen, RED, (205, 125), (245, 125)) # Sum Symbol 1
    pygame.draw.line(screen, RED, (225, 105), (225, 145)) # Sym Symbol 2

    pygame.draw.line(screen, RED, (105, 225), (145, 225)) # Minus Symbol
    pygame.draw.line(screen, RED, (205, 225), (245, 225)) # Sum Symbol 1
    pygame.draw.line(screen, RED, (225, 205), (225, 245)) # Sym Symbol 2

    
    for event in pygame.event.get(): # Event
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouse_x < 150 and mouse_x > 100 and mouse_y < 150 and mouse_y> 100:
                    print("- Minutes")
                    total_sec = total_sec - 60
                    print(total_sec)
                if mouse_x < 250 and mouse_x > 200 and mouse_y < 150 and mouse_y> 100:
                    print("+ Minutes")
                    total_sec = total_sec + 60
                    print(total_sec)
                if mouse_x < 150 and mouse_x > 100 and mouse_y < 250 and mouse_y> 200:
                    print("- Seconds")
                    total_sec = total_sec - 1
                    print(total_sec)
                if mouse_x < 250 and mouse_x > 200 and mouse_y < 250 and mouse_y> 200:
                    print("+ Seconds")
                    total_sec = total_sec + 1
                    print(total_sec)
                if mouse_x < 350 and mouse_x > 300 and mouse_y < 150 and mouse_y> 100:
                    print("Start")
                if mouse_x < 350 and mouse_x > 300 and mouse_y < 250 and mouse_y> 200:
                    print("Reset")
        

    pygame.display.flip()
pygame.quit()