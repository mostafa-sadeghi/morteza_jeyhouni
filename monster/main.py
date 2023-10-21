import pygame
from config import *
from player import Player
from game import Game

pygame.init()

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

my_player = Player()
monster_group = pygame.sprite.Group()

my_game = Game(my_player, monster_group)
my_game.start_new_level()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                my_player.escape()

    display_surface.fill((0, 0, 0))
    my_player.draw(display_surface)
    my_player.move()
    my_game.update()
    my_game.draw(display_surface)
    monster_group.update()
    monster_group.draw(display_surface)
    pygame.display.update()
    clock.tick(FPS)
