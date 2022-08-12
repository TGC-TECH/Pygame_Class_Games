#initialization 
import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((550, 500))
pygame.display.set_caption('MazeGame')
myfont = pygame.font.Font(None, 60)
clock = pygame.time.Clock()
clock.tick(60)
label = myfont.render("MazeGame", 1, (255, 255, 255))
x = 30
y = 60
color = (255, 255, 255)
draw = False
player = pygame.Rect(12, 12, 60, 60) #sets up player rect
win = pygame.Rect(300, 300, 20, 20) #sets up end rect
can_win = False

def intersect(r1, r2):#r1 represents the first rectangle and r2 represents the second
    c1 = (r1.x < (r2.x + r2.width))
    c2 = ((r1.x + r1.width) > r2.x)
    c3 = (r1.y < (r2.y + r2.height))
    c4 = ((r1.height + r1.y) > r2.y)
    if c1 and c2 and c3 and c4:
        return True
    else:
        return False

#gameloop 
while True:
    screen.blit(label, (50, 10)) #title
    if not intersect(player, win):
        player = pygame.Rect(x, y, 30, 30)
        pygame.draw.rect(screen, color, player)

        #maze
        wall_1 = pygame.Rect(0, 50, 600, 5)
        wall_2 = pygame.Rect(0, 95, 200, 5)
        wall_3 = pygame.Rect(245, 95, 250, 5)
        wall_4 = pygame.Rect(540, 50, 5, 400)
        wall_5 = pygame.Rect(200, 95, 5, 150)
        wall_6 = pygame.Rect(245, 100, 5, 150)
        wall_7 = pygame.Rect(245, 245, 250, 5)
        wall_8 = pygame.Rect(300, 50, 59, 40)
        wall_9 = pygame.Rect(200, 100, 5, 250)
        wall_10 = pygame.Rect(200, 350, 340, 5)
        pygame.draw.rect(screen, (0,0,255), wall_1)
        pygame.draw.rect(screen, (0,0,255), wall_2)
        pygame.draw.rect(screen, (0,0,255), wall_3)
        pygame.draw.rect(screen, (0,0,255), wall_4)
        pygame.draw.rect(screen, (0,0,255), wall_5)
        pygame.draw.rect(screen, (0,0,255), wall_6)
        pygame.draw.rect(screen, (0,0,255), wall_7)
        pygame.draw.rect(screen, (0,0,255), wall_8)
        pygame.draw.rect(screen, (0,0,255), wall_9)
        pygame.draw.rect(screen, (0,0,255), wall_10)
        #mazeDetection
        if intersect(player, wall_1) or intersect(player, wall_2) or intersect(player, wall_3) or intersect(player, wall_4) or intersect(player, wall_5) or intersect(player, wall_6) or  intersect(player, wall_7) or  intersect(player, wall_9) or  intersect(player, wall_10):
            x=30  
            y=60
        if intersect(player, wall_8):
            can_win = True
        if can_win == True:
            pygame.draw.rect(screen, (255,0,0), win)


    elif can_win == True:
        label = myfont.render("YouWin", 1, (255, 255, 255))

    

    
    
    

    
    pygame.display.update()
    screen.fill((0,0,0))# clears display 
    

    
    #input
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            label = myfont.render("Space Pressed!", 1, (0, 255, 0))
            x=200
            y=10
            color = (255, 10, 0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            draw = not draw
            print("a pressed")
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            y=y-5
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            y=y+5
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            x=x-5
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            x=x+5


            

print("Hello World!")
