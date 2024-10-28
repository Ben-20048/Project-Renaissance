from operator import index
import pygame, sys
#from pygame.locals import *


pygame.init()
SCREEN_WIDTH = 1930
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('Assets/Nuclear_reactor_meltdown_map_lighton.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)
#bg_surface = pygame.transform.scale_by(bg_surface, 0.333)

#game variables
move_x = -1000
move_y = -1100
move_x_pr = move_x
move_y_pr = move_y


moving_right = -5
moving_left = 5
moving_up = 5
moving_down = -5

speed_down_right = -5
speed_up_left = 5

rand_rect = pygame.Rect(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,50,50)

char_rect = pygame.Rect(SCREEN_WIDTH/2+5,SCREEN_HEIGHT/2+7,50,50)

#wall data
wall1 = pygame.Rect(180,140,660,270-0)
wall2 = pygame.Rect(1140,140,660,270-0)
wall3 = pygame.Rect(245,1035,335,270-0)
wall4 = pygame.Rect(1396,1035,335,270-0)
wall5 = pygame.Rect(1075,1288,350,20-0)
wall6 = pygame.Rect(2100,524, 80,400-0)
wall7 = pygame.Rect(1842,907,250,20-0)

wall_list = [wall1, wall2, wall3, wall4, wall5, wall6, wall7]

wall_list2 = [wall1, wall2, wall3, wall4, wall5, wall6, wall7]


#key
key1 = pygame.Rect(-150,-480,50,50-0)
key2 = pygame.Rect(91,-480,50,50-0)
key3 = pygame.Rect(350,-480,50,50-0)
key4 = pygame.Rect(1560,-480,50,50-0)
key5 = pygame.Rect(1800,-480,50,50-0)
key6 = pygame.Rect(2080,-480,50,50-0)

key_list = [key1,key2,key3,key4,key5,key6]

#doors
part_door1 = pygame.Rect(914,-565,65,20-0)
part_door4 = pygame.Rect(725,1928,65,20-0)

door3 = pygame.Rect(303,810,20,65-0)
door2 = pygame.Rect(1648,810,20,65-0)
door4 = pygame.Rect(815,1450,20,65-0)
door5 = pygame.Rect(1135,1450,20,65-0)

door_list = [part_door1, part_door4, door2, door3, door4, door5]

empty_list = []

#inventory

def inventory():
    
    global door_list, part_door1, part_door4, door2

    inventory_list = []
    for key in key_list:
        if char_rect.colliderect(key):
            inventory_list.append(key)
            key_list.remove(key)
        if key1 in inventory_list:
            door_list.pop(0)
            break
    for parts in part_list:
        if char_rect.colliderect(parts):
            inventory_list.append(parts)
            part_list.remove(parts)
        if part1 in inventory_list:
            door_list.pop(2)
            break
        if part2 in inventory_list:
            door_list.pop(2)
            break
        if part3 in inventory_list:
            door_list.pop(2)
            break
        if part4 in inventory_list:
            door_list.pop(2)
            break
                    
#maybe try and use true/false statments in door stuff?

#reactor            


#parts

part1 = pygame.Rect(942,-825,50,50-0)
part2 = pygame.Rect(2787,834,50,50-0)
part3 = pygame.Rect(-858,450,50,50-0)
part4 = pygame.Rect(740,1983,50,50-0)
part5 = pygame.Rect(1420,2445,50,50-0)
            
part_list = [part1,part2,part3,part4,part5]        
    

#Water

def water():
    water = pygame.rect(815,500,50,50,50-0)

#nuclear waste
waste1 = pygame.Rect(4,420,95,403-0)
        
nuc_list = [waste1]

#timer
        

#game over

restart = False

game_state = True

text_font = pygame.font.SysFont("Helvetica", 30)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def game_status():
    
    wall1 = pygame.Rect(180,140,660,270-0)
    wall2 = pygame.Rect(1140,140,660,270-0)
    wall3 = pygame.Rect(245,1035,335,270-0)
    wall4 = pygame.Rect(1396,1035,335,270-0)
    wall5 = pygame.Rect(1075,1288,350,20-0)
    wall6 = pygame.Rect(2100,524, 80,400-0)
    wall7 = pygame.Rect(1842,907,250,20-0)

    wall_list = [wall1, wall2, wall3, wall4, wall5, wall6, wall7]

    wall_list2 = [wall1, wall2, wall3, wall4, wall5, wall6, wall7]

    #if game_state == True:
        #print("running")
    if game_state == False:
        print("game over")
        screen.fill(pygame.Color("black"))
        draw_text("Game Over", text_font, (255, 255, 255), 900, 150)
        if keys[pygame.K_r]:
            print("restart")
            restart = True
            #move_x = -1000
            #move_y = -1100
            print(wall_list)
            #wall_list.clear()
            #wall_list = wall_list2
            #wall_list.append(wall_list2)
            print(wall_list)
            for key in key_list:
                key.x = move_x + 1000
                key.y = move_y + 1100
            for parts in part_list:
                parts.x = move_x + 1000
                parts.y = move_y + 1100
            for doors in door_list:
                doors.x = move_x + 1000
                doors.y = move_y + 1100
            for waste in nuc_list:
                waste.x = move_x + 1000
                waste.y = move_y + 1100


def collision_test(char_rect,wall_list):
    collisions = []
    for wall in wall_list:
        if char_rect.colliderect(wall):
            collisions.append(wall)
    return collisions
 
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
 
    #for key in key_list:
        #if keys[pygame.K_d]:
            #key.x += moving_right

        #if keys[pygame.K_a]:
            #key.x += moving_left

        #if keys[pygame.K_w]:
            #key.y += moving_up

        #if keys[pygame.K_s]:
            #key.y += moving_down

#animation stuff
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
current_sprite = char_idle[image_index]

ANIMATION = pygame.USEREVENT

pygame.time.set_timer(ANIMATION, 100)

#when taking coords from image editor take away 408 from X value and 480 from Y to get game coords

color = pygame.Color("yellow")


#collision_detected = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            print(move_x+1000)
            print(move_y+1100)
            #print("base run")
            #print(door_list)

        if event.type == ANIMATION:
            if moving_right == speed_down_right:
                if image_index < len(char_walk)-1:
                    image_index += 1
                    #current_sprite = char_walk[image_index]
                else:
                    image_index = 0

            elif moving_left == speed_up_left:
                if image_index < len(char_walk)-1:
                    image_index += 1
                    #current_sprite = pygame.transform.flip(image_sprite[image_index], True, False)
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

                #if event.type == pygame.KEYUP:
                    #if event.key == pygame.K_d or pygame.K_a or pygame.K_w or pygame.K_s:
                        ##image_index += 1

                #keys = pygame.key.get_pressed()

                #if (keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]) == False:
                #print("no keys")
                #for i in range(len(char_idle)):
                    #if i == 1:
                        #current_sprite = char_idle[image_index]
                        #print("anim rest")
                        #if image_index < len(char_idle)-1:
                           # print("rest cycle")
                            #current_sprite = char_idle[image_index]
                            #image_index += 1
                        #else:
                            #image_index = 0
                            
            if (keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]) == False:
                #print("no keys")
    
                # Safeguard: Ensure `image_index` stays within bounds
                #if len(char_idle) >= 0:
                    #current_sprite = char_idle[image_index]
                    #print("anim rest")
        
                if image_index <= len(char_idle)-1:
                    current_sprite = char_idle[image_index]
                    #print("rest cycle")
                    image_index += 1
                    #print(image_index)
                else:
                    #print("reset idle")
                    image_index = 0
            else:
                print("Error: char_idle list is empty")

    if char_rect.colliderect:
        inventory()

    keys = pygame.key.get_pressed()

    #print(keys[pygame.K_d])
    #print(keys[pygame.K_w])
    #print(keys[pygame.K_s])
    #print(keys[pygame.K_a])

    if keys[pygame.K_d] and game_state == True:
        screen.fill(pygame.Color("black"))
        screen.blit(bg_surface,(move_x,move_y))
        move_x += moving_right+2
        rand_rect.x += moving_right+2
        current_sprite = char_walk[image_index]
        for wall in wall_list:
            wall.x += moving_right+2
        for key in key_list:
            key.x += moving_right+2
        for parts in part_list:
            parts.x += moving_right+2
        for doors in door_list:
            doors.x += moving_right+2
        for waste in nuc_list:
            waste.x += moving_right+2
                
    if keys[pygame.K_a] and game_state == True:
        screen.fill(pygame.Color("black"))
        screen.blit(bg_surface,(move_x+6,move_y))
        move_x += moving_left-2
        rand_rect.x += moving_left-2
        current_sprite = pygame.transform.flip(char_walk[image_index], True, False)
        for wall in wall_list:
            wall.x += moving_left-2
        for key in key_list:
            key.x += moving_left-2
        for parts in part_list:
            parts.x += moving_left-2
        for doors in door_list:
            doors.x += moving_left-2
        for waste in nuc_list:
            waste.x += moving_left-2
        
    if keys[pygame.K_w] and game_state == True:
        screen.fill(pygame.Color("black"))
        screen.blit(bg_surface,(move_x+3,move_y+3))
        move_y += moving_up-2
        rand_rect.y += moving_up-2
        current_sprite = char_walk[image_index]
        for wall in wall_list:
            wall.y += moving_up-2
        for key in key_list:
            key.y += moving_up-2
        for parts in part_list:
            parts.y += moving_up-2
        for doors in door_list:
            doors.y += moving_up-2
        for waste in nuc_list:
            waste.y += moving_up-2
        
    if keys[pygame.K_s] and game_state == True:
        screen.fill(pygame.Color("black"))
        screen.blit(bg_surface,(move_x+3,move_y-3))
        move_y += moving_down+2
        rand_rect.y += moving_down+2
        current_sprite = pygame.transform.flip(char_walk[image_index], True, False)
        for wall in wall_list:
            wall.y += moving_down+2
        for key in key_list:
            key.y += moving_down+2
        for parts in part_list:
            parts.y += moving_down+2
        for doors in door_list:
            doors.y += moving_down+2
        for waste in nuc_list:
            waste.y += moving_down+2


    #if (keys[pygame.K_w] and keys[pygame.K_s] and keys[pygame.K_a] and keys[pygame.K_d]) == False:
        #print("no keys")
        #current_sprite = char_idle[image_index]
            
    #screen.Surface(char_idle,(move_x,move_y))
    
    for wall in wall_list:
        wall = move(char_rect,wall_list)

    for wall in wall_list:
        pygame.draw.rect(screen, color, wall)
        
    pygame.draw.rect(screen,pygame.Color("purple"),rand_rect) 
    scaled_c_sprite = pygame.transform.scale_by(current_sprite, 3)
    screen.blit(scaled_c_sprite, (SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
    #pygame.draw.rect(screen,pygame.Color("yellow"),wall)
    #pygame.draw.rect(screen,pygame.Color("blue"),char_rect)
    for key in key_list:
        pygame.draw.rect(screen,pygame.Color("red"),key)
    for parts in part_list:
        pygame.draw.rect(screen,pygame.Color("green"),parts)
    for doors in door_list:
        pygame.draw.rect(screen,pygame.Color("white"),doors)
    for waste in nuc_list:
        pygame.draw.rect(screen,pygame.Color("orange"),waste)
        
    if keys[pygame.K_p] or char_rect.colliderect(waste1):
        game_state = False
        game_status()
        
    print(restart)

    if keys[pygame.K_r] and game_state == False:
        game_state = True

    if game_state == False:
        wall_list.clear()
        print(wall_list)
        wall_list = wall_list2
        print(wall_list)
            
    pygame.display.update()
    clock.tick(120)