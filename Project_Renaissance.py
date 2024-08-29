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

move_right = -5
moving_left = 5
moving_up = 5
moving_down = -5

rand_rect = pygame.Rect(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,50,50)

char_rect = pygame.Rect(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,50,50)

#wall data
wall1 = pygame.Rect(591,508,1000,370-235)
wall2 = pygame.Rect(591,380,620,10-0)

wall_list = [wall1,wall2]
new_wall_list = []

color = pygame.Color("yellow")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                      
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        screen.fill(pygame.Color("black"))
        screen.blit(bg_surface,(move_x,move_y))
        move_x += move_right
        rand_rect.x += move_right
        for wall in wall_list:
            wall.x += move_right
                

    if keys[pygame.K_a]:
        screen.fill(pygame.Color("black"))
        screen.blit(bg_surface,(move_x + 10,move_y))
        move_x += 5
        rand_rect.x += 5
        for wall in wall_list:
            wall.x += 5
        
    if keys[pygame.K_w]:
        screen.fill(pygame.Color("black"))
        screen.blit(bg_surface,(move_x + 5,move_y + 5))
        move_y += 5
        rand_rect.y += 5
        for wall in wall_list:
            wall.y += 5
        
    if keys[pygame.K_s]:
        screen.fill(pygame.Color("black"))
        screen.blit(bg_surface,(move_x + 5,move_y - 5))
        move_y += -5
        rand_rect.y += -5
        for wall in wall_list:
            wall.y += -5
            

    for wall in wall_list:

        if char_rect.colliderect(wall):
            print ("collision")

            if char_rect.right - wall.left <=20:
                print("collision right")
                print (char_rect.bottom)
                print (wall.top)
                move_right = 0
                if char_rect.right - wall.left <=10:
                    print("uncollided right")
                    move_right = -5
        if char_rect.bottom - wall.top <= -1:
            print("slide col exe")
            move_right = -5
                    
        
    if event.type == pygame.MOUSEBUTTONDOWN:
        print(pygame.mouse.get_pos())
        
    for wall in wall_list:
        pygame.draw.rect(screen, color, wall)
        

        
    pygame.draw.rect(screen,pygame.Color("purple"),rand_rect) 
    #pygame.draw.rect(screen,pygame.Color("yellow"),wall1)
    pygame.draw.rect(screen,pygame.Color("blue"),char_rect)
    pygame.display.update()
    clock.tick(120)