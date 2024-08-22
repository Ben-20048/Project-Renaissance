import pygame, sys

def check_collision():
    if char_rect.colliderect(wall1):
        print("collision")
        move_x = 0
        move_y = 0

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

wall_list = [wall1]




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                pass 
                
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_d]:
        screen.fill(pygame.Color("black"))
        screen.blit(bg_surface,(move_x,move_y))
        move_x += -5
        rand_rect.x += -5
        wall1.x += -5
        
    if keys[pygame.K_a]:
        screen.fill(pygame.Color("black"))
        screen.blit(bg_surface,(move_x + 10,move_y))
        move_x += 5
        rand_rect.x += 5
        wall1.x += 5
        
    if keys[pygame.K_w]:
        screen.fill(pygame.Color("black"))
        screen.blit(bg_surface,(move_x + 5,move_y + 5))
        move_y += 5
        rand_rect.y += 5
        wall1.y += 5
        
    if keys[pygame.K_s]:
        screen.fill(pygame.Color("black"))
        screen.blit(bg_surface,(move_x + 5,move_y - 5))
        move_y += -5
        rand_rect.y += -5
        wall1.y += -5
        
    if event.type == pygame.MOUSEBUTTONDOWN:
        print(pygame.mouse.get_pos())
        
    check_collision()
        
    pygame.draw.rect(screen,pygame.Color("purple"),rand_rect) 
    pygame.draw.rect(screen,pygame.Color("yellow"),wall1)
    pygame.draw.rect(screen,pygame.Color("blue"),char_rect)
    pygame.display.update()
    clock.tick(120)