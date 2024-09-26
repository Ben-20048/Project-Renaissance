from operator import index
import pygame, sys
#from pygame.locals import *


pygame.init()
SCREEN_WIDTH = 1930
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('Assets/Digital_assessment_map_no-light.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)
#bg_surface = pygame.transform.scale_by(bg_surface, 0.333)

#game variables
move_x = -130
move_y = -4000

moving_right = -5
moving_left = 5
moving_up = 5
moving_down = -5

speed_down_right = -5
speed_up_left = 5

rand_rect = pygame.Rect(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,50,50)

char_rect = pygame.Rect(SCREEN_WIDTH/2-50,SCREEN_HEIGHT/2-50,100,100)

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

#wall data
wall1 = pygame.Rect(1591,380,620,10-0)
wall2 = pygame.Rect(1305,695,1810,450-235)
wall3 = pygame.Rect(1591, 100, 620, 5)

wall_list = [wall1, wall2, wall3]

color = pygame.Color("yellow")


collision_detected = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            print("base run")
    
        if event.type == ANIMATION:
            print ("anim")
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
                    #current_sprite = pygame.transform.flip(image_sprite[image_index], True, False)
                else:
                    image_index = 0

            elif moving_up == speed_up_left:
                if image_index < len(char_walk)-1:
                    image_index += 1
                    #current_sprite = char_walk[image_index]
                else:
                    image_index = 0

                #if event.type == pygame.KEYUP:
                    #if event.key == pygame.K_d or pygame.K_a or pygame.K_w or pygame.K_s:
                        ##image_index += 1


            elif (keys[pygame.K_w] and keys[pygame.K_s] and keys[pygame.K_a] and keys[pygame.K_d]) == False:
                print("no keys")
                current_sprite = char_idle[image_index]
                print("anim rest")
                if image_index < len(char_idle)-1:
                    print("rest cycle")
                    current_sprite = char_idle[image_index]
                    image_index += 1
                else:
                    image_index = 0

    keys = pygame.key.get_pressed()

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
    
    collision_detected = False

    for wall in wall_list:
        if char_rect.colliderect(wall):
            
            collision_detected = True
            
            if char_rect.right - wall.left <= 20:
                moving_right = 0
                if char_rect.right - wall.left <= 10:
                    moving_right = -5

            elif char_rect.left - wall.right >= -20:
                moving_left = 0
                if char_rect.left - wall.right >= -10:
                    moving_left = 5

            elif char_rect.bottom - wall.top <= 20:
                moving_down = 0
                if char_rect.bottom - wall.top <= 10:
                    moving_down = -5

            elif char_rect.top - wall.bottom >= -20:
                moving_up = 0
                if char_rect.top - wall.bottom >= -10:
                    moving_up = 5
                    
            break
        
        else:
            moving_right = -5
            moving_left = 5
            moving_up = 5
            moving_down = -5            

    for wall in wall_list:
        pygame.draw.rect(screen, color, wall)
            
        
    pygame.draw.rect(screen,pygame.Color("purple"),rand_rect) 
    scaled_c_sprite = pygame.transform.scale_by(current_sprite, 3)
    screen.blit(scaled_c_sprite, (SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
    #pygame.draw.rect(screen,pygame.Color("yellow"),wall1)
    #pygame.draw.rect(screen,pygame.Color("blue"),char_rect)
    pygame.display.update()
    clock.tick(120)