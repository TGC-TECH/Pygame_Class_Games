import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((550, 600))
pygame.display.set_caption("maze game")
myfont = pygame.font.Font (None, 60)
clock = pygame.time.Clock()
clock.tick(60)
label = myfont. render("mazegame", 1, (255, 255, 255, 255))
x = 10
y = 10
color = (255, 255, 255)
rectangle1 = pygame.Rect(10, 30, 5, 5)
rectangle2 = pygame.Rect(36, 56, 565, 5)
draw = True 
player = pygame.Rect(0, 0, 30, 30)
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


    #row 1
        
        wall_1 =pygame.Rect (20, 45, 40, 5)
        wall_2 =pygame.Rect (20, 90, 40, 5)
        wall_3 =pygame.Rect (60, 50, 5, 40)
        wall_4 =pygame.Rect (15, 50, 5, 40)
        wall_5 =pygame.Rect (60, 45, 40, 5)
        wall_6 =pygame.Rect (60, 90, 40, 5)
        wall_7 =pygame.Rect (100, 50, 5, 40)
        wall_8 =pygame.Rect (100, 45, 40, 5)
        wall_9 =pygame.Rect (100, 90, 40, 5)
        wall_10 =pygame.Rect (140, 50, 5, 40)
        wall_11 =pygame.Rect (140, 45, 40, 5)
        wall_12 =pygame.Rect (140, 90, 40, 5)
        wall_13 =pygame.Rect (180, 50, 5, 40)
        wall_14 =pygame.Rect (180, 45, 40, 5)
        wall_15 =pygame.Rect (180, 90, 40, 5)
        wall_16 =pygame.Rect (220, 50, 5, 40)
        wall_17 =pygame.Rect (220, 45, 40, 5)
        wall_18 =pygame.Rect (220, 90, 40, 5)
        wall_19 =pygame.Rect (260, 50, 5, 40)
        wall_20 =pygame.Rect (260, 45, 40, 5)
        wall_21 =pygame.Rect (260, 90, 40, 5)
        wall_22 =pygame.Rect (300, 50, 5, 40)
        wall_23 =pygame.Rect (300, 45, 40, 5)
        wall_24 =pygame.Rect (300, 90, 40, 5)
        wall_25 =pygame.Rect (340, 50, 5, 40)
        wall_26 =pygame.Rect (340, 45, 40, 5)
        wall_27 =pygame.Rect (340, 90, 40, 5)
        wall_28 =pygame.Rect (380, 50, 5, 40)
        wall_29 =pygame.Rect (380, 45, 40, 5)
        wall_30 =pygame.Rect (380, 90, 40, 5)
        wall_31 =pygame.Rect (420, 50, 5, 40)
        wall_32 =pygame.Rect (420, 45, 40, 5)
        wall_33 =pygame.Rect (420, 90, 40, 5)
        wall_34 =pygame.Rect (460, 50, 5, 40)
        wall_35 =pygame.Rect (460, 45, 40, 5)
        wall_36 =pygame.Rect (460, 90, 40, 5)
        wall_37 =pygame.Rect (500, 50, 5, 40)
        wall_38 =pygame.Rect (500, 45, 40, 5)
        wall_39 =pygame.Rect (500, 90, 40, 5)
        wall_40 =pygame.Rect (540, 50, 5, 40)
        pygame.draw.rect(screen, (0,255,255), wall_1)     
        pygame.draw.rect(screen, (0,0,255), wall_2)
        pygame.draw.rect(screen, (0,0,255), wall_3)
        pygame.draw.rect(screen, (0,255,255), wall_4)
        pygame.draw.rect(screen, (0,255,255), wall_5)     
        pygame.draw.rect(screen, (0,0,255), wall_6)
        pygame.draw.rect(screen, (0,0,255), wall_7)
        pygame.draw.rect(screen, (0,255,255), wall_8)     
        pygame.draw.rect(screen, (0,0,255), wall_9)
        pygame.draw.rect(screen, (0,0,255), wall_10)
        pygame.draw.rect(screen, (0,255,255), wall_11)     
        pygame.draw.rect(screen, (0,0,255), wall_12)
        pygame.draw.rect(screen, (0,0,255), wall_13)
        pygame.draw.rect(screen, (0,255,255), wall_14)
        pygame.draw.rect(screen, (0,0,255), wall_15)
        pygame.draw.rect(screen, (0,0,255), wall_16)     
        pygame.draw.rect(screen, (0,255,255), wall_17)
        pygame.draw.rect(screen, (0,0,255), wall_18)
        pygame.draw.rect(screen, (0,0,255), wall_19)     
        pygame.draw.rect(screen, (0,255,255), wall_20)
        pygame.draw.rect(screen, (0,0,255), wall_21)
        pygame.draw.rect(screen, (0,0,255), wall_22)     
        pygame.draw.rect(screen, (0,255,255), wall_23)
        pygame.draw.rect(screen, (0,0,255), wall_24)
        pygame.draw.rect(screen, (0,0,255), wall_25)
        pygame.draw.rect(screen, (0,255,255), wall_26)    
        pygame.draw.rect(screen, (0,0,255), wall_27)
        pygame.draw.rect(screen, (0,0,255), wall_28)
        pygame.draw.rect(screen, (0,255,255), wall_29)     
        pygame.draw.rect(screen, (0,0,255), wall_30)
        pygame.draw.rect(screen, (0,0,255), wall_31)
        pygame.draw.rect(screen, (0,255,255), wall_32)
        pygame.draw.rect(screen, (0,0,255), wall_33)
        pygame.draw.rect(screen, (0,0,255), wall_34)     
        pygame.draw.rect(screen, (0,255,255), wall_35)
        pygame.draw.rect(screen, (0,0,255), wall_36)
        pygame.draw.rect(screen, (0,0,255), wall_37)     
        pygame.draw.rect(screen, (0,255,255), wall_38)
        pygame.draw.rect(screen, (0,0,255), wall_39)
        pygame.draw.rect(screen, (0,255,255), wall_40)

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
        if interact(player, wall_25) or interact(player, wall_26) or interact(player, wall_27) or interact(player, wall_28):
          x=30
          y=60
        if interact(player, wall_29) or interact(player, wall_30) or interact(player, wall_31) or interact(player, wall_32):
          x=30
          y=60
        if interact(player, wall_33) or interact(player, wall_34) or interact(player, wall_35) or interact(player, wall_36):
          x=30
          y=60
        if interact(player, wall_37) or interact(player, wall_38) or interact(player, wall_39) or interact(player, wall_40):
          x=30
          y=60


#row 2

        
        wall_1 =pygame.Rect (20, 135, 40, 5)
        wall_2 =pygame.Rect (60, 95, 5, 40)
        wall_3 =pygame.Rect (15, 95, 5, 40)
        wall_4 =pygame.Rect (60, 135, 40, 5)
        wall_5 =pygame.Rect (100, 95, 5, 40)
        wall_6 =pygame.Rect (100, 135, 40, 5)
        wall_7 =pygame.Rect (140, 95, 5, 40)
        wall_8 =pygame.Rect (140, 135, 40, 5)
        wall_9 =pygame.Rect (180, 95, 5, 40)
        wall_10 =pygame.Rect (180, 135, 40, 5)
        wall_11 =pygame.Rect (220, 95, 5, 40)
        wall_12 =pygame.Rect (220, 135, 40, 5)
        wall_13 =pygame.Rect (260, 95, 5, 40)
        wall_14 =pygame.Rect (260, 135, 40, 5)
        wall_15 =pygame.Rect (300, 95, 5, 40)
        wall_16 =pygame.Rect (300, 135, 40, 5)
        wall_17 =pygame.Rect (340, 95, 5, 40)
        wall_18 =pygame.Rect (340, 135, 40, 5)
        wall_19 =pygame.Rect (380, 95, 5, 40)
        wall_20 =pygame.Rect (380, 135, 40, 5)
        wall_21 =pygame.Rect (420, 95, 5, 40)
        wall_22 =pygame.Rect (420, 135, 40, 5)
        wall_23 =pygame.Rect (460, 95, 5, 40)
        wall_24 =pygame.Rect (460, 135, 40, 5)
        wall_25 =pygame.Rect (500, 95, 5, 40)
        wall_26 =pygame.Rect (500, 135, 40, 5)
        wall_27 =pygame.Rect (540, 95, 5, 40)
        pygame.draw.rect(screen, (0,0,255), wall_1)     
        pygame.draw.rect(screen, (0,0,255), wall_2)
        pygame.draw.rect(screen, (0,255,255), wall_3)
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
        pygame.draw.rect(screen, (0,255,255), wall_27)

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
        if interact(player, wall_25) or interact(player, wall_26) or interact(player, wall_27):
          x=30
          y=60
  #row 3

        
        wall_1 =pygame.Rect (20, 180, 40, 5)
        wall_2 =pygame.Rect (60, 140, 5, 40)
        wall_3 =pygame.Rect (15, 140, 5, 40)
        wall_4 =pygame.Rect (60, 180, 40, 5)
        wall_5 =pygame.Rect (100, 140, 5, 40)
        wall_6 =pygame.Rect (100, 180, 40, 5)
        wall_7 =pygame.Rect (140, 140, 5, 40)
        wall_8 =pygame.Rect (140, 180, 40, 5)
        wall_9 =pygame.Rect (180, 140, 5, 40)
        wall_10 =pygame.Rect (180, 180, 40, 5)
        wall_11 =pygame.Rect (220, 140, 5, 40)
        wall_12 =pygame.Rect (220, 180, 40, 5)
        wall_13 =pygame.Rect (260, 140, 5, 40)
        wall_14 =pygame.Rect (260, 180, 40, 5)
        wall_15 =pygame.Rect (300, 140, 5, 40)
        wall_16 =pygame.Rect (300, 180, 40, 5)
        wall_17 =pygame.Rect (340, 140, 5, 40)
        wall_18 =pygame.Rect (340, 180, 40, 5)
        wall_19 =pygame.Rect (380, 140, 5, 40)
        wall_20 =pygame.Rect (380, 180, 40, 5)
        wall_21 =pygame.Rect (420, 140, 5, 40)
        wall_22 =pygame.Rect (420, 180, 40, 5)
        wall_23 =pygame.Rect (460, 140, 5, 40)
        wall_24 =pygame.Rect (460, 180, 40, 5)
        wall_25 =pygame.Rect (500, 140, 5, 40)
        wall_26 =pygame.Rect (500, 180, 40, 5)
        wall_27 =pygame.Rect (540, 140, 5, 40)
        pygame.draw.rect(screen, (0,0,255), wall_1)     
        pygame.draw.rect(screen, (0,0,255), wall_2)
        pygame.draw.rect(screen, (0,255,255), wall_3)
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
        pygame.draw.rect(screen, (0,255,255), wall_27)
  #row 4

        
        wall_1 =pygame.Rect (20, 225, 40, 5)
        wall_2 =pygame.Rect (60, 185, 5, 40)
        wall_3 =pygame.Rect (15, 185, 5, 40)
        wall_4 =pygame.Rect (60, 225, 40, 5)
        wall_5 =pygame.Rect (100, 185, 5, 40)
        wall_6 =pygame.Rect (100, 225, 40, 5)
        wall_7 =pygame.Rect (140, 185, 5, 40)
        wall_8 =pygame.Rect (140, 225, 40, 5)
        wall_9 =pygame.Rect (180, 185, 5, 40)
        wall_10 =pygame.Rect (180, 225, 40, 5)
        wall_11 =pygame.Rect (220, 185, 5, 40)
        wall_12 =pygame.Rect (220, 225, 40, 5)
        wall_13 =pygame.Rect (260, 185, 5, 40)
        wall_14 =pygame.Rect (260, 225, 40, 5)
        wall_15 =pygame.Rect (300, 185, 5, 40)
        wall_16 =pygame.Rect (300, 225, 40, 5)
        wall_17 =pygame.Rect (340, 185, 5, 40)
        wall_18 =pygame.Rect (340, 225, 40, 5)
        wall_19 =pygame.Rect (380, 185, 5, 40)
        wall_20 =pygame.Rect (380, 225, 40, 5)
        wall_21 =pygame.Rect (420, 185, 5, 40)
        wall_22 =pygame.Rect (420, 225, 40, 5)
        wall_23 =pygame.Rect (460, 185, 5, 40)
        wall_24 =pygame.Rect (460, 225, 40, 5)
        wall_25 =pygame.Rect (500, 185, 5, 40)
        wall_26 =pygame.Rect (500, 225, 40, 5)
        wall_27 =pygame.Rect (540, 185, 5, 40)
        pygame.draw.rect(screen, (0,0,255), wall_1)     
        pygame.draw.rect(screen, (0,0,255), wall_2)
        pygame.draw.rect(screen, (0,255,255), wall_3)
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
        pygame.draw.rect(screen, (0,0,0), wall_18)
        pygame.draw.rect(screen, (0,0,0), wall_19)     
        pygame.draw.rect(screen, (0,0,0), wall_20)
        pygame.draw.rect(screen, (0,0,0), wall_21)
        pygame.draw.rect(screen, (0,0,255), wall_22)     
        pygame.draw.rect(screen, (0,0,0), wall_23)
        pygame.draw.rect(screen, (0,0,0), wall_24)
        pygame.draw.rect(screen, (0,0,255), wall_25)
        pygame.draw.rect(screen, (0,0,0), wall_26)     
        pygame.draw.rect(screen, (0,255,255), wall_27)

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
        if interact(player, wall_17) or interact(player, wall_1) or interact(player, wall_1) or interact(player, wall_2):
          x=30
          y=60
        if interact(player, wall_2) or interact(player, wall_22) or interact(player, wall_2) or interact(player, wall_2):
          x=30
          y=60
        if interact(player, wall_25) or interact(player, wall_2) or interact(player, wall_27):
          x=30
          y=60

  #row 5

        
        wall_1 =pygame.Rect (20, 270, 40, 5)
        wall_2 =pygame.Rect (60, 230, 5, 40)
        wall_3 =pygame.Rect (15, 230, 5, 40)
        wall_4 =pygame.Rect (60, 270, 40, 5)
        wall_5 =pygame.Rect (100, 230, 5, 40)
        wall_6 =pygame.Rect (100, 270, 40, 5)
        wall_7 =pygame.Rect (140, 230, 5, 40)
        wall_8 =pygame.Rect (140, 270, 40, 5)
        wall_9 =pygame.Rect (180, 230, 5, 40)
        wall_10 =pygame.Rect (180, 270, 40, 5)
        wall_11 =pygame.Rect (220, 230, 5, 40)
        wall_12 =pygame.Rect (220, 270, 40, 5)
        wall_13 =pygame.Rect (260, 230, 5, 40)
        wall_14 =pygame.Rect (260, 270, 40, 5)
        wall_15 =pygame.Rect (300, 230, 5, 40)
        wall_16 =pygame.Rect (300, 270, 40, 5)
        wall_17 =pygame.Rect (340, 230, 5, 40)
        wall_18 =pygame.Rect (340, 270, 40, 5)
        wall_19 =pygame.Rect (380, 230, 5, 40)
        wall_20 =pygame.Rect (380, 270, 40, 5)
        wall_21 =pygame.Rect (420, 230, 5, 40)
        wall_22 =pygame.Rect (420, 270, 40, 5)
        wall_23 =pygame.Rect (460, 230, 5, 40)
        wall_24 =pygame.Rect (460, 270, 40, 5)
        wall_25 =pygame.Rect (500, 230, 5, 40)
        wall_26 =pygame.Rect (500, 270, 40, 5)
        wall_27 =pygame.Rect (540, 230, 5, 40)
        pygame.draw.rect(screen, (0,0,0), wall_1)     
        pygame.draw.rect(screen, (0,0,0), wall_2)
        pygame.draw.rect(screen, (0,255,255), wall_3)
        pygame.draw.rect(screen, (0,0,0), wall_4)
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
        pygame.draw.rect(screen, (0,0,0), wall_18)
        pygame.draw.rect(screen, (0,0,255), wall_19)     
        pygame.draw.rect(screen, (0,0,255), wall_20)
        pygame.draw.rect(screen, (0,0,0), wall_21)
        pygame.draw.rect(screen, (0,0,255), wall_22)     
        pygame.draw.rect(screen, (0,0,0), wall_23)
        pygame.draw.rect(screen, (0,0,0), wall_24)
        pygame.draw.rect(screen, (0,0,255), wall_25)
        pygame.draw.rect(screen, (0,0,0), wall_26)     
        pygame.draw.rect(screen, (0,255,255), wall_27)

        if interact(player, wall_3) or interact(player, wall_3) or interact(player, wall_3) or interact(player, wall_3):
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
        if interact(player, wall_17) or interact(player, wall_1) or interact(player, wall_19) or interact(player, wall_20):
          x=30
          y=60
        if interact(player, wall_3) or interact(player, wall_22) or interact(player, wall_3) or interact(player, wall_3):
          x=30
          y=60
        if interact(player, wall_25) or interact(player, wall_3) or interact(player, wall_27):
          x=30
          y=60
  #row 6

        
        wall_1 =pygame.Rect (20, 315, 40, 5)
        wall_2 =pygame.Rect (60, 275, 5, 40)
        wall_3 =pygame.Rect (15, 275, 5, 40)
        wall_4 =pygame.Rect (60, 315, 40, 5)
        wall_5 =pygame.Rect (100, 275, 5, 40)
        wall_6 =pygame.Rect (100, 315, 40, 5)
        wall_7 =pygame.Rect (140, 275, 5, 40)
        wall_8 =pygame.Rect (140, 315, 40, 5)
        wall_9 =pygame.Rect (180, 275, 5, 40)
        wall_10 =pygame.Rect (180, 315, 40, 5)
        wall_11 =pygame.Rect (220, 275, 5, 40)
        wall_12 =pygame.Rect (220, 315, 40, 5)
        wall_13 =pygame.Rect (260, 275, 5, 40)
        wall_14 =pygame.Rect (260, 315, 40, 5)
        wall_15 =pygame.Rect (300, 275, 5, 40)
        wall_16 =pygame.Rect (300, 315, 40, 5)
        wall_17 =pygame.Rect (340, 275, 5, 40)
        wall_18 =pygame.Rect (340, 315, 40, 5)
        wall_19 =pygame.Rect (380, 275, 5, 40)
        wall_20 =pygame.Rect (380, 315, 40, 5)
        wall_21 =pygame.Rect (420, 275, 5, 40)
        wall_22 =pygame.Rect (420, 315, 40, 5)
        wall_23 =pygame.Rect (460, 275, 5, 40)
        wall_24 =pygame.Rect (460, 315, 40, 5)
        wall_25 =pygame.Rect (500, 275, 5, 40)
        wall_26 =pygame.Rect (500, 315, 40, 5)
        wall_27 =pygame.Rect (540, 275, 5, 40)
        pygame.draw.rect(screen, (0,0,0), wall_1)     
        pygame.draw.rect(screen, (0,0,255), wall_2)
        pygame.draw.rect(screen, (0,255,255), wall_3)
        pygame.draw.rect(screen, (0,0,0), wall_4)
        pygame.draw.rect(screen, (0,0,255), wall_5)     
        pygame.draw.rect(screen, (0,0,255), wall_6)
        pygame.draw.rect(screen, (0,0,0), wall_7)
        pygame.draw.rect(screen, (0,0,0), wall_8)     
        pygame.draw.rect(screen, (0,0,0), wall_9)
        pygame.draw.rect(screen, (0,0,0), wall_10)
        pygame.draw.rect(screen, (0,0,0), wall_11)     
        pygame.draw.rect(screen, (0,0,0), wall_12)
        pygame.draw.rect(screen, (0,0,255), wall_13)
        pygame.draw.rect(screen, (0,0,255), wall_14)
        pygame.draw.rect(screen, (0,0,0), wall_15)
        pygame.draw.rect(screen, (0,0,255), wall_16)     
        pygame.draw.rect(screen, (0,0,255), wall_17)
        pygame.draw.rect(screen, (0,0,0), wall_18)
        pygame.draw.rect(screen, (0,0,255), wall_19)     
        pygame.draw.rect(screen, (0,0,0), wall_20)
        pygame.draw.rect(screen, (0,0,0), wall_21)
        pygame.draw.rect(screen, (0,0,255), wall_22)     
        pygame.draw.rect(screen, (0,0,0), wall_23)
        pygame.draw.rect(screen, (0,0,0), wall_24)
        pygame.draw.rect(screen, (0,0,255), wall_25)
        pygame.draw.rect(screen, (0,0,0), wall_26)     
        pygame.draw.rect(screen, (0,255,255), wall_27)
        if interact(player, wall_2) or interact(player, wall_2) or interact(player, wall_3) or interact(player, wall_2):
          x=30
          y=60
        if interact(player, wall_5) or interact(player, wall_6) or interact(player, wall_3) or interact(player, wall_3):
          x=30
          y=60
        if interact(player, wall_13) or interact(player, wall_14) or interact(player, wall_3) or interact(player, wall_16):
          x=30
          y=60
        if interact(player, wall_17) or interact(player, wall_2) or interact(player, wall_19) or interact(player, wall_2):
          x=30
          y=60
        if interact(player, wall_2) or interact(player, wall_22) or interact(player, wall_2) or interact(player, wall_2):
          x=30
          y=60
        if interact(player, wall_25) or interact(player, wall_2) or interact(player, wall_27):
          x=30
          y=60
  #row 7

        
        wall_1 =pygame.Rect (20, 360, 40, 5)
        wall_2 =pygame.Rect (60, 320, 5, 40)
        wall_3 =pygame.Rect (15, 320, 5, 40)
        wall_4 =pygame.Rect (60, 360, 40, 5)
        wall_5 =pygame.Rect (100, 320, 5, 40)
        wall_6 =pygame.Rect (100, 360, 40, 5)
        wall_7 =pygame.Rect (140, 320, 5, 40)
        wall_8 =pygame.Rect (140, 360, 40, 5)
        wall_9 =pygame.Rect (180, 320, 5, 40)
        wall_10 =pygame.Rect (180, 360, 40, 5)
        wall_11 =pygame.Rect (220, 320, 5, 40)
        wall_12 =pygame.Rect (220, 360, 40, 5)
        wall_13 =pygame.Rect (260, 320, 5, 40)
        wall_14 =pygame.Rect (260, 360, 40, 5)
        wall_15 =pygame.Rect (300, 320, 5, 40)
        wall_16 =pygame.Rect (300, 360, 40, 5)
        wall_17 =pygame.Rect (340, 320, 5, 40)
        wall_18 =pygame.Rect (340, 360, 40, 5)
        wall_19 =pygame.Rect (380, 320, 5, 40)
        wall_20 =pygame.Rect (380, 360, 40, 5)
        wall_21 =pygame.Rect (420, 320, 5, 40)
        wall_22 =pygame.Rect (420, 360, 40, 5)
        wall_23 =pygame.Rect (460, 320, 5, 40)
        wall_24 =pygame.Rect (460, 360, 40, 5)
        wall_25 =pygame.Rect (500, 320, 5, 40)
        wall_26 =pygame.Rect (500, 360, 40, 5)
        wall_27 =pygame.Rect (540, 320, 5, 40)
        pygame.draw.rect(screen, (0,0,255), wall_1)     
        pygame.draw.rect(screen, (0,0,0), wall_2)
        pygame.draw.rect(screen, (0,255,255), wall_3)
        pygame.draw.rect(screen, (0,0,255), wall_4)
        pygame.draw.rect(screen, (0,0,0), wall_5)     
        pygame.draw.rect(screen, (0,0,255), wall_6)
        pygame.draw.rect(screen, (0,0,0), wall_7)
        pygame.draw.rect(screen, (0,0,255), wall_8)     
        pygame.draw.rect(screen, (0,0,255), wall_9)
        pygame.draw.rect(screen, (0,0,0), wall_10)
        pygame.draw.rect(screen, (0,0,255), wall_11)     
        pygame.draw.rect(screen, (0,0,0), wall_12)
        pygame.draw.rect(screen, (0,0,255), wall_13)
        pygame.draw.rect(screen, (0,0,0), wall_14)
        pygame.draw.rect(screen, (0,0,0), wall_15)
        pygame.draw.rect(screen, (0,0,0), wall_16)     
        pygame.draw.rect(screen, (0,0,0), wall_17)
        pygame.draw.rect(screen, (0,0,255), wall_18)
        pygame.draw.rect(screen, (0,0,255), wall_19)     
        pygame.draw.rect(screen, (0,0,255), wall_20)
        pygame.draw.rect(screen, (0,0,0), wall_21)
        pygame.draw.rect(screen, (0,0,0), wall_22)     
        pygame.draw.rect(screen, (0,0,255), wall_23)
        pygame.draw.rect(screen, (0,0,0), wall_24)
        pygame.draw.rect(screen, (0,0,255), wall_25)
        pygame.draw.rect(screen, (0,0,0), wall_26)     
        pygame.draw.rect(screen, (0,255,255), wall_27)
        if interact(player, wall_1) or interact(player, wall_1) or interact(player, wall_3) or interact(player, wall_4):
          x=30
          y=60
        if interact(player, wall_1) or interact(player, wall_6) or interact(player, wall_1) or interact(player, wall_8):
          x=30
          y=60
        if interact(player, wall_9) or interact(player, wall_1) or interact(player, wall_11) or interact(player, wall_1):
          x=30
          y=60
        if interact(player, wall_13) or interact(player, wall_1) or interact(player, wall_1) or interact(player, wall_1):
          x=30
          y=60
        if interact(player, wall_1) or interact(player, wall_18) or interact(player, wall_19) or interact(player, wall_20):
          x=30
          y=60
        if interact(player, wall_1) or interact(player, wall_1) or interact(player, wall_23) or interact(player, wall_4):
          x=30
          y=60
        if interact(player, wall_25) or interact(player, wall_6) or interact(player, wall_27):
          x=30
          y=60
  #row 8

        
        wall_1 =pygame.Rect (20, 405, 40, 5)
        wall_2 =pygame.Rect (60, 365, 5, 40)
        wall_3 =pygame.Rect (15, 365, 5, 40)
        wall_4 =pygame.Rect (60, 405, 40, 5)
        wall_5 =pygame.Rect (100, 365, 5, 40)
        wall_6 =pygame.Rect (100, 405, 40, 5)
        wall_7 =pygame.Rect (140, 365, 5, 40)
        wall_8 =pygame.Rect (140, 405, 40, 5)
        wall_9 =pygame.Rect (180, 365, 5, 40)
        wall_10 =pygame.Rect (180, 405, 40, 5)
        wall_11 =pygame.Rect (220, 365, 5, 40)
        wall_12 =pygame.Rect (220, 405, 40, 5)
        wall_13 =pygame.Rect (260, 365, 5, 40)
        wall_14 =pygame.Rect (260, 405, 40, 5)
        wall_15 =pygame.Rect (300, 365, 5, 40)
        wall_16 =pygame.Rect (300, 405, 40, 5)
        wall_17 =pygame.Rect (340, 365, 5, 40)
        wall_18 =pygame.Rect (340, 405, 40, 5)
        wall_19 =pygame.Rect (380, 365, 5, 40)
        wall_20 =pygame.Rect (380, 405, 40, 5)
        wall_21 =pygame.Rect (420, 365, 5, 40)
        wall_22 =pygame.Rect (420, 405, 40, 5)
        wall_23 =pygame.Rect (460, 365, 5, 40)
        wall_24 =pygame.Rect (460, 405, 40, 5)
        wall_25 =pygame.Rect (500, 365, 5, 40)
        wall_26 =pygame.Rect (500, 405, 40, 5)
        wall_27 =pygame.Rect (540, 365, 5, 40)
        pygame.draw.rect(screen, (0,0,0), wall_1)     
        pygame.draw.rect(screen, (0,0,0), wall_2)
        pygame.draw.rect(screen, (0,255,255), wall_3)
        pygame.draw.rect(screen, (0,0,255), wall_4)
        pygame.draw.rect(screen, (0,0,0), wall_5)     
        pygame.draw.rect(screen, (0,0,255), wall_6)
        pygame.draw.rect(screen, (0,0,0), wall_7)
        pygame.draw.rect(screen, (0,0,255), wall_8)     
        pygame.draw.rect(screen, (0,0,0), wall_9)
        pygame.draw.rect(screen, (0,0,0), wall_10)
        pygame.draw.rect(screen, (0,0,255), wall_11)     
        pygame.draw.rect(screen, (0,0,255), wall_12)
        pygame.draw.rect(screen, (0,0,0), wall_13)
        pygame.draw.rect(screen, (0,0,0), wall_14)
        pygame.draw.rect(screen, (0,0,255), wall_15)
        pygame.draw.rect(screen, (0,0,0), wall_16)     
        pygame.draw.rect(screen, (0,0,0), wall_17)
        pygame.draw.rect(screen, (0,0,0), wall_18)
        pygame.draw.rect(screen, (0,0,0), wall_19)     
        pygame.draw.rect(screen, (0,0,255), wall_20)
        pygame.draw.rect(screen, (0,0,255), wall_21)
        pygame.draw.rect(screen, (0,0,0), wall_22)     
        pygame.draw.rect(screen, (0,0,255), wall_23)
        pygame.draw.rect(screen, (0,0,255), wall_24)
        pygame.draw.rect(screen, (0,0,255), wall_25)
        pygame.draw.rect(screen, (0,0,0), wall_26)     
        pygame.draw.rect(screen, (0,255,255), wall_27)
        if interact(player, wall_3) or interact(player, wall_3) or interact(player, wall_3) or interact(player, wall_4):
          x=30
          y=60
        if interact(player, wall_3) or interact(player, wall_6) or interact(player, wall_3) or interact(player, wall_8):
          x=30
          y=60
        if interact(player, wall_3) or interact(player, wall_3) or interact(player, wall_11) or interact(player, wall_12):
          x=30
          y=60
        if interact(player, wall_3) or interact(player, wall_3) or interact(player, wall_15) or interact(player, wall_6):
          x=30
          y=60
        if interact(player, wall_3) or interact(player, wall_3) or interact(player, wall_3) or interact(player, wall_20):
          x=30
          y=60
        if interact(player, wall_21) or interact(player, wall_3) or interact(player, wall_23) or interact(player, wall_24):
          x=30
          y=60
        if interact(player, wall_25) or interact(player, wall_3) or interact(player, wall_27):
          x=30
          y=60
  #row 9

        
        wall_1 =pygame.Rect (20, 450, 40, 5)
        wall_2 =pygame.Rect (60, 410, 5, 40)
        wall_3 =pygame.Rect (15, 410, 5, 40)
        wall_4 =pygame.Rect (60, 450, 40, 5)
        wall_5 =pygame.Rect (100, 410, 5, 40)
        wall_6 =pygame.Rect (100, 450, 40, 5)
        wall_7 =pygame.Rect (140, 410, 5, 40)
        wall_8 =pygame.Rect (140, 450, 40, 5)
        wall_9 =pygame.Rect (180, 410, 5, 40)
        wall_10 =pygame.Rect (180, 450, 40, 5)
        wall_11 =pygame.Rect (220, 410, 5, 40)
        wall_12 =pygame.Rect (220, 450, 40, 5)
        wall_13 =pygame.Rect (260, 410, 5, 40)
        wall_14 =pygame.Rect (260, 450, 40, 5)
        wall_15 =pygame.Rect (300, 410, 5, 40)
        wall_16 =pygame.Rect (300, 450, 40, 5)
        wall_17 =pygame.Rect (340, 410, 5, 40)
        wall_18 =pygame.Rect (340, 450, 40, 5)
        wall_19 =pygame.Rect (380, 410, 5, 40)
        wall_20 =pygame.Rect (380, 450, 40, 5)
        wall_21 =pygame.Rect (420, 410, 5, 40)
        wall_22 =pygame.Rect (420, 450, 40, 5)
        wall_23 =pygame.Rect (460, 410, 5, 40)
        wall_24 =pygame.Rect (460, 450, 40, 5)
        wall_25 =pygame.Rect (500, 410, 5, 40)
        wall_26 =pygame.Rect (500, 450, 40, 5)
        wall_27 =pygame.Rect (540, 410, 5, 40)
        pygame.draw.rect(screen, (0,0,0), wall_1)     
        pygame.draw.rect(screen, (0,0,255), wall_2)
        pygame.draw.rect(screen, (0,255,255), wall_3)
        pygame.draw.rect(screen, (0,0,255), wall_4)
        pygame.draw.rect(screen, (0,0,0), wall_5)     
        pygame.draw.rect(screen, (0,0,0), wall_6)
        pygame.draw.rect(screen, (0,0,0), wall_7)
        pygame.draw.rect(screen, (0,0,0), wall_8)     
        pygame.draw.rect(screen, (0,0,255), wall_9)
        pygame.draw.rect(screen, (0,0,255), wall_10)
        pygame.draw.rect(screen, (0,0,0), wall_11)     
        pygame.draw.rect(screen, (0,0,0), wall_12)
        pygame.draw.rect(screen, (0,0,255), wall_13)
        pygame.draw.rect(screen, (0,0,0), wall_14)
        pygame.draw.rect(screen, (0,0,255), wall_15)
        pygame.draw.rect(screen, (0,0,255), wall_16)     
        pygame.draw.rect(screen, (0,0,255), wall_17)
        pygame.draw.rect(screen, (0,0,0), wall_18)
        pygame.draw.rect(screen, (0,0,0), wall_19)     
        pygame.draw.rect(screen, (0,0,255), wall_20)
        pygame.draw.rect(screen, (0,0,255), wall_21)
        pygame.draw.rect(screen, (0,0,0), wall_22)     
        pygame.draw.rect(screen, (0,0,255), wall_23)
        pygame.draw.rect(screen, (0,0,0), wall_24)
        pygame.draw.rect(screen, (0,0,255), wall_25)
        pygame.draw.rect(screen, (0,0,0), wall_26)     
        pygame.draw.rect(screen, (0,255,255), wall_27)
        if interact(player, wall_2) or interact(player, wall_2) or interact(player, wall_3) or interact(player, wall_4):
          x=30
          y=60
        if interact(player, wall_9) or interact(player, wall_10) or interact(player, wall_2) or interact(player, wall_2):
          x=30
          y=60
        if interact(player, wall_13) or interact(player, wall_1) or interact(player, wall_15) or interact(player, wall_16):
          x=30
          y=60
        if interact(player, wall_17) or interact(player, wall_2) or interact(player, wall_9) or interact(player, wall_20):
          x=30
          y=60
        if interact(player, wall_21) or interact(player, wall_2) or interact(player, wall_23) or interact(player, wall_2):
          x=30
          y=60
        if interact(player, wall_25) or interact(player, wall_2) or interact(player, wall_27):
          x=30
          y=60
  #row 10

        
        wall_1 =pygame.Rect (20, 495, 40, 5)
        wall_2 =pygame.Rect (60, 455, 5, 40)
        wall_3 =pygame.Rect (15, 455, 5, 40)
        wall_4 =pygame.Rect (60, 495, 40, 5)
        wall_5 =pygame.Rect (100, 455, 5, 40)
        wall_6 =pygame.Rect (100, 495, 40, 5)
        wall_7 =pygame.Rect (140, 455, 5, 40)
        wall_8 =pygame.Rect (140, 495, 40, 5)
        wall_9 =pygame.Rect (180, 455, 5, 40)
        wall_10 =pygame.Rect (180, 495, 40, 5)
        wall_11 =pygame.Rect (220, 455, 5, 40)
        wall_12 =pygame.Rect (220, 495, 40, 5)
        wall_13 =pygame.Rect (260, 455, 5, 40)
        wall_14 =pygame.Rect (260, 495, 40, 5)
        wall_15 =pygame.Rect (300, 455, 5, 40)
        wall_16 =pygame.Rect (300, 495, 40, 5)
        wall_17 =pygame.Rect (340, 455, 5, 40)
        wall_18 =pygame.Rect (340, 495, 40, 5)
        wall_19 =pygame.Rect (380, 455, 5, 40)
        wall_20 =pygame.Rect (380, 495, 40, 5)
        wall_21 =pygame.Rect (420, 455, 5, 40)
        wall_22 =pygame.Rect (420, 495, 40, 5)
        wall_23 =pygame.Rect (460, 455, 5, 40)
        wall_24 =pygame.Rect (460, 495, 40, 5)
        wall_25 =pygame.Rect (500, 455, 5, 40)
        wall_26 =pygame.Rect (500, 495, 40, 5)
        wall_27 =pygame.Rect (540, 455, 5, 40)
        pygame.draw.rect(screen, (0,0,0), wall_1)     
        pygame.draw.rect(screen, (0,0,0), wall_2)
        pygame.draw.rect(screen, (0,255,255), wall_3)
        pygame.draw.rect(screen, (0,0,255), wall_4)
        pygame.draw.rect(screen, (0,0,0), wall_5)     
        pygame.draw.rect(screen, (0,0,255), wall_6)
        pygame.draw.rect(screen, (0,0,255), wall_7)
        pygame.draw.rect(screen, (0,0,0), wall_8)     
        pygame.draw.rect(screen, (0,0,0), wall_9)
        pygame.draw.rect(screen, (0,0,0), wall_10)
        pygame.draw.rect(screen, (0,0,255), wall_11)     
        pygame.draw.rect(screen, (0,0,255), wall_12)
        pygame.draw.rect(screen, (0,0,255), wall_13)
        pygame.draw.rect(screen, (0,0,0), wall_14)
        pygame.draw.rect(screen, (0,0,255), wall_15)
        pygame.draw.rect(screen, (0,0,0), wall_16)     
        pygame.draw.rect(screen, (0,0,255), wall_17)
        pygame.draw.rect(screen, (0,0,0), wall_18)
        pygame.draw.rect(screen, (0,0,255), wall_19)     
        pygame.draw.rect(screen, (0,0,0), wall_20)
        pygame.draw.rect(screen, (0,0,0), wall_21)
        pygame.draw.rect(screen, (0,0,0), wall_22)     
        pygame.draw.rect(screen, (0,0,0), wall_23)
        pygame.draw.rect(screen, (0,0,255), wall_24)
        pygame.draw.rect(screen, (0,0,255), wall_25)
        pygame.draw.rect(screen, (0,0,0), wall_26)     
        pygame.draw.rect(screen, (0,255,255), wall_27)
        if interact(player, wall_1) or interact(player, wall_2) or interact(player, wall_3) or interact(player, wall_4):
          x=30
          y=60
        if interact(player, wall_5) or interact(player, wall_6) or interact(player, wall_7) or interact(player, wall_1):
          x=30
          y=60
        if interact(player, wall_1) or interact(player, wall_1) or interact(player, wall_11) or interact(player, wall_12):
          x=30
          y=60
        if interact(player, wall_13) or interact(player, wall_1) or interact(player, wall_15) or interact(player, wall_1):
          x=30
          y=60
        if interact(player, wall_17) or interact(player, wall_1) or interact(player, wall_19) or interact(player, wall_2):
          x=30
          y=60
        if interact(player, wall_2) or interact(player, wall_2) or interact(player, wall_2) or interact(player, wall_24):
          x=30
          y=60
        if interact(player, wall_2) or interact(player, wall_2) or interact(player, wall_27):
          x=30
          y=60

        #row 11

        
        wall_1 =pygame.Rect (20, 540, 40, 5)
        wall_2 =pygame.Rect (60, 500, 5, 40)
        wall_3 =pygame.Rect (15, 500, 5, 40)
        wall_4 =pygame.Rect (60, 540, 40, 5)
        wall_5 =pygame.Rect (100, 500, 5, 40)
        wall_6 =pygame.Rect (100, 540, 40, 5)
        wall_7 =pygame.Rect (140, 500, 5, 40)
        wall_8 =pygame.Rect (140, 540, 40, 5)
        wall_9 =pygame.Rect (180, 500, 5, 40)
        wall_10 =pygame.Rect (180, 540, 40, 5)
        wall_11 =pygame.Rect (220, 500, 5, 40)
        wall_12 =pygame.Rect (220, 540, 40, 5)
        wall_13 =pygame.Rect (260, 500, 5, 40)
        wall_14 =pygame.Rect (260, 540, 40, 5)
        wall_15 =pygame.Rect (300, 500, 5, 40)
        wall_16 =pygame.Rect (300, 540, 40, 5)
        wall_17 =pygame.Rect (340, 500, 5, 40)
        wall_18 =pygame.Rect (340, 540, 40, 5)
        wall_19 =pygame.Rect (380, 500, 5, 40)
        wall_20 =pygame.Rect (380, 540, 40, 5)
        wall_21 =pygame.Rect (420, 500, 5, 40)
        wall_22 =pygame.Rect (420, 540, 40, 5)
        wall_23 =pygame.Rect (460, 500, 5, 40)
        wall_24 =pygame.Rect (460, 540, 40, 5)
        wall_25 =pygame.Rect (500, 500, 5, 40)
        wall_26 =pygame.Rect (500, 540, 40, 5)
        wall_27 =pygame.Rect (540, 500, 5, 40)
        pygame.draw.rect(screen, (0,0,255), wall_1)     
        pygame.draw.rect(screen, (0,0,255), wall_2)
        pygame.draw.rect(screen, (0,255,255), wall_3)
        pygame.draw.rect(screen, (0,0,0), wall_4)
        pygame.draw.rect(screen, (0,0,0), wall_5)     
        pygame.draw.rect(screen, (0,0,0), wall_6)
        pygame.draw.rect(screen, (0,0,255), wall_7)
        pygame.draw.rect(screen, (0,0,0), wall_8)     
        pygame.draw.rect(screen, (0,0,255), wall_9)
        pygame.draw.rect(screen, (0,0,255), wall_10)
        pygame.draw.rect(screen, (0,0,255), wall_11)     
        pygame.draw.rect(screen, (0,0,0), wall_12)
        pygame.draw.rect(screen, (0,0,0), wall_13)
        pygame.draw.rect(screen, (0,0,255), wall_14)
        pygame.draw.rect(screen, (0,0,255), wall_15)
        pygame.draw.rect(screen, (0,0,255), wall_16)     
        pygame.draw.rect(screen, (0,0,0), wall_17)
        pygame.draw.rect(screen, (0,0,255), wall_18)
        pygame.draw.rect(screen, (0,0,255), wall_19)     
        pygame.draw.rect(screen, (0,0,0), wall_20)
        pygame.draw.rect(screen, (0,0,255), wall_21)
        pygame.draw.rect(screen, (0,0,255), wall_22)     
        pygame.draw.rect(screen, (0,0,0), wall_23)
        pygame.draw.rect(screen, (0,0,255), wall_24)
        pygame.draw.rect(screen, (0,0,255), wall_25)
        pygame.draw.rect(screen, (0,0,0), wall_26)     
        pygame.draw.rect(screen, (0,255,255), wall_27)
        if interact(player, wall_1) or interact(player, wall_2) or interact(player, wall_3) or interact(player, wall_1):
          x=30
          y=60
        if interact(player, wall_1) or interact(player, wall_1) or interact(player, wall_7) or interact(player, wall_1):
          x=30
          y=60
        if interact(player, wall_9) or interact(player, wall_10) or interact(player, wall_11) or interact(player, wall_1):
          x=30
          y=60
        if interact(player, wall_1) or interact(player, wall_14) or interact(player, wall_15) or interact(player, wall_16):
          x=30
          y=60
        if interact(player, wall_1) or interact(player, wall_18) or interact(player, wall_19) or interact(player, wall_2):
          x=30
          y=60
        if interact(player, wall_21) or interact(player, wall_22) or interact(player, wall_2) or interact(player, wall_24):
          x=30
          y=60
        if interact(player, wall_25) or interact(player, wall_2) or interact(player, wall_27):
          x=30
          y=60
        #row 12

        
        wall_1 =pygame.Rect (20, 585, 40, 5)
        wall_2 =pygame.Rect (60, 545, 5, 40)
        wall_3 =pygame.Rect (15, 545, 5, 40)
        wall_4 =pygame.Rect (60, 585, 40, 5)
        wall_5 =pygame.Rect (100, 545, 5, 40)
        wall_6 =pygame.Rect (100, 585, 40, 5)
        wall_7 =pygame.Rect (140, 545, 5, 40)
        wall_8 =pygame.Rect (140, 585, 40, 5)
        wall_9 =pygame.Rect (180, 545, 5, 40)
        wall_10 =pygame.Rect (180, 585, 40, 5)
        wall_11 =pygame.Rect (220, 545, 5, 40)
        wall_12 =pygame.Rect (220, 585, 40, 5)
        wall_13 =pygame.Rect (260, 545, 5, 40)
        wall_14 =pygame.Rect (260, 585, 40, 5)
        wall_15 =pygame.Rect (300, 545, 5, 40)
        wall_16 =pygame.Rect (300, 585, 40, 5)
        wall_17 =pygame.Rect (340, 545, 5, 40)
        wall_18 =pygame.Rect (340, 585, 40, 5)
        wall_19 =pygame.Rect (380, 545, 5, 40)
        wall_20 =pygame.Rect (380, 585, 40, 5)
        wall_21 =pygame.Rect (420, 545, 5, 40)
        wall_22 =pygame.Rect (420, 585, 40, 5)
        wall_23 =pygame.Rect (460, 545, 5, 40)
        wall_24 =pygame.Rect (460, 585, 40, 5)
        wall_25 =pygame.Rect (500, 545, 5, 40)
        wall_26 =pygame.Rect (500, 585, 40, 5)
        wall_27 =pygame.Rect (540, 545, 5, 40)
        pygame.draw.rect(screen, (0,255,255), wall_1)     
        pygame.draw.rect(screen, (0,0,0), wall_2)
        pygame.draw.rect(screen, (0,255,255), wall_3)
        pygame.draw.rect(screen, (0,255,255), wall_4)
        pygame.draw.rect(screen, (0,0,255), wall_5)     
        pygame.draw.rect(screen, (0,255,255), wall_6)
        pygame.draw.rect(screen, (0,0,0), wall_7)
        pygame.draw.rect(screen, (0,255,255), wall_8)     
        pygame.draw.rect(screen, (0,0,0), wall_9)
        pygame.draw.rect(screen, (0,255,255), wall_10)
        pygame.draw.rect(screen, (0,0,0), wall_11)     
        pygame.draw.rect(screen, (0,255,255), wall_12)
        pygame.draw.rect(screen, (0,0,255), wall_13)
        pygame.draw.rect(screen, (0,255,255), wall_14)
        pygame.draw.rect(screen, (0,0,0), wall_15)
        pygame.draw.rect(screen, (0,255,255), wall_16)     
        pygame.draw.rect(screen, (0,0,0), wall_17)
        pygame.draw.rect(screen, (0,255,255), wall_18)
        pygame.draw.rect(screen, (0,0,0), wall_19)     
        pygame.draw.rect(screen, (0,255,255), wall_20)
        pygame.draw.rect(screen, (0,0,0), wall_21)
        pygame.draw.rect(screen, (0,255,255), wall_22)     
        pygame.draw.rect(screen, (0,0,0), wall_23)
        pygame.draw.rect(screen, (0,255,255), wall_24)
        pygame.draw.rect(screen, (0,0,0), wall_25)
        pygame.draw.rect(screen, (0,255,255), wall_26)     
        pygame.draw.rect(screen, (0,255,255), wall_27)
        if interact(player, wall_1) or interact(player, wall_1) or interact(player, wall_3) or interact(player, wall_4):
          x=30
          y=60
        if interact(player, wall_5) or interact(player, wall_6) or interact(player, wall_6) or interact(player, wall_8):
          x=30
          y=60
        if interact(player, wall_6) or interact(player, wall_10) or interact(player, wall_11) or interact(player, wall_12):
          x=30
          y=60
        if interact(player, wall_13) or interact(player, wall_14) or interact(player, wall_1) or interact(player, wall_16):
          x=30
          y=60
        if interact(player, wall_1) or interact(player, wall_18) or interact(player, wall_1) or interact(player, wall_20):
          x=30
          y=60
        if interact(player, wall_1) or interact(player, wall_22) or interact(player, wall_3) or interact(player, wall_24):
          x=30
          y=60
        if interact(player, wall_5) or interact(player, wall_26) or interact(player, wall_27):
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
        if event.type == pygame.KEYUP and event.key == pygame.K_w:
            y=y-10
        if event.type == pygame.KEYUP and event.key == pygame.K_s:
            y=y+10
        if event.type == pygame.KEYUP and event.key == pygame.K_a:
            x=x-10
        if event.type == pygame.KEYUP and event.key == pygame.K_d:
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
        
        
            
            
            
