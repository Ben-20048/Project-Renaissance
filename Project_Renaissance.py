import pygame, sys

def check_collision(wall):
    
    global moving_right
    global moving_left
    global moving_up
    global moving_down
    
    moving_right = True
    moving_left = True
    moving_up = True
    moving_down = True
    
    for wall in wall_list:
    
        if char_rect.colliderect(wall):
            print("collision")
        
            #if char_rect.right > wall.left and char_rect.left < wall.left:
            if char_rect.right - wall.left >= 0:
                
                #if char_rect.right >= wall.left and char_rect.left < wall.left:
                    #if pygame.key.get_pressed()[pygame.K_d]:
                print("set to false R")
                moving_right = False
                moving_up = True
                moving_down = True
                #moving_left = True
                if char_rect.top <= wall.y or char_rect.top >= wall.y:
                    if char_rect.bottom >= wall.y or char_rect.bottom <= wall.y:
                        print("set to false R second criterea")
                        moving_right = False
                        moving_up = True
                        moving_down = True
                         
            if char_rect.left < wall.right and char_rect.right > wall.right:
                
                if char_rect.left <= wall.right and char_rect.right > wall.right:    
                    #if pygame.key.get_pressed()[pygame.K_a]:
                    print("set to false L")
                    moving_left = False
                    moving_up = True
                    moving_down = True
                    #moving_right = True
                    
            if char_rect.bottom > wall.top and char_rect.top < wall.bottom:
                if char_rect.bottom >= wall.top and char_rect.top < wall.top:
                    #if pygame.key.get_pressed()[pygame.K_s]:
                    print("set to false D")
                    moving_down = False
                    moving_left = True
                    moving_right = True
                    
            if char_rect.top < wall.bottom and char_rect.bottom > wall.top:
                if char_rect.top <= wall.bottom and char_rect.bottom > wall.bottom:
                    #if pygame.key.get_pressed()[pygame.K_w]:
                    print("set to false U")
                    moving_up = False
                    moving_left = True
                    moving_right = True
            

                
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

color = pygame.Color("yellow")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                      
    keys = pygame.key.get_pressed()
    
    for wall in wall_list:
        check_collision(wall)

    if keys[pygame.K_d] and moving_right:
            screen.fill(pygame.Color("black"))
            screen.blit(bg_surface,(move_x,move_y))
            move_x += -5
            rand_rect.x += -5
            for wall in wall_list:
                wall.x += -5
                

    if keys[pygame.K_a] and moving_left:
        screen.fill(pygame.Color("black"))
        screen.blit(bg_surface,(move_x + 10,move_y))
        move_x += 5
        rand_rect.x += 5
        for wall in wall_list:
            wall.x += 5
        
    if keys[pygame.K_w] and moving_up:
        screen.fill(pygame.Color("black"))
        screen.blit(bg_surface,(move_x + 5,move_y + 5))
        move_y += 5
        rand_rect.y += 5
        for wall in wall_list:
            wall.y += 5
        
    if keys[pygame.K_s] and moving_down:
        screen.fill(pygame.Color("black"))
        screen.blit(bg_surface,(move_x + 5,move_y - 5))
        move_y += -5
        rand_rect.y += -5
        for wall in wall_list:
            wall.y += -5
        
    if event.type == pygame.MOUSEBUTTONDOWN:
        print(pygame.mouse.get_pos())
        
    for wall in wall_list:
        pygame.draw.rect(screen, color, wall)
        

        
    pygame.draw.rect(screen,pygame.Color("purple"),rand_rect) 
    #pygame.draw.rect(screen,pygame.Color("yellow"),wall1)
    pygame.draw.rect(screen,pygame.Color("blue"),char_rect)
    pygame.display.update()
    clock.tick(120)