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

rand_rect = pygame.Rect(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,50,50)

char_rect = pygame.Rect(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,50,50)

#wall data
wall1 = pygame.Rect(591,508,1000,370-235)
wall2 = pygame.Rect(591,380,620,10-0)

wall_list = [wall1,wall2]
new_wall_list = []

color = pygame.Color("yellow")
coll = False

move_right = True
move_left = True
move_up = True
move_down = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())              
    keys = pygame.key.get_pressed()
    movement_speed = 5
    
            

    for wall in wall_list:

        if char_rect.colliderect(wall):
            print ("collision")
            coll = True
            if abs(char_rect.right - wall.left) <=10:
                print("collision right")
                print(coll)
                #bg_surface, (move_x - 5)
                #move_x += 5
                #rand_rect.x += 5
                #for wall in wall_list:
                 #   new_wall_list.append(wall.x+1)
                char_rect.right = wall.left
                movement_speed = 0
                move_right = False
            
        if abs(char_rect.left - wall.right) <=10:
            print("collision right")
            print(coll)
            char_rect.right = wall.left
            movement_speed = 0
            move_left = False
                
        else:
            coll = False
                
    if keys[pygame.K_d] and move_right and not coll:
        screen.fill(pygame.Color("black"))
        screen.blit(bg_surface,(move_x,move_y))
        move_x += -movement_speed
        rand_rect.x += -movement_speed
        for wall in wall_list:
            wall.x += -movement_speed
                

    if keys[pygame.K_a] and move_left and not coll:
        screen.fill(pygame.Color("black"))
        screen.blit(bg_surface,(move_x + 10,move_y))
        move_x += movement_speed
        rand_rect.x += movement_speed
        for wall in wall_list:
            wall.x += movement_speed
        
    if keys[pygame.K_w] and move_up and not coll:
        screen.fill(pygame.Color("black"))
        screen.blit(bg_surface,(move_x + 5,move_y + 5))
        move_y += movement_speed
        rand_rect.y += movement_speed
        for wall in wall_list:
            wall.y += movement_speed
        
    if keys[pygame.K_s] and move_down and not coll:
        screen.fill(pygame.Color("black"))
        screen.blit(bg_surface,(move_x + 5,move_y - 5))
        move_y += -movement_speed
        rand_rect.y += -movement_speed
        for wall in wall_list:
            wall.y += -movement_speed                
        
    
        
    for wall in wall_list:
        pygame.draw.rect(screen, color, wall)
        

        
    pygame.draw.rect(screen,pygame.Color("purple"),rand_rect) 
    #pygame.draw.rect(screen,pygame.Color("yellow"),wall1)
    pygame.draw.rect(screen,pygame.Color("blue"),char_rect)
    pygame.display.update()
    clock.tick(120)