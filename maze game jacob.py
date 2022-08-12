import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((550, 600))
pygame.display.set_caption("maze game")
myfont = pygame.font.Font (None, 60)
clock = pygame.time.Clock()
clock.tick(60)
label = myfont. render("mazegame", 1, (255, 255, 255, 255))
x = 30
y = 60
color = (255, 255, 255)
rectangle1 = pygame.Rect(30, 30, 5, 5)
rectangle2 = pygame.Rect(96, 96, 5, 5)
draw = True
player = pygame.Rect(12, 12, 60, 60)
win = pygame.Rect(30, 555, 20, 20)
x=30
y=60  
def interact(r1, r2):
    c1 = (r1.x < (r2.x + r2.width))
    c2 = ((r1.x + r1. width) > r2.x)
    c3 = (r1.y < (r2.y + r2.height))
    c4 = ((r1.height + r1.y) > r2.y)
    if c1 and c2 and c3 and c4:
        return True
    else:
        return False

while True:
    screen.blit(label, (50, 10)) 
    if not interact (player, win):
        player = pygame.Rect(x, y, 30, 30)
        pygame.draw.rect(screen, (255,0,0), win)
        pygame.draw.rect(screen, color , player)

        wall_1 =pygame.Rect (10, 50, 590, 5)
        wall_2 =pygame.Rect (10, 95, 190, 5)
        wall_3 =pygame.Rect (245, 95, 250, 5)
        wall_4 =pygame.Rect (540, 50, 5, 550)
        wall_5 =pygame.Rect (200, 95, 5, 150)
        wall_6 =pygame.Rect (240, 95, 5, 190)
        wall_7 =pygame.Rect (100, 240, 100, 5)
        wall_8 =pygame.Rect (100, 100, 100, 60)
        wall_9 =pygame.Rect (60, 195, 100, 5)
        wall_10 =pygame.Rect (60, 280, 180, 5)
        wall_11 =pygame.Rect (10, 330, 280, 5)
        wall_12 =pygame.Rect (10, 100, 5, 450)
        wall_13 =pygame.Rect (60, 135, 5, 150)
        wall_14 =pygame.Rect (290, 135, 5, 200)
        wall_15 =pygame.Rect (295, 135, 160, 5)
        wall_16 =pygame.Rect (490, 100, 5, 450)
        wall_17 =pygame.Rect (10, 590, 590, 5)
        wall_18 =pygame.Rect (60, 540, 430, 5)
        wall_19 =pygame.Rect (60, 380, 5, 210)
        wall_20 =pygame.Rect (100, 500, 350, 5)
        wall_21 =pygame.Rect (450, 140, 5, 360)
        wall_22 =pygame.Rect (60, 460, 350, 5)
        wall_23 =pygame.Rect (100, 420, 350, 5)
        wall_24 =pygame.Rect (60, 380, 360, 5)
        wall_25 =pygame.Rect (330, 220, 5, 160)
        wall_26 =pygame.Rect (370, 140, 5, 200)
        wall_27 =pygame.Rect (410, 220, 5, 160)
        wall_28 =pygame.Rect (10, 55, 5, 40)
        wall_29 =pygame.Rect (10, 550, 5, 40)
        wall_30 =pygame.Rect (15, 540, 50, 5)        
        pygame.draw.rect(screen, (0,255,255), wall_1)
        pygame.draw.rect(screen, (0,0,255), wall_2)
        pygame.draw.rect(screen, (0,0,255), wall_3)
        pygame.draw.rect(screen, (0,0,255), wall_4)
        pygame.draw.rect(screen, (0,0,255), wall_5)
        pygame.draw.rect(screen, (0,0,255), wall_6)
        pygame.draw.rect(screen, (0,0,255), wall_7)
        pygame.draw.rect(screen, (0,0,255), wall_8)
        pygame.draw.rect(screen, (0,0,255), wall_9)
        pygame.draw.rect(screen, (0,0,255), wall_10)
        pygame.draw.rect(screen, (0,0,255), wall_11)
        pygame.draw.rect(screen, (0,0,255), wall_12)
        pygame.draw.rect(screen, (0,0,255), wall_13)
        pygame.draw.rect(screen, (0,0,255), wall_14)
        pygame.draw.rect(screen, (0,0,255), wall_15)
        pygame.draw.rect(screen, (0,0,255), wall_16)
        pygame.draw.rect(screen, (0,0,255), wall_17)
        pygame.draw.rect(screen, (0,0,255), wall_18)
        pygame.draw.rect(screen, (0,0,255), wall_19)
        pygame.draw.rect(screen, (0,0,255), wall_20)
        pygame.draw.rect(screen, (0,0,255), wall_21)
        pygame.draw.rect(screen, (0,0,255), wall_22)
        pygame.draw.rect(screen, (0,0,255), wall_23)
        pygame.draw.rect(screen, (0,0,255), wall_24)
        pygame.draw.rect(screen, (0,0,255), wall_25)
        pygame.draw.rect(screen, (0,0,255), wall_26)
        pygame.draw.rect(screen, (0,0,255), wall_27)
        pygame.draw.rect(screen, (0,0,255), wall_28)
        pygame.draw.rect(screen, (0,0,255), wall_29)
        pygame.draw.rect(screen, (0,0,255), wall_30)

        

        if interact(player, wall_1) or interact(player, wall_2) or interact(player, wall_3) or interact(player, wall_4):
          x=30
          y=60
        if interact(player, wall_5) or interact(player, wall_6) or interact(player, wall_7) or interact(player, wall_8):
          x=30
          y=60
        if interact(player, wall_9) or interact(player, wall_10) or interact(player, wall_11) or interact(player, wall_12):
          x=30
          y=60
        if interact(player, wall_13) or interact(player, wall_14) or interact(player, wall_15) or interact(player, wall_16):
          x=30
          y=60
        if interact(player, wall_17) or interact(player, wall_18) or interact(player, wall_19) or interact(player, wall_20):
          x=30
          y=60
        if interact(player, wall_21) or interact(player, wall_22) or interact(player, wall_23) or interact(player, wall_24):
          x=30
          y=60
        if interact(player, wall_25) or interact(player, wall_26) or interact(player, wall_27) or interact(player, wall_30):
          x=30
          y=60
    rectangle1 = pygame.Rect(x, y, 30, 30)

    pygame.draw.rect(screen, (255, 255, 255), rectangle1)
    



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
            
            
