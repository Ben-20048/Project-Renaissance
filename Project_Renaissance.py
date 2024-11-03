from operator import index
import pygame, sys, time

from pygame.sprite import collide_rect
#from pygame.locals import *

#pygame initialisation
pygame.init()
#screen dimensions
SCREEN_WIDTH = 1930
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

clock = pygame.time.Clock()

#background image
bg_surface = pygame.image.load('Assets/Nuclear_reactor_meltdown_map_lighton.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

#game variables

'map offset'
move_x = -1000
move_y = -1100

'player speed'
moving_right = -5
moving_left = 5
moving_up = 5
moving_down = -5

'animation values'
speed_down_right = -5
speed_up_left = 5

'character rect'
char_rect = pygame.Rect(SCREEN_WIDTH/2+10,SCREEN_HEIGHT/2+13,35,40)

#wall data/door data. Coordinates of all objects in map
part_door1 = pygame.Rect(914,-565,130,20-0)
part_door4 = pygame.Rect(725,1928,65,20-0)

door2 = pygame.Rect(303,810,20,130-0)
door3 = pygame.Rect(1648,810,20,130-0)
door4 = pygame.Rect(815,1450,20,130-0)
door5 = pygame.Rect(1135,1450,20,130-0)

#hub walls
wall1_h = pygame.Rect(180,140,660,270-0)
wall2_h = pygame.Rect(1140,140,660,270-0)
wall3_h = pygame.Rect(245,1035,335,270-0)
wall4_h = pygame.Rect(1396,1035,335,270-0)
wall5_h = pygame.Rect(1075,1288,350,20-0)
wall8_h = pygame.Rect(243,415,338,320)
wall9_h = pygame.Rect(1393,415,338,320)
wall10_h = pygame.Rect(580,409,260,67-0)
wall11_h = pygame.Rect(1140,410,251,67-0)
wall12_h = pygame.Rect(242,1291,657,20-0)
wall13_h = pygame.Rect(839,200,63,20-0)
wall14_h = pygame.Rect(1070,200,63,20-0)
wall15_h = pygame.Rect(306,734,20,64-0)
wall16_h = pygame.Rect(307,965,20,64-0)
wall17_h = pygame.Rect(1650,734,20,65-0)
wall18_h = pygame.Rect(1650,965,20,64-0)


#level 1 doors
wall13 = pygame.Rect(-269,-118,785,20-0)
wall14 = pygame.Rect(499,-185,20,400-0)
wall15 = pygame.Rect(497,-564,20,275-0)
wall16 = pygame.Rect(-268,-564,20,445-0)
wall17 = pygame.Rect(-269,-566,1170,20-0)
wall18 = pygame.Rect(-13,-548,20,190-0)
wall19 = pygame.Rect(243,-547,20,190-0)
wall20 = pygame.Rect(-250,-372,65,20-0)
wall21 = pygame.Rect(-82, -372,153,20-0)
wall22 = pygame.Rect(174,-372,153,20-0)
wall23 = pygame.Rect(430,-372,65,20-0)
wall24 = pygame.Rect(1477,-372,65,20-0)
wall25 = pygame.Rect(1647, -372,153,20-0)
wall26 = pygame.Rect(1900,-372,153,20-0)
wall27 = pygame.Rect(2160,-372,65,20-0)
wall28 = pygame.Rect(1069,-564,1172,20-0)
wall29 = pygame.Rect(2226,-564,20,460-0)
wall30 = pygame.Rect(1459,-118,782,20-0)
wall31 = pygame.Rect(1459,-544,20,256-0)
wall32 = pygame.Rect(1459,-186,20,386-0)
wall33 = pygame.Rect(1715,-544,20,186-0)
wall34 = pygame.Rect(1970,-544,20,186-0)
wall35 = pygame.Rect(755,-1012,20,443-0)
wall36 = pygame.Rect(755,-1012,464,20-0)
wall37 = pygame.Rect(1202,-1012,20,443-0)
wall38 = pygame.Rect(839,1740,299,20-0)
wall39 = pygame.Rect(1139,1308,20,131-0)

#level3 walls
wall6 = pygame.Rect(2100,524, 80,400-0)
wall7 = pygame.Rect(1842,907,338,20-0)
wall3_l3 = pygame.Rect(1733,1358,1150,20-0)
wall4_l3 = pygame.Rect(1730,394,1152,20-0)
wall5_l3 = pygame.Rect(2866,394,20,1000-0)
wall6_l3 = pygame.Rect(1730,715,127,20-0)
wall7_l3 = pygame.Rect(1730,1035,127,20-0)
wall8_l3 = pygame.Rect(1842,650,20,145-0)
wall9_l3 = pygame.Rect(1842,906,20,210-0)
wall10_l3 = pygame.Rect(1842,523,143,20-0)
wall11_l3 = pygame.Rect(1842,780,143,20-0)
wall12_l3 = pygame.Rect(1842,1098,210,20-0)
wall13_l3 = pygame.Rect(1842,1228,337,20-0)
wall14_l3 = pygame.Rect(1970,412,20,132-0)
wall15_l3 = pygame.Rect(1970,650,20,151-0)
wall16_l3 = pygame.Rect(2034,1033,20,84-0)
wall17_l3 = pygame.Rect(2162,926,20,322-0)
wall18_l3 = pygame.Rect(2290,412,20,831-0)
wall19_l3 = pygame.Rect(2308,1227,190,20-0)
wall20_l3 = pygame.Rect(2418,1098,190,20-0)
wall21_l3 = pygame.Rect(2308,969,190,20-0)
wall22_l3 = pygame.Rect(2418,840,190,20-0)
wall23_l3 = pygame.Rect(2308,711,190,20-0)
wall24_l3 = pygame.Rect(2418,582,190,20-0)
wall25_l3 = pygame.Rect(2610,522,20,721-0)
wall26_l3 = pygame.Rect(2610,907,255,120-0)
wall27_l3 = pygame.Rect(2738,522,20,274-0)
wall28_l3 = pygame.Rect(2738,778,126,20-0)
wall29_l3 = pygame.Rect(2738,1098,126,20-0)
wall30_l3 = pygame.Rect(2629,1227,126,20-0)

#level2 walls
wall1_l2 = pygame.Rect(-910,397,1150,20-0)
wall2_l2 = pygame.Rect(-910,397,20,965-0)
wall3_l2 = pygame.Rect(-910,1352,1147,20-0)
wall4_l2 = pygame.Rect(-782,416,20,790-0)

#level4 walls
wall1_l4 = pygame.Rect(240,1310,20,777-0)
wall2_l4 = pygame.Rect(240,2060,580,20-0)
wall3_l4 = pygame.Rect(820,1605,20,455-0)
wall4_l4 = pygame.Rect(818,1310,20,128-0)
wall5_l4 = pygame.Rect(691,1932,20,125-0)

#level5 walls
wall1_l5 = pygame.Rect(1714,1306,20,1420-0)
wall2_l5 = pygame.Rect(1139,1606,20,1150-0)

#wall lists. A list containing all collidable objects
wall_list = [part_door1, part_door4, door2, door3, door4, door5,
             wall1_h,wall2_h,wall3_h,wall4_h,wall5_h,wall8_h,wall9_h,wall10_h,wall11_h,wall12_h,wall13_h,wall14_h,wall15_h,wall16_h,wall17_h,wall18_h,
             wall13,wall14,wall15,wall16,wall17,wall18,wall19,wall20,wall21,wall22,wall23,wall24,wall25,wall26,wall27,wall28,wall29,wall30,wall31,wall32,wall33,wall34,wall35,wall36,wall37,wall38,wall39,
             wall6,wall7,wall3_l3,wall4_l3,wall5_l3,wall6_l3,wall7_l3,wall8_l3,wall9_l3,wall10_l3,wall11_l3,wall12_l3,wall13_l3,wall14_l3,wall15_l3,wall16_l3,wall17_l3,wall18_l3,wall19_l3,wall20_l3,wall21_l3,wall22_l3,wall23_l3,wall24_l3,wall25_l3,wall26_l3,wall27_l3,wall28_l3,wall29_l3,wall30_l3,
             wall1_l2,wall2_l2,wall3_l2,wall4_l2,
             wall1_l4,wall2_l4,wall3_l4,wall4_l4,wall5_l4,
             wall1_l5,wall2_l5]

#secondary wall list identical to the first. This exists to re-add all the objects to the first wall list upon restart
wall_list2 = [part_door1, part_door4, door2, door3, door4, door5,
             wall1_h,wall2_h,wall3_h,wall4_h,wall5_h,wall8_h,wall9_h,wall10_h,wall11_h,wall12_h,wall13_h,wall14_h,wall15_h,wall16_h,wall17_h,wall18_h,
             wall13,wall14,wall15,wall16,wall17,wall18,wall19,wall20,wall21,wall22,wall23,wall24,wall25,wall26,wall27,wall28,wall29,wall30,wall31,wall32,wall33,wall34,wall35,wall36,wall37,wall38,wall39,
             wall6,wall7,wall3_l3,wall4_l3,wall5_l3,wall6_l3,wall7_l3,wall8_l3,wall9_l3,wall10_l3,wall11_l3,wall12_l3,wall13_l3,wall14_l3,wall15_l3,wall16_l3,wall17_l3,wall18_l3,wall19_l3,wall20_l3,wall21_l3,wall22_l3,wall23_l3,wall24_l3,wall25_l3,wall26_l3,wall27_l3,wall28_l3,wall29_l3,wall30_l3,
             wall1_l2,wall2_l2,wall3_l2,wall4_l2,
             wall1_l4,wall2_l4,wall3_l4,wall4_l4,wall5_l4,
             wall1_l5,wall2_l5]


#key object coordinates
key1 = pygame.Rect(-150,-480,50,50-0)
key2 = pygame.Rect(91,-480,50,50-0)
key3 = pygame.Rect(350,-480,50,50-0)
key4 = pygame.Rect(1560,-480,50,50-0)
key5 = pygame.Rect(1800,-480,50,50-0)
key6 = pygame.Rect(2080,-480,50,50-0)

#Key lists
key_list = [key1,key2,key3,key4,key5,key6]

key_list2 = [key1,key2,key3,key4,key5,key6]

#inventory

def inventory():

    global door_list, part_door1, part_door4, door2, inventory_list #makes these variables global across code. Now when I reference the variables that are in the function in main loop they are recognised

    #inventory list. Stores values of collected objects
    inventory_list = []
    
    #if player collides with a key it is added to inventory. If the correct key is collected then a door is unlocked
    for key in key_list:
        if char_rect.colliderect(key):
            inventory_list.append(key)
            key_list.remove(key)
        if key1 in inventory_list:
            wall_list.pop(0)
            break
        
    #progression code. If a part is collected, the next level is unlocked.
    for parts in part_list:
        if char_rect.colliderect(parts):
            inventory_list.append(parts)
            part_list.remove(parts)
        if part1 in inventory_list:
            wall_list.pop(2)
            break
        if part2 in inventory_list:
            wall_list.pop(1)
            break
        if part3 in inventory_list:
            wall_list.pop(1)
            break
        if part4 in inventory_list:
            wall_list.pop(0)
            break
                    

#when you aquire an item, the corrosponding item is set to true to cross off the item.
check = False
check1 = False
check2 = False
check3 = False
check4 = False
check5 = False

check_dash = pygame.Rect(10,58,270,3-0)
check_dash1 = pygame.Rect(10,88,270,3-0)
check_dash2 = pygame.Rect(10,118,270,3-0)
check_dash3 = pygame.Rect(10,148,270,3-0)
check_dash4 = pygame.Rect(10,178,270,3-0)
check_dash5 = pygame.Rect(10,208,270,3-0)

clipboard_bg = pygame.Rect(0,0,330,268-0)
clipboard_border = pygame.Rect(0,0,300,238-0)

#reactor            
reactor = pygame.Rect(786,632,400,570-0)

#parts

part1 = pygame.Rect(942,-825,50,50-0)
part2 = pygame.Rect(2787,834,50,50-0)
part3 = pygame.Rect(-858,450,50,50-0)
part4 = pygame.Rect(740,1983,50,50-0)
part5 = pygame.Rect(1420,2445,50,50-0)
            
part_list = [part1,part2,part3,part4,part5]

part_list2 = [part1,part2,part3,part4,part5]        

#Water data

collision_start_time = None

water_flow = False

water_machine = pygame.Rect(260,1380,167,650-0)
water_rect = pygame.Rect(815,520,300,300-0)
goal_area = pygame.Rect(810,500,320,20-0)

gravity = 0.3
haswatercoloccur = False

def water(water_rect, gravity):
    pygame.draw.rect(screen,pygame.Color("green"),goal_area)
    water_rect.y += gravity
    collision_start_time = pygame.time.get_ticks()
    #if the water rect is at a certain Y level then it stops moving
    if water_rect.y > 700:
        water_rect.y = 700
    
        has_water_col_occur = False
    if water_rect.colliderect(goal_area):
        has_water_col_occur = True
        #if haswatercoloccur is true then the timer starts
        if haswatercoloccur:
            collision_start_time = pygame.time.get_ticks()

        #if water has collided with goal area and has done so for the set amount of time then door is unlocked
        if water_rect.colliderect(goal_area) and pygame.time.get_ticks() - collision_start_time >= 1000:
            door_list.pop(0)

#nuclear waste
run = False
            
#nuclear waste coordinates
waste0 = pygame.Rect(1150,2634,700, 10-0)            
waste1 = pygame.Rect(10,420,95,403-0)
waste2 = pygame.Rect(-762,415,780,70-0)
waste3 = pygame.Rect(-680,1280,793,92-0)
waste4 = pygame.Rect(-763,417,76,744-0)
waste5 = pygame.Rect(-37,937,149,321-0)
waste6 = pygame.Rect(-362,520,74,606-0)
waste7 = pygame.Rect(-538,578,46,678-0)
waste8 = pygame.Rect(-160,639,62,298-0)
waste9 = pygame.Rect(-295,1074,111,62-0)
waste10 = pygame.Rect(-494,757,43,123-0)
waste11 = pygame.Rect(-400,483,54,150-0)
waste12 = pygame.Rect(-100,935,62,63-0)
waste13 = pygame.Rect(-289,1014,60,58-0)
waste14 = pygame.Rect(-689,482,57,127-0)
waste15 = pygame.Rect(-587,707,53,46-0)
waste16 = pygame.Rect(-692,829,51,43-0)
waste17 = pygame.Rect(-587,964,50,45-0)
waste18 = pygame.Rect(-762,1089,133,99-0)
        
nuc_list = [waste0, waste1,waste2,waste3,waste4,waste5,waste6,waste7,waste8,waste9,waste10,waste11,waste12,waste13,waste14,waste15,waste16,waste17,waste18]

#timer
        
my_time = int(20)

#game over

restart = False

game_state = True

text_font = pygame.font.SysFont("Helvetica", 30) #setting text font

#function that draws text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

#function that handles game reseting
def game_status():

    if game_state == False:
        print("game over")
        screen.fill(pygame.Color("black"))
        draw_text("Game Over", text_font, (255, 255, 255), 900, 150)
        draw_text("Press R to Reload", text_font, (255, 255, 255), 870, 550)
        if keys[pygame.K_r]:
            print("restart")
            restart = True

#collision checking function
def collision_test(char_rect,wall_list):
    collisions = []
    for wall in wall_list:
        if char_rect.colliderect(wall):
            collisions.append(wall)
    return collisions
 
#function that handles movement values
def move(char_rect, wall_list):
    
    global moving_right, moving_left, moving_up, moving_down
 
    collisions = collision_test(char_rect, wall_list)
    
    moving_right = -5
    moving_left = 5
    moving_up = 5
    moving_down = -5

    for wall in collisions:
        
        right = abs(char_rect.right - wall.left)
        left = abs(char_rect.left - wall.right)
        bottom = abs(char_rect.bottom - wall.top)
        top = abs(char_rect.top - wall.bottom)
        minimum = min(left, right, top, bottom)
        if minimum == left:
          print('collision left')
          moving_left = 0
          
        elif minimum == right:
          print('collision right')
          moving_right = 0
          
        elif minimum == top:
          print('collision top')
          moving_up = 0
          
        elif minimum == bottom:
          print('collision bottom')
          moving_down = 0
 
water_col_occur = False

#list of images for character sprite
char_walk = [pygame.image.load("Assets/CharAnim/walk1.png"),
             pygame.image.load("Assets/CharAnim/walk2.png"),
             pygame.image.load("Assets/CharAnim/walk3.png"),
             pygame.image.load("Assets/CharAnim/walk4.png"),
             pygame.image.load("Assets/CharAnim/walk5.png"),
             pygame.image.load("Assets/CharAnim/walk6.png")]

char_idle = [pygame.image.load("Assets/CharAnim/Idle/idle1.png"),
             pygame.image.load("Assets/CharAnim/Idle/idle2.png"),
             pygame.image.load("Assets/CharAnim/Idle/idle3.png"),
             pygame.image.load("Assets/CharAnim/Idle/idle4.png")]

image_index = 0
current_sprite = char_idle[image_index] #sets current sprite to idle by default

ANIMATION = pygame.USEREVENT

pygame.time.set_timer(ANIMATION, 100) #animation clock

color = pygame.Color("yellow")

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            #mouse click position for drawing walls
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            print(move_x+1000)
            print(move_y+1100)

            #animation events
        if event.type == ANIMATION:
            if moving_right == speed_down_right:
                if image_index < len(char_walk)-1:
                    image_index += 1 #cycles through image index
                else:
                    image_index = 0 #resets image index

            elif moving_left == speed_up_left:
                if image_index < len(char_walk)-1:
                    image_index += 1
                else:
                    image_index = 0
            
            elif moving_down == speed_down_right:
                if image_index < len(char_walk)-1:
                    image_index += 1
                else:
                    image_index = 0

            elif moving_up == speed_up_left:
                if image_index < len(char_walk)-1:
                    image_index += 1
                else:
                    image_index = 0

            if (keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]) == False:
                if image_index <= len(char_idle)-1:
                    current_sprite = char_idle[image_index]
                    image_index += 1
                else:
                    image_index = 0
            else:
                print("Error: char_idle list is empty")
        
        if event.type == pygame.KEYDOWN and char_rect.colliderect(water_machine):
            if event.key == pygame.K_SPACE:
                water_rect.y -= 25

    if char_rect.colliderect:
        inventory() #everytime a collision occurs the inventory function is ran

    keys = pygame.key.get_pressed()

    #movement
    if keys[pygame.K_d] and game_state == True:
        screen.fill(pygame.Color("black")) #fills previously blitted background with black, to save on performance
        screen.blit(bg_surface,(move_x,move_y)) #blits the background surface on screen and moves it to the offset of move_x and move_y
        move_x += moving_right+2 #the offset values for the map have the moving value added to them to provide illusion of moving
        current_sprite = char_walk[image_index] #changes current sprite to the walk cycle
        water_machine.x += moving_right+2
        reactor.x += moving_right+2
        for wall in wall_list:
            wall.x += moving_right+2
        for key in key_list:
            key.x += moving_right+2
        for parts in part_list:
            parts.x += moving_right+2
        for waste in nuc_list:
            waste.x += moving_right+2
                
    if keys[pygame.K_a] and game_state == True:
        screen.fill(pygame.Color("black"))
        screen.blit(bg_surface,(move_x+6,move_y))
        move_x += moving_left-2
        current_sprite = pygame.transform.flip(char_walk[image_index], True, False)
        water_machine.x += moving_left-2
        reactor.x += moving_left-2
        for wall in wall_list:
            wall.x += moving_left-2
        for key in key_list:
            key.x += moving_left-2
        for parts in part_list:
            parts.x += moving_left-2
        for waste in nuc_list:
            waste.x += moving_left-2
        
    if keys[pygame.K_w] and game_state == True:
        screen.fill(pygame.Color("black"))
        screen.blit(bg_surface,(move_x+3,move_y+3))
        move_y += moving_up-2
        current_sprite = char_walk[image_index]
        water_machine.y += moving_up-2
        reactor.y += moving_up-2
        for wall in wall_list:
            wall.y += moving_up-2
        for key in key_list:
            key.y += moving_up-2
        for parts in part_list:
            parts.y += moving_up-2
        for waste in nuc_list:
            waste.y += moving_up-2
        
    if keys[pygame.K_s] and game_state == True:
        screen.fill(pygame.Color("black"))
        screen.blit(bg_surface,(move_x+3,move_y-3))
        move_y += moving_down+2
        current_sprite = pygame.transform.flip(char_walk[image_index], True, False)
        water_machine.y += moving_down+2
        reactor.y += moving_down+2
        for wall in wall_list:
            wall.y += moving_down+2
        for key in key_list:
            key.y += moving_down+2
        for parts in part_list:
            parts.y += moving_down+2
        for waste in nuc_list:
            waste.y += moving_down+2

    #if no keys are being pressed then this continues to blit the background
    if (keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]) == False:
        screen.fill(pygame.Color("black"))
        screen.blit(bg_surface,(move_x+3,move_y))
    
    #for x in range(my_time,0,-1):
        #seconds = x % 60
        #minutes = int(x/60) % 60
        #draw_text(f"{minutes:02}:{seconds:02}", text_font, (255, 255, 255), 800, 150)
    
    for wall in wall_list:
        wall = move(char_rect,wall_list)

    #for wall in wall_list:
       # pygame.draw.rect(screen, color, wall)
        
    'rect drawing'

    #pygame.draw.rect(screen,pygame.Color("purple"),rand_rect) 
    scaled_c_sprite = pygame.transform.scale_by(current_sprite, 3)
    screen.blit(scaled_c_sprite, (SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
    #pygame.draw.rect(screen,pygame.Color("yellow"),wall)
    #pygame.draw.rect(screen,pygame.Color("blue"),char_rect)
    #pygame.draw.rect(screen,pygame.Color("pink"),water_machine)
    for key in key_list:
        pygame.draw.rect(screen,pygame.Color("red"),key)
    for parts in part_list:
        pygame.draw.rect(screen,pygame.Color("green"),parts)
    #for doors in door_list:
        #pygame.draw.rect(screen,pygame.Color("white"),doors)
    #for waste in nuc_list:
        #pygame.draw.rect(screen,pygame.Color("orange"),waste)
    #pygame.draw.rect(screen,pygame.Color("purple"),reactor)
            
    if char_rect.colliderect(water_machine):
        water_col_occur = True
    else:
        water_col_occur = False
        
        
    if water_col_occur == True:
        water(water_rect,gravity)
        pygame.draw.rect(screen,pygame.Color("blue"),water_rect)
        draw_text("Press Space to Adjust Water Flow to Green Area", text_font, (255, 255, 255), 800, 150)
        #pygame.draw.rect(screen,water_rect)
        if water_flow == True:
            draw_text("Water Flow Corrected! Collect Part", text_font, (255, 255, 255), 800, 200)
        
    if water_rect.colliderect(goal_area):
        # Start timing if collision just began
        if collision_start_time is None:
            collision_start_time = pygame.time.get_ticks()
        # Check if the collision has lasted for 5 seconds
        elif pygame.time.get_ticks() - collision_start_time >= 5000:
            wall_list.pop(0)
            water_flow = True
            # Reset collision start time if you want to print only once
            collision_start_time = None
    else:
        # Reset timer if no collision
        collision_start_time = None
        
        
    if part5 in inventory_list:
        run = True
    
    if run == True:
        waste0.y -= 2.1 #speed of acid chasing you in level 5
        waste0.height += 2.1 #speed of acid chasing you in level 5
        draw_text("RUN!!!", text_font, (255, 255, 255), 900, 150)
        pygame.draw.rect(screen,pygame.Color("green"),waste0)

    pygame.draw.rect(screen,pygame.Color("black"),clipboard_bg)
    pygame.draw.rect(screen,pygame.Color("grey"),clipboard_border)

    draw_text("character sprite by DANI MACCARI", text_font, (255, 255, 255), 1450, 970)

    draw_text("Checklist:", text_font, (255, 255, 255), 10, 10)
    draw_text("key to part1 room", text_font, (255, 255, 255), 10, 40)
    draw_text("part1", text_font, (255, 255, 255), 10, 70)
    draw_text("part2", text_font, (255, 255, 255), 10, 100)
    draw_text("part3", text_font, (255, 255, 255), 10, 130)
    draw_text("part4", text_font, (255, 255, 255), 10, 160)
    draw_text("part5", text_font, (255, 255, 255), 10, 190)
    
    #checklist. Checks if certain things are in inventory and marks them off list
    if key1 in inventory_list: #checks if key is in inventory
        check = True
    if check == True:
        pygame.draw.rect(screen,pygame.Color("white"),check_dash) #draws dash over words on checklist to communicate to player they have collected item
        
    if part1 in inventory_list:
        check1 = True
    if check1 == True:
        pygame.draw.rect(screen,pygame.Color("white"),check_dash1)
        
    if part2 in inventory_list:
        check2 = True
    if check2 == True:
        pygame.draw.rect(screen,pygame.Color("white"),check_dash2)
        
    if part3 in inventory_list:
        check3 = True
    if check3 == True:
        pygame.draw.rect(screen,pygame.Color("white"),check_dash3)
        
    if part4 in inventory_list:
        check4 = True
    if check4 == True:
        pygame.draw.rect(screen,pygame.Color("white"),check_dash4)
        
    if part5 in inventory_list:
        check5 = True
    if check5 == True:
        pygame.draw.rect(screen,pygame.Color("white"),check_dash5)

    if len(part_list) == 0 and char_rect.colliderect(reactor):
        screen.fill(pygame.Color("black"))
        draw_text("You win!", text_font, (255, 255, 255), 800, 150)
        print("you win")

        #if you collide with waste then the game enters a state where the player is dead until restart
    for waste in nuc_list:
        if char_rect.colliderect(waste):
            game_state = False
            game_status()

    #replaces everything upon restart
    if keys[pygame.K_r] and game_state == False:
        game_state = True
        
        #check = False
        #check1 = False
        #check2 = False
        #check3 = False
        #check4 = False
        #check5 = False
        
        water_flow = False
        
        Run = False

        #wall_list.clear()
        #wall_list += wall_list2
        
        #inventory_list.clear()
        
        #key_list.clear()
        #key_list += key_list2

        #part_list.clear()
        #part_list += part_list2
        
        part_door1.x, part_door1.y = 914, -565
        part_door4.x, part_door4.y = 725, 1928

        door2.x, door2.y = 303, 810
        door3.x, door3.y = 1648, 810
        door4.x, door4.y = 815, 1450
        door5.x, door5.y = 1135, 1450

        wall1_h.x, wall1_h.y = 180, 140
        wall2_h.x, wall2_h.y = 1140, 140
        wall3_h.x, wall3_h.y = 245, 1035
        wall4_h.x, wall4_h.y = 1396, 1035
        wall5_h.x, wall5_h.y = 1075, 1288
        wall8_h.x, wall8_h.y = 243, 415
        wall9_h.x, wall9_h.y = 1393, 415
        wall10_h.x, wall10_h.y = 580, 409
        wall11_h.x, wall11_h.y = 1140, 410
        wall12_h.x, wall12_h.y = 242, 1291
        wall13_h.x, wall13_h.y = 839,200
        wall14_h.x, wall14_h.y = 1070,200
        wall15_h.x, wall15_h.y = 306,734
        wall16_h.x, wall16_h.y = 307,965
        wall17_h.x, wall17_h.y = 1650,734
        wall18_h.x, wall18_h.y = 1650,965

        wall13.x, wall13.y = -269, -118
        wall14.x, wall14.y = 499, -185
        wall15.x, wall15.y = 497, -564
        wall16.x, wall16.y = -268, -564
        wall17.x, wall17.y = -269, -566
        wall18.x, wall18.y = -13, -548
        wall19.x, wall19.y = 243, -547
        wall20.x, wall20.y = -250, -372
        wall21.x, wall21.y = -82, -372
        wall22.x, wall22.y = 174, -372
        wall23.x, wall23.y = 430, -372
        wall24.x, wall24.y = 1477, -372
        wall25.x, wall25.y = 1647, -372
        wall26.x, wall26.y = 1900, -372
        wall27.x, wall27.y = 2160, -372
        wall28.x, wall28.y = 1069, -564
        wall29.x, wall29.y = 2226, -564
        wall30.x, wall30.y = 1459, -118
        wall31.x, wall31.y = 1459, -544
        wall32.x, wall32.y = 1459, -186
        wall33.x, wall33.y = 1715, -544
        wall34.x, wall34.y = 1970, -544
        wall35.x, wall35.y = 755, -1012
        wall36.x, wall36.y = 755, -1012
        wall37.x, wall37.y = 1202, -1012
        wall38.x, wall38.y = 839, 1740
        wall39.x, wall39.y = 1139, 1308

        wall6.x, wall6.y = 2100, 524
        wall7.x, wall7.y = 1842, 907
        wall3_l3.x, wall3_l3.y = 1733, 1358
        wall4_l3.x, wall4_l3.y = 1730, 394
        wall5_l3.x, wall5_l3.y = 2866, 394
        wall6_l3.x, wall6_l3.y = 1730, 715
        wall7_l3.x, wall7_l3.y = 1730, 1035
        wall8_l3.x, wall8_l3.y = 1842, 650
        wall9_l3.x, wall9_l3.y = 1842, 906
        wall10_l3.x, wall10_l3.y = 1842, 523
        wall11_l3.x, wall11_l3.y = 1842, 780
        wall12_l3.x, wall12_l3.y = 1842, 1098
        wall13_l3.x, wall13_l3.y = 1842, 1228
        wall14_l3.x, wall14_l3.y = 1970, 412
        wall15_l3.x, wall15_l3.y = 1970, 650
        wall16_l3.x, wall16_l3.y = 2034, 1033
        wall17_l3.x, wall17_l3.y = 2162, 926
        wall18_l3.x, wall18_l3.y = 2290, 412
        wall19_l3.x, wall19_l3.y = 2308, 1227
        wall20_l3.x, wall20_l3.y = 2418, 1098
        wall21_l3.x, wall21_l3.y = 2308, 969
        wall22_l3.x, wall22_l3.y = 2418, 840
        wall23_l3.x, wall23_l3.y = 2308, 711
        wall24_l3.x, wall24_l3.y = 2418, 582
        wall25_l3.x, wall25_l3.y = 2610, 522
        wall26_l3.x, wall26_l3.y = 2610, 907
        wall27_l3.x, wall27_l3.y = 2738, 522
        wall28_l3.x, wall28_l3.y = 2738, 778
        wall29_l3.x, wall29_l3.y = 2738, 1098
        wall30_l3.x, wall30_l3.y = 2629, 1227

        wall1_l2.x, wall1_l2.y = -910, 397
        wall2_l2.x, wall2_l2.y = -910, 397
        wall3_l2.x, wall3_l2.y = -910, 1352
        wall4_l2.x, wall4_l2.y = -782, 416

        wall1_l4.x, wall1_l4.y = 240, 1310
        wall2_l4.x, wall2_l4.y = 240, 2060
        wall3_l4.x, wall3_l4.y = 820, 1605
        wall4_l4.x, wall4_l4.y = 818, 1310
        wall5_l4.x, wall5_l4.y = 691, 1932

        wall1_l5.x, wall1_l5.y = 1714, 1306
        wall2_l5.x, wall2_l5.y = 1139, 1606

        key1.x, key1.y = -150, -480
        key2.x, key2.y = 91, -480
        key3.x, key3.y = 350, -480
        key4.x, key4.y = 1560, -480
        key5.x, key5.y = 1800, -480
        key6.x, key6.y = 2080, -480

        check_dash.x, check_dash.y = 10, 58
        check_dash1.x, check_dash1.y = 10, 88
        check_dash2.x, check_dash2.y = 10, 118
        check_dash3.x, check_dash3.y = 10, 148
        check_dash4.x, check_dash4.y = 10, 178
        check_dash5.x, check_dash5.y = 10, 208

        part1.x, part1.y = 942, -825
        part2.x, part2.y = 2787, 834
        part3.x, part3.y = -858, 450
        part4.x, part4.y = 740, 1983
        part5.x, part5.y = 1420, 2445

        water_machine.x, water_machine.y = 260, 1380
        water_rect.x, water_rect.y = 815, 520
        goal_area.x, goal_area.y = 810, 500

        waste0.x, waste0.y = 1150, 2634
        waste1.x, waste1.y = 10, 420
        waste2.x, waste2.y = -762, 415
        waste3.x, waste3.y = -680, 1258
        waste4.x, waste4.y = -763, 417
        waste5.x, waste5.y = -37, 937
        waste6.x, waste6.y = -362, 520
        waste7.x, waste7.y = -538, 578
        waste8.x, waste8.y = -160, 639
        waste9.x, waste9.y = -295, 1074
        waste10.x, waste10.y = -494, 757
        waste11.x, waste11.y = -417, 483
        waste12.x, waste12.y = -100, 935
        waste13.x, waste13.y = -289, 1014
        waste14.x, waste14.y = -689, 482
        waste15.x, waste15.y = -587, 707
        waste16.x, waste16.y = -692, 829
        waste17.x, waste17.y = -587, 964
        waste18.x, waste18.y = -762, 1089

        reactor.x, reactor.y = 786, 682

    if game_state == False:
        
        move_x = -1000
        move_y = -1100

    pygame.display.update()
    clock.tick(120)