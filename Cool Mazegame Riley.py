#initialization 
import pygame, sys, random
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((850, 850))
pygame.display.set_caption('MazeGame')
myfont = pygame.font.Font(None, 60)
colorfont = pygame.font.Font(None, 30)

clock = pygame.time.Clock()
clock.tick(60)
label = myfont.render("MazeGame", 1, (255, 255, 255))
color_direct = colorfont.render("Press r to change your player to red, p for pink, v for violet, and so on...", 1, (255, 255, 255))
r = colorfont.render("r", 1, (255, 255, 255))
o = colorfont.render("o", 1, (255, 255, 255))
ye = colorfont.render("y", 1, (255, 255, 255))
g = colorfont.render("g", 1, (255, 255, 255))
b = colorfont.render("b", 1, (255, 255, 255))
v = colorfont.render("v", 1, (255, 255, 255))
p = colorfont.render("p", 1, (255, 255, 255))
x = 30
y = 60
r_r = random.randrange(0, 255)
r_g = random.randrange(0, 255)
r_b = random.randrange(0, 255)
color = (r_r, r_g, r_b)
draw = False
player = pygame.Rect(12, 12, 60, 60) #sets up player rect
win = pygame.Rect(400, 300, 20, 20) #sets up end rect
secret_cheater = pygame.Rect(300, 170, 20, 20)
fun_button = pygame.Rect(800, 800, 60, 60)
secret_death_key = pygame.Rect(800, 800, 100, 100)
red_color = pygame.Rect(600, 700, 30, 30)
orange_color = pygame.Rect(630, 700, 30, 30)
yellow_color = pygame.Rect(660, 700, 30, 30)
green_color = pygame.Rect(690, 700, 30, 30)
blue_color = pygame.Rect(720, 700, 30, 30)
violet_color = pygame.Rect(750, 700, 30, 30)
pink_color = pygame.Rect(780, 700, 30, 30)
b_r = True
b_o = True
b_y = True
b_g = True
b_b = True
b_p = True
b_v = True



color_change = True
wall_hit = True
move_left = False
move_right = False
move_down = False
move_up = False
x_wall = 0
y_wall = 120
x_wall2 = 210
y_wall2 = 600
dolor = (0, 0, 0)

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
    current_time = pygame.time.get_ticks()/1000 # for automatic movement yay
    last_time = 0
    current_time2 = pygame.time.get_ticks()/1000 # for automatic movement yay
    last_time2 = 0
    if current_time > (last_time + 1):
        x_wall = x_wall + 1
        last_time = current_time
    if current_time2 > (last_time2 + 1):
        y_wall2 = y_wall2 + .3
        last_time2 = current_time2
        
    if x_wall >= 650:
        x_wall = x_wall - 850
    if y_wall2 >= 800:
        y_wall2 = y_wall2 - 400
        
    screen.blit(label, (50, 10))# title
    

    pygame.draw.rect(screen, dolor, fun_button)
    if not intersect(player, win):
        screen.blit(r, (600, 710))
        screen.blit(o, (630, 710))
        screen.blit(ye, (670, 710))
        screen.blit(g, (690, 710))
        screen.blit(b, (720, 710))
        screen.blit(v, (750, 710))
        screen.blit(p, (780, 710))
        screen.blit(color_direct, (5, 800))
        
        screen.blit(color_direct, (5, 800))# color directions yay!!!
        player = pygame.Rect(x, y, 30, 30)
        pygame.draw.rect(screen, (r_r, r_g, r_b), player)
        pygame.draw.rect(screen, (255,0,0), win)
        pygame.draw.rect(screen, color, secret_cheater)
        pygame.draw.rect(screen, (255,0,0), red_color)
        pygame.draw.rect(screen, (254, 186, 79), orange_color)
        pygame.draw.rect(screen, (255, 253, 116), yellow_color)
        pygame.draw.rect(screen, (11, 102, 35), green_color)
        pygame.draw.rect(screen, (137, 207, 240), blue_color)
        pygame.draw.rect(screen, (243, 100, 248), violet_color)
        pygame.draw.rect(screen, (255,183, 197), pink_color)

        # color interaction
            
        if b_r is False:
            pygame.draw.rect(screen, (255, 0, 0), player)
        if b_o is False:
            pygame.draw.rect(screen, (254, 186, 79), player)
        if b_y is False:
            pygame.draw.rect(screen, (255, 253, 116), player)
        if b_g is False:
            pygame.draw.rect(screen, (11, 102, 35), player)
        if b_b is False:
            pygame.draw.rect(screen, (137, 207, 240), player)
        if b_v is False:
            pygame.draw.rect(screen, (243, 100, 248), player)
        if b_p is False:
            pygame.draw.rect(screen, (255, 183, 197), player)

        
            
        #maze
        wall_fun = pygame.Rect(x_wall, y_wall, 200, 5)
        wall_weird = pygame.Rect(x_wall2, y_wall2, 5, 200)
        wall_1 = pygame.Rect(0, 50, 700, 5)
        wall_2 = pygame.Rect(0, 95, 200, 5)
        wall_3 = pygame.Rect(245, 95, 250, 5)
        wall_4 = pygame.Rect(700, 50, 5, 395)
        wall_5 = pygame.Rect(200, 95, 5, 150)
        wall_6 = pygame.Rect(245, 95, 5, 150)
        wall_7 = pygame.Rect(245, 245, 250, 5)
        wall_8 = pygame.Rect(490, 95, 5, 150)
        wall_9 = pygame.Rect(105, 245, 100, 5)
        wall_10 = pygame.Rect(105, 145, 5, 100)
        wall_11 = pygame.Rect(0, 145, 105, 5)
        wall_12 = pygame.Rect(5, 145, 5, 600)
        wall_13 = pygame.Rect(55, 195, 5, 200)
        wall_14 = pygame.Rect(105, 285, 465, 5)   #DRAW THE WALL
        wall_15 = pygame.Rect(105, 285, 5, 110)
        wall_16 = pygame.Rect(55, 395, 150, 5)
        wall_17 = pygame.Rect(205, 395, 5, 85)
        wall_18 = pygame.Rect(60,480, 150, 5)
        wall_19 = pygame.Rect(5,440, 135, 5)
        wall_20 = pygame.Rect(60, 480, 5, 210)
        wall_21 = pygame.Rect(5, 745, 365, 5)
        wall_22 = pygame.Rect(60, 685, 250, 5)
        wall_23 = pygame.Rect(310, 490, 5, 200)
        wall_24 = pygame.Rect(370, 490, 5, 260)
        wall_25 = pygame.Rect(370, 490, 150, 5)
        wall_26 = pygame.Rect(370, 440, 150, 5)
        wall_27 = pygame.Rect(520, 490, 5, 100)
        wall_28 = pygame.Rect(570, 285, 5, 310)
        wall_29 = pygame.Rect(370, 340, 5, 105)
        wall_30 = pygame.Rect(370, 340, 150, 5)
        wall_31 = pygame.Rect(465, 390, 105, 5)
        wall_death = pygame.Rect(370, 290, 5, 50)
        wall_33 = pygame.Rect(520, 590, 50, 5)
        wall_34 = pygame.Rect(650, 220, 50, 5)   #DRAW THE WALL
        wall_35 = pygame.Rect(570, 440, 135, 5)
        wall_36 = pygame.Rect(450, 290, 5, 50)
        wall_37 = pygame.Rect(230, 490, 85, 5)
        wall_38 = pygame.Rect(230,285, 5, 205)
        wall_39 = pygame.Rect(290,380, 80, 5)
        wall_40 = pygame.Rect(650, 95, 5, 205)
       #draw the rect#
        pygame.draw.rect(screen, (207, 159, 255), wall_weird)
        pygame.draw.rect(screen, (207, 159, 255), wall_fun)
        pygame.draw.rect(screen, (207, 159, 255), wall_1)
        pygame.draw.rect(screen, (207, 159, 255), wall_2)
        pygame.draw.rect(screen, (207, 159, 255), wall_3)
        pygame.draw.rect(screen, (207, 159, 255), wall_4)
        pygame.draw.rect(screen, (207, 159, 255), wall_5)
        pygame.draw.rect(screen, (207, 159, 255), wall_6)
        pygame.draw.rect(screen, (207, 159, 255), wall_7)
        pygame.draw.rect(screen, (207, 159, 255), wall_8)
        pygame.draw.rect(screen, (207, 159, 255), wall_9)
        pygame.draw.rect(screen, (207, 159, 255), wall_10)
        pygame.draw.rect(screen, (207, 159, 255), wall_11)
        pygame.draw.rect(screen, (207, 159, 255), wall_12)
        pygame.draw.rect(screen, (207, 159, 255), wall_13)
        pygame.draw.rect(screen, (207, 159, 255), wall_14)
        pygame.draw.rect(screen, (207, 159, 255), wall_15)
        pygame.draw.rect(screen, (207, 159, 255), wall_16)
        pygame.draw.rect(screen, (207, 159, 255), wall_17)
        pygame.draw.rect(screen, (207, 159, 255), wall_18)
        pygame.draw.rect(screen, (207, 159, 255), wall_19)
        pygame.draw.rect(screen, (207, 159, 255), wall_20)
        pygame.draw.rect(screen, (207, 159, 255), wall_21)
        pygame.draw.rect(screen, (207, 159, 255), wall_22)
        pygame.draw.rect(screen, (207, 159, 255), wall_23)
        pygame.draw.rect(screen, (207, 159, 255), wall_24)
        pygame.draw.rect(screen, (207, 159, 255), wall_25)
        pygame.draw.rect(screen, (207, 159, 255), wall_26)
        pygame.draw.rect(screen, (207, 159, 255), wall_27)
        pygame.draw.rect(screen, (207, 159, 255), wall_28)
        pygame.draw.rect(screen, (207, 159, 255), wall_29)
        pygame.draw.rect(screen, (207, 159, 255), wall_30)
        pygame.draw.rect(screen, (207, 159, 255), wall_31)
        pygame.draw.rect(screen, (0, 0, 0), wall_death)
        pygame.draw.rect(screen, (207, 159, 255), wall_33)
        pygame.draw.rect(screen, (207, 159, 255), wall_34)
        pygame.draw.rect(screen, (207, 159, 255), wall_35)
        pygame.draw.rect(screen, (207, 159, 255), wall_36)
        pygame.draw.rect(screen, (207, 159, 255), wall_37)
        pygame.draw.rect(screen, (207, 159, 255), wall_38)
        pygame.draw.rect(screen, (207, 159, 255), wall_39)
        pygame.draw.rect(screen, (207, 159, 255), wall_40)
      
        
    
        #mazeDetection
        walls = [wall_fun,
                 wall_weird,
                 wall_1,
                 wall_2,
                 wall_3,
                 wall_4,
                 wall_5,
                 wall_6,
                 wall_7,
                 wall_8,
                 wall_9,
                 wall_10,
                 wall_11,
                 wall_12,
                 wall_13,
                 wall_14,
                 wall_15,
                 wall_16,
                 wall_17,
                 wall_18,
                 wall_19,
                 wall_20,
                 wall_21,
                 wall_22,
                 wall_23,
                 wall_24,
                 wall_25,
                 wall_26,
                 wall_27,
                 wall_28,
                 wall_29,
                 wall_30,
                 wall_31,
                 wall_death,
                 wall_33,
                 wall_34,
                 wall_35,
                 wall_37,
                 wall_38,
                 wall_39,
                 wall_40]
        secrets = [
            secret_cheater,
            secret_death_key]

        for secret in secrets:
            if intersect(player, secret_cheater):
                    label = myfont.render("Cheater... here is your punishment", 1, (r_r, r_g, r_b))
                    current_tim = pygame.time.get_ticks()/2000
                    if current_tim > 3:
                        screen.fill((255, 0, 0))
        for wall in walls:
            if intersect(player, wall) and wall_hit:
                x=30
                y=60
    else:
        label = myfont.render("YouWin", 1, (255, 255, 255))
        color_change = False
    if color_change is True:
            dolor = (0, 0, 0)
    else:
        dolor = (r_r, r_g, r_b)



    
    
    

    
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
            color = (r_r, r_b, r_g)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            draw = not draw
            print("a pressed")
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
            wall_hit = not wall_hit
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            move_up = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            move_down = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            move_left = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            move_right = True
        if event.type == pygame.KEYUP and event.key == pygame.K_w:
           move_up = False
        if event.type == pygame.KEYUP and event.key == pygame.K_s:
           move_down = False
        if event.type == pygame.KEYUP and event.key == pygame.K_a:
           move_left = False
        if event.type == pygame.KEYUP and event.key == pygame.K_d:
           move_right = False
        if event.type == pygame.KEYUP and event.key == pygame.K_r:
            b_r = False
            b_o = True
            b_y = True
            b_g = True
            b_b = True
            b_v = True
            b_p = True
        
        if event.type == pygame.KEYUP and event.key == pygame.K_o:
            b_r = True
            b_o = False
            b_y = True
            b_g = True
            b_b = True
            b_v = True
            b_p = True
            
        if event.type == pygame.KEYUP and event.key == pygame.K_y:
            b_r = True
            b_o = True
            b_y = False
            b_g = True
            b_b = True
            b_v = True
            b_p = True
          
        if event.type == pygame.KEYUP and event.key == pygame.K_g:
            b_r = True
            b_o = True
            b_y = True
            b_g = False
            b_b = True
            b_v = True
            b_p = True
        if event.type == pygame.KEYUP and event.key == pygame.K_b:
            b_r = True
            b_o = True
            b_y = True
            b_g = True
            b_b = False
            b_v = True
            b_p = True
            
        if event.type == pygame.KEYUP and event.key == pygame.K_v:
            b_r = True
            b_o = True
            b_y = True
            b_g = True
            b_b = True
            b_v = False
            b_p = True
          
        if event.type == pygame.KEYUP and event.key == pygame.K_p:
            b_r = True
            b_o = True
            b_y = True
            b_g = True
            b_b = True
            b_v = True
            b_p = False
          

        
        if move_up:
            y = y - 5
        if move_down:
            y = y + 5
        if move_left:
            x = x - 5
        if move_right:
            x = x + 5


            

print("Hello World!")
