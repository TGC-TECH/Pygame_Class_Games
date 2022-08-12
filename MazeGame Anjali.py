import pygame, sys, random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((550, 600))

pygame.display.set_caption('Hello')
myfont = pygame.font.Font(None, 60)
clock = pygame.time.Clock()
clock.tick(60)
label = myfont.render("MazeGame", 1, (255, 255, 255))
#label = myfont.render("Hello World!", 1, (128,0,0))
x=30
y=30
color = (255, 255, 255)
draw = False
player = pygame.Rect(12, 12, 30, 30) #sets player rct
win = pygame.Rect(525, 575, 20, 20)
x_w = 100 
y_w = 165
color = (
    random.randint(0, 255),
    random.randint(0, 255),
    random.randint(0, 255)
    )
    


def intersect(r1, r2):
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
    
    current_time = (int) (pygame.time.get_ticks()/1000) #for automatic movement

    #print(current_time)
    if current_time %  3 == 0:
         x_w = x_w + .1
         
    if current_time % 6 == 0:
        x_w = x_w - .2
        
        screen.blit(label, (50, 10))
    if not intersect(player, win):
        player = pygame.Rect(x, y, 20, 20)
        pygame.draw.rect(screen, color, player)
        pygame.draw.rect(screen, ((255, 0, 0)), win)

    #maze
        walls = [
            pygame.Rect(0, 50, 600, 5),
            pygame.Rect (0, 95, 200, 5),
            pygame.Rect (245, 95, 125, 5),
            pygame.Rect (540, 50, 5, 400),
            pygame.Rect (200, 95, 5, 150),
            pygame.Rect (245, 95, 5, 150),
            pygame.Rect (245, 245, 100, 5),
            pygame.Rect (0, 245, 200, 5),
            pygame.Rect (55, 285, 125, 5),
            pygame.Rect(345, 245, 5, 100),
            pygame.Rect(345, 245, 5, 120),
            pygame.Rect(345, 365, 145, 5),  
            pygame.Rect(x_w, y_w, 145, 5),
            pygame.Rect(486, 95, 5, 275),
            pygame.Rect(288, 290, 5, 65),
            pygame.Rect(288, 411, 150, 5),
            pygame.Rect(438, 410, 5, 120),
            pygame.Rect(50, 530, 395, 5),
            pygame.Rect (230, 285, 65, 5),
            pygame.Rect(175, 285, 5, 50),
            pygame.Rect(175, 335, 50, 5),
            pygame.Rect(225, 285, 5, 55),
            pygame.Rect (415, 95, 75, 5),
            pygame.Rect (415, 95, 5, 100),
            pygame.Rect (370, 95, 5, 100),
            pygame.Rect (370, 195, 50, 5),
            pygame.Rect (50, 405, 5, 125),
            pygame.Rect (50, 285, 5, 75),
            pygame.Rect (55, 355, 235, 5),
            pygame.Rect (55, 408, 235, 5)
             
            
            
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
    screen.fill ((0,0,0))# clears display

    #input
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            label = myfont.render ("Hello World!", 1, (0, 255, 0))
            x=200
            y=10
            color = (255, 10, 0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            draw= not draw
            print("a pressed")

        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            y=y-5
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            y=y+5                                              
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            x=x-5
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            x=x+5

print ("MazeGame")


