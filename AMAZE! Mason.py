import pygame, sys
import random
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((850, 850))
pygame.display.set_caption("Coffee")
myfont = pygame.font.Font(None, 60)
colorfont = pygame.font.Font(None, 30)
clock = pygame.time.Clock()
clock.tick(60)
label = myfont.render("Maze!", 1, (0, 255, 0))
label2 = colorfont.render("Press R for red, B for blue, and so on!", 1, (0, 255, 0))
x = 30
y = 30
random_r = random.randrange(0, 255)
random_g = random.randrange(0, 255)
random_b = random.randrange(0, 255)
color = (random_r, random_g, random_b)
draw = False
player = pygame.Rect(12, 12, 60, 60)
win = pygame.Rect(400, 300, 20, 20)
secret_death_key = pygame.Rect(555, 60, 20, 20)
secret_cheater = pygame.Rect(300, 170, 20, 20,)
rectangle1 = pygame.Rect(12, 12, 60, 60)
rectangle2 = pygame.Rect(100, 100, 60, 60)
fun_button = pygame.Rect(800, 800, 100, 100)
b_red = pygame.Rect(500, 700, 30, 30)
b_orange = pygame.Rect(540, 700, 30, 30)
b_yellow = pygame.Rect(580, 700, 30, 30)
b_green = pygame.Rect(620, 700, 30, 30)
b_blue = pygame.Rect(660, 700, 30, 30)
b_indago = pygame.Rect(700, 700, 30, 30)
b_purple = pygame.Rect(740, 700, 30, 30)
b_red2 = True
b_orange2 = True
b_yellow2 = True
b_green2 = True
b_blue2 = True
b_indago2 = True
b_purple2 = True
color_change = True
wall_hit = True
move_left = False
move_right = False
move_down = False
move_up = False
x_w = 0
y_w = 105
colour = (0, 0, 0)
x_wall2 = 210
y_wall2 = 610



def intersect(r1, r2):
    cond1 = (r1.x < (r2.x + r2.width))
    cond2 = ((r1.x + r1.width) > r2.x)
    cond3 = (r1.y < (r2.y + r2.height))
    cond4 = ((r1.height + r1.y) > r2.y)
    if cond1 and cond2 and cond3 and cond4:
        return True
    else:
        return False

    

        
    
while True:
    current_time = pygame.time.get_ticks()/1
    last_time = 0
    if current_time > last_time + 0.7:
        x_w = x_w + 0.7
    if x_w >= 650:
        x_w = x_w - 850

        

    current_time2 = pygame.time.get_ticks()/1
    last_time2 = 0
    if current_time2 > last_time2 + 1:
        y_wall2 = y_wall2 + 0.3
    if y_wall2 >= 800:
        y_wall2 = y_wall2 - 400


        

    
    screen.blit(label, (50, 10))
    pygame.draw.rect(screen, colour, fun_button)
    if not intersect(player, win):
        screen.blit(label2, (400, 750))
        player = pygame.Rect(x, y, 30, 30)
        pygame.draw.rect(screen, (255, 0, 0), win)
        pygame.draw.rect(screen, color, player)
        pygame.draw.rect(screen, (0, 0, 0,), secret_death_key)
        pygame.draw.rect(screen, (255, 165, 0), secret_cheater)
        pygame.draw.rect(screen, (255, 0, 0), b_red)
        pygame.draw.rect(screen, (255, 165, 0), b_orange)
        pygame.draw.rect(screen, (255, 255, 0), b_yellow)
        pygame.draw.rect(screen, (0, 255, 0), b_green)
        pygame.draw.rect(screen, (0, 0, 255), b_blue)
        pygame.draw.rect(screen, (75, 0, 130), b_indago)
        pygame.draw.rect(screen, (180, 0, 180), b_purple)






        
        if b_red2 is False:
            pygame.draw.rect(screen, (255, 0, 0), player)
        if b_orange2 is False:
            pygame.draw.rect(screen, (255, 165, 0), player)
        if b_yellow2 is False:
            pygame.draw.rect(screen, (255, 255, 0), player)
        if b_green2 is False:
            pygame.draw.rect(screen, (0, 255, 0), player)
        if b_blue2 is False:
            pygame.draw.rect(screen, (0, 0, 255), player)
        if b_indago2 is False:
            pygame.draw.rect(screen, (255, 0, 130), player)
        if b_purple2 is False:
            pygame.draw.rect(screen, (180, 0, 180), player)

        
        
        wall_fun = pygame.Rect( x_w, y_w, 200, 5)
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
        wall_14 = pygame.Rect(105, 285, 465, 5)
        wall_15 = pygame.Rect(105, 285, 5, 110)
        wall_16 = pygame.Rect(55, 395, 150, 5)
        wall_17 = pygame.Rect(205, 395, 5, 85)
        wall_18 = pygame.Rect(60, 480, 150, 5)
        wall_19 = pygame.Rect(5, 440, 135, 5)
        wall_20 = pygame.Rect(60, 480, 5, 205)
        wall_21 = pygame.Rect(5, 745, 365, 5)
        wall_22 = pygame.Rect(60, 685, 250, 5)
        wall_23 = pygame.Rect(310, 490, 5, 200)
        wall_24 = pygame.Rect(370, 490, 5, 260)
        wall_25 = pygame.Rect(370, 490, 150, 5)
        wall_26 = pygame.Rect(370, 440, 150, 5)
        wall_27 = pygame.Rect(520, 490, 5, 100)
        wall_28 = pygame.Rect(570, 285, 5, 400)
        wall_29 = pygame.Rect(370, 290, 5, 155)
        wall_30 = pygame.Rect(370, 340, 150, 5)
        wall_31 = pygame.Rect(465, 390, 105, 5)
        wall_death = pygame.Rect(370, 290, 5, 50)
        wall_33 = pygame.Rect(520, 590, 50, 5)
        wall_34 = pygame.Rect(650, 220, 50, 5)
        wall_35 = pygame.Rect(570, 440, 135, 5)
        wall_36 = pygame.Rect(450, 290, 5, 50)
        wall_37 = pygame.Rect(230, 490, 85, 5)
        wall_38 = pygame.Rect(230, 285, 5, 205)
        wall_39 = pygame.Rect(290, 380, 80, 5)
        wall_40 = pygame.Rect(650, 95, 5, 205)
        wall_weird = pygame.Rect(x_wall2, y_wall2, 5, 200)
        
        #wall_2 = pygame.Rect(0, 95, 200, 5)
        #wall_3 = pygame.Rect(245, 95, 250, 5)
        #wall_4 = pygame.Rect(600, 50, 5, 400)
        #wall_5 = pygame.Rect(200, 95, 5, 150)
        #wall_6 = pygame.Rect(245, 95, 5, 150)
        #wall_7 = pygame.Rect(245, 245, 250, 5)
        #wall_8 = pygame.Rect(490, 95, 5, 150)
        #wall_9 = pygame.Rect(105, 245, 100, 5)
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
        pygame.draw.rect(screen, (207, 159, 255), wall_death)
        pygame.draw.rect(screen, (207, 159, 255), wall_33)
        pygame.draw.rect(screen, (207, 159, 255), wall_34)
        pygame.draw.rect(screen, (207, 159, 255), wall_35)
        pygame.draw.rect(screen, (207, 159, 255), wall_36)
        pygame.draw.rect(screen, (207, 159, 255), wall_37)
        pygame.draw.rect(screen, (207, 159, 255), wall_38)
        pygame.draw.rect(screen, (207, 159, 255), wall_39)
        pygame.draw.rect(screen, (207, 159, 255), wall_40)
        pygame.draw.rect(screen, (207, 159, 255), wall_weird)
        
                       
                           
        #pygame.draw.rect(screen, (0, 0, 255), wall_2)                       
        #pygame.draw.rect(screen, (0, 0, 255), wall_3)
        #pygame.draw.rect(screen, (0, 0, 255), wall_4)
        #pygame.draw.rect(screen, (0, 0, 255), wall_5)
        #pygame.draw.rect(screen, (0, 0, 255), wall_6)
        #pygame.draw.rect(screen, (0, 0, 255), wall_7)
        #pygame.draw.rect(screen, (0, 0, 255), wall_8)
        #pygame.draw.rect(screen, (0, 0, 255), wall_9)
       

        #maze
        walls = [
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
            wall_fun,
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
            wall_36,
            wall_37,
            wall_38,
            wall_39,
            wall_40,
            wall_weird]

        secrets = [
            secret_cheater,
            secret_death_key]
         
        
        #mazeDetection
        


        
        for secret in secrets:
            if intersect(player, secret_cheater):
                    label = myfont.render("Cheater... Here is your punishment!", 1, (random_r, random_g, random_b))
                    current_tim = pygame.time.get_ticks()/3000
                    if current_tim > last_time + 3:
                        screen.fill((255, 0, 0))


       
                    
                
               


        
        for wall in walls:
            if intersect(player, wall) and wall_hit:
                x = 30
                y = 60
   
    else:
         label = myfont.render("woohoo", 1, (0, 0, 255))
         color_change = False
    if color_change is True:
        dolor = (0, 0, 0)
    else:
        dolor = (random_r, random_g, random_b)
         


        


         
         
        
        


    pygame.display.update()
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            label = myfont.render(" To Space! ", 1, (10, 255, 190))
            x = 200
            y = 10
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            draw = not draw
            print ('E pressed')

            
       
            
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
        if event.type == pygame.KEYUP and event.key == pygame.K_n:
            wall_hit = not wall_hit
            print ('n pressed') 
        if event.type == pygame.KEYUP and event.key == pygame.K_r:
            color = (255, 0, 0)
            
        if event.type == pygame.KEYUP and event.key == pygame.K_o:
           color = (255, 165, 0)
            
        if event.type == pygame.KEYUP and event.key == pygame.K_y:
            color = (255, 255, 0)
            
        if event.type == pygame.KEYUP and event.key == pygame.K_g:
            color = (0, 255, 0)
            
        if event.type == pygame.KEYUP and event.key == pygame.K_b:
            color = (0, 0, 255)
            
        if event.type == pygame.KEYUP and event.key == pygame.K_i:
            color = (75, 0, 130)
        if event.type == pygame.KEYUP and event.key == pygame.K_p:
           color = (180, 0, 180)






             
        
        if move_up:
            y = y - 5
        if move_down:
            y = y + 5 
        if move_left:
            x = x - 5
        if move_right:
            x = x + 5


        for secret in secrets:
            if intersect(player, secret_death_key):
                    label = myfont.render("Bwahahahah!!!!!", 1, (random_r, random_g, random_b))
                    move_up = True
                    move_down = True
                    move_left = True
                    move_right = True


print ("Hello World")





