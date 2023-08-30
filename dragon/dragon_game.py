import random
import pygame
pygame.init()
WIDTH = 1000
HEIGHT = 600
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
dragon = pygame.transform.scale(pygame.image.load("dragon.png"), (128, 128))
dragon = pygame.transform.flip(dragon, True, False)
dragon_rect = dragon.get_rect()
dragon_rect.topleft = (25, HEIGHT/2)
meat = pygame.image.load("meat.png")
meat_rect = meat.get_rect(
    center=(WIDTH + 100, random.randint(100, HEIGHT - 50)))
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and dragon_rect.top >= 0:
        dragon_rect.y -= 5
    if keys[pygame.K_DOWN] and dragon_rect.bottom <= HEIGHT:
        dragon_rect.y += 5

    meat_rect.x -= 5

    if meat_rect.x <= 0:
        meat_rect.center = (WIDTH + 100, random.randint(100, HEIGHT - 50))
    display_surface.fill((0, 0, 0))
    display_surface.blit(dragon, dragon_rect)
    display_surface.blit(meat, meat_rect)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
