from operator import index
import pygame, sys


pygame.init()
SCREEN_WIDTH = 2432/3
SCREEN_HEIGHT = 2528/3
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('Assets/Digital_assessment_map_no-light.png').convert()
#bg_surface = pygame.transform.scale2x(bg_surface)
#bg_surface = pygame.transform.scale_by(bg_surface, 0.333)

#game variables
move_x = -130
move_y = -1840

moving_right = -5
moving_left = 5
moving_up = 5
moving_down = -5

rand_rect = pygame.Rect(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,50,50)

char_rect = pygame.Rect(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,50,50)

#wall data
wall2 = pygame.Rect(591,508,1000,370-235)
wall1 = pygame.Rect(591,380,620,10-0)
wall3 = pygame.Rect(591, 100, 620, 5)

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
                      
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        screen.fill(pygame.Color("black"))
        screen.blit(bg_surface,(move_x,move_y))
        move_x += moving_right
        rand_rect.x += moving_right
        for wall in wall_list:
            wall.x += moving_right
                

    if keys[pygame.K_a]:
        screen.fill(pygame.Color("black"))
        screen.blit(bg_surface,(move_x + 10,move_y))
        move_x += moving_left
        rand_rect.x += moving_left
        for wall in wall_list:
            wall.x += moving_left
        
    if keys[pygame.K_w]:
        screen.fill(pygame.Color("black"))
        screen.blit(bg_surface,(move_x + 5,move_y + 5))
        move_y += moving_up
        rand_rect.y += moving_up
        for wall in wall_list:
            wall.y += moving_up
        
    if keys[pygame.K_s]:
        screen.fill(pygame.Color("black"))
        screen.blit(bg_surface,(move_x + 5,move_y - 5))
        move_y += moving_down
        rand_rect.y += moving_down
        for wall in wall_list:
            wall.y += moving_down
            

    for wall in wall_list:
        
        if char_rect.colliderect(wall):
            collision_detected = True
            print ("collision with " + str(wall))

            if char_rect.right - wall.left <=20:
                print("collision right")
                print (char_rect.right)
                print (wall.left)
                print(char_rect.right - wall.left)
                moving_right = 0
                print (moving_right)
                if char_rect.right - wall.left <=10:
                    print("uncollided right")
                    moving_right = -5
                    
            elif char_rect.left - wall.right >=-20:
                print("collision left")
                #print(char_rect.left)
                #print(wall.right)
                moving_left = 0
                if char_rect.left - wall.right >=-10:
                    print("uncollided left")
                    moving_left = 5
                    
            elif char_rect.bottom - wall.top <=20:
                #print("collision bottom")
                moving_down = 0
                if char_rect.bottom - wall.top <=10:
                    #print("uncollided bottom")
                    moving_down = -5
                    
            elif char_rect.top - wall.bottom >=-20:
                #print("collision top")
                moving_up = 0
                if char_rect.top - wall.bottom >=-10:
                    #print("uncollided top")
                    moving_up = 5
                    
        else:
            moving_right = -5
            moving_left = 5
            moving_up = 5
            moving_down = -5
                    
    #if not collision_detected:
        #print("slide col exe 2")
        #print("char rect top: " + str(char_rect.top))
        #print("wall bottom: " + str(wall.bottom))
        #print("moving right: " + str(moving_right) + "          moving left: " + str(moving_left))
        #moving_right = -5
        #oving_left = 5
        #moving_up = 5
        #moving_down = -5

        #if char_rect.bottom - wall.top <= -1:
            #print("slide col exe")
            #moving_right = -5
            #moving_left = 5
            
            #if char_rect.top - wall.bottom <= -1:
            
                    
        

        
    for wall in wall_list:
        pygame.draw.rect(screen, color, wall)
        

        
    pygame.draw.rect(screen,pygame.Color("purple"),rand_rect) 
    #pygame.draw.rect(screen,pygame.Color("yellow"),wall1)
    pygame.draw.rect(screen,pygame.Color("blue"),char_rect)
    pygame.display.update()
    clock.tick(120)