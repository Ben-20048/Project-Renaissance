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

    keys = pygame.key.get_pressed()

    #print(keys[pygame.K_d])
    #print(keys[pygame.K_w])
    #print(keys[pygame.K_s])
    #print(keys[pygame.K_a])

    if keys[pygame.K_d]:
        screen.fill(pygame.Color("black"))
        screen.blit(bg_surface,(move_x,move_y))
        move_x += moving_right+2
        rand_rect.x += moving_right+2
        current_sprite = char_walk[image_index]
        for wall in wall_list:
            wall.x += moving_right+2
                
    if keys[pygame.K_a]:
        screen.fill(pygame.Color("black"))
        screen.blit(bg_surface,(move_x + 10,move_y))
        move_x += moving_left-2
        rand_rect.x += moving_left-2
        current_sprite = pygame.transform.flip(char_walk[image_index], True, False)
        for wall in wall_list:
            wall.x += moving_left-2
        
    if keys[pygame.K_w]:
        screen.fill(pygame.Color("black"))
        screen.blit(bg_surface,(move_x + 5,move_y + 5))
        move_y += moving_up-2
        rand_rect.y += moving_up-2
        current_sprite = char_walk[image_index]
        for wall in wall_list:
            wall.y += moving_up-2
        
    if keys[pygame.K_s]:
        screen.fill(pygame.Color("black"))
        screen.blit(bg_surface,(move_x + 5,move_y - 5))
        move_y += moving_down+2
        rand_rect.y += moving_down+2
        current_sprite = pygame.transform.flip(char_walk[image_index], True, False)
        for wall in wall_list:
            wall.y += moving_down+2
            
    #if (keys[pygame.K_w] and keys[pygame.K_s] and keys[pygame.K_a] and keys[pygame.K_d]) == False:
        #print("no keys")
        #current_sprite = char_idle[image_index]
            
    #screen.Surface(char_idle,(move_x,move_y))
    
    for wall in wall_list:
        wall = move(char_rect,wall_list)

                #moving_right = -5
                #moving_left = 5
                #moving_up = 5
                #moving_down = -5            

    for wall in wall_list:
        pygame.draw.rect(screen, color, wall)
            
        
    pygame.draw.rect(screen,pygame.Color("purple"),rand_rect) 
    scaled_c_sprite = pygame.transform.scale_by(current_sprite, 3)
    screen.blit(scaled_c_sprite, (SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
    #pygame.draw.rect(screen,pygame.Color("yellow"),wall)
    #pygame.draw.rect(screen,pygame.Color("blue"),char_rect)
    pygame.display.update()
    clock.tick(120)