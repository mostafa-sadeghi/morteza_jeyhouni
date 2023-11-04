import pygame
from constants import *
from player import Player
pygame.init()

first_time = pygame.time.get_ticks()
bullet_group = pygame.sprite.Group()
my_player = Player(bullet_group)

font = pygame.font.Font("assets/Facon.ttf", 64)
welcome_text = font.render("Welcome To My Game", True, (255, 0, 255))
welcome_rect = welcome_text.get_rect()
welcome_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)

running = True
while running:
    next_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    screen.fill((0, 0, 0))
    if next_time - first_time < 2000:
        screen.blit(welcome_text, welcome_rect)
    else:
        my_player.move()
        my_player.draw(screen)
    pygame.display.update()
