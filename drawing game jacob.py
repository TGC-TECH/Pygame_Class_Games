import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("hello world")
myfont = pygame.font.Font (None, 60)
clock = pygame.time.Clock()
clock.tick(60)
color = (255,187, 0,)
Rcolor =(187, 237, 187)
x = 60
y = 30
rectangle1 = pygame.Rect(x, y, 5, 5)
rectangle2 = pygame.Rect(96, 96, 5, 5)
draw = True


while True:
    rectangle1 = pygame.Rect(x, y, 5, 5)


    pygame.draw.rect(screen, Rcolor ,rectangle1)
 




    pygame.display.update()
    if draw: screen.fill((0,0,0))

    




    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            y=y-10
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            y=y+10
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            x=x-10
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            x=x+10
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            draw = not draw
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            Rcolor = (255, 10, 0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            Rcolor = (255, 177, 0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
            Rcolor = (255, 255, 0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
            Rcolor = (100, 255, 0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_5:
            Rcolor = (0, 0, 255)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_6:
            Rcolor = (177, 156, 217)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_7:
            Rcolor = (255, 255, 255)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_8:
            Rcolor = (150, 75, 0)    
        if event.type == pygame.KEYDOWN and event.key == pygame.K_9:
            Rcolor = (0, 0, 0)
            
            
            
            
