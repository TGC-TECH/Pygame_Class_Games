#initialization 
import pygame, sys, random
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
color = (
    random.randint(0, 255),
    random.randint(0, 255),
    random.randint(0, 255)
)
draw = False
player = pygame.Rect(12, 12, 60, 60) #sets up player rect
win = pygame.Rect(400, 400, 20, 20) #sets up end rect
x_w = 0
y_w = 165



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
  
    current_time = (int)(pygame.time.get_ticks()/1000) #for automatic movement
    #print(current_time)
    #print(current_time % 5)
    if current_time %  3 == 0:
        x_w = x_w + .1
    if current_time % 6 == 0:
        x_w = 0

    
    screen.blit(label, (50, 10)) #title
    
    if not intersect(player, win):
        player = pygame.Rect(x, y, 30, 30)
        pygame.draw.rect(screen, (255,0,0), win)
        pygame.draw.rect(screen, color, player)

        #maze
        walls = [
            pygame.Rect(0, 50, 600, 5),
            pygame.Rect(0, 95, 200, 5),
            pygame.Rect(245, 95, 250, 5),
            pygame.Rect(540, 50, 5, 400),
            pygame.Rect(200, 95, 5, 150),
            pygame.Rect(245, 95, 5, 150),
            pygame.Rect(245, 245, 100, 5),
            pygame.Rect(0, 245, 200, 5),
            pygame.Rect(x_w, y_w, 200, 5),
            pygame.Rect(345, 245, 5, 95),
            pygame.Rect(250, 340, 100, 5),
            pygame.Rect(305, 280, 5, 25),
            pygame.Rect(215, 305, 93, 5),
            pygame.Rect(250, 340, 5, 86)
        ]

        for wall in walls:
            pygame.draw.rect(screen, (0,0,255), wall)


        #mazeDetection
        for wall in walls:
            if intersect(player, wall):
                x=30
                y=60
    else:
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
