import pygame
from constants import *
from player import Player
from game import Game
pygame.init()
clock = pygame.time.Clock()
first_time = pygame.time.get_ticks()
bullet_group = pygame.sprite.Group()
my_player = Player(bullet_group)

enemy_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()

my_game = Game(my_player, enemy_group, bullet_group, enemy_bullet_group)
my_game.start_new_level()

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
            if event.key == pygame.K_SPACE:
                my_player.fire()
    screen.fill((0, 0, 0))
    if next_time - first_time < 2000:
        screen.blit(welcome_text, welcome_rect)
    else:
        my_player.move()
        my_player.draw(screen)
        bullet_group.update()
        bullet_group.draw(screen)

        enemy_group.update()
        enemy_group.draw(screen)
        my_game.update()
    pygame.display.update()
    clock.tick(FPS)
