import pygame, sys

pygame.init()
screen = pygame.display.set_mode((2432/3,2528/3))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('Assets/Digital_assessment_map_no-light.png').convert()
#bg_surface = pygame.transform.scale2x(bg_surface)
#bg_surface = pygame.transform.scale_by(bg_surface, 0.333)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
           

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                pass
     
                
    screen.blit(bg_surface,(0,0)) 
    pygame.display.update()
    clock.tick(120)