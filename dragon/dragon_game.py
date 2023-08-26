import pygame
pygame.init()


WIDTH = 1000
HEIGHT = 600


display_surface = pygame.display.set_mode((WIDTH, HEIGHT))

dragon = pygame.image.load("dragon.png")
dragon = pygame.transform.flip(dragon, True, False)
dragon_rect = dragon.get_rect()
dragon_rect.topleft = (25, HEIGHT/2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display_surface.blit(dragon, dragon_rect)
    pygame.display.update()

pygame.quit()
