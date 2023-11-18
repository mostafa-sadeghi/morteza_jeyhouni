from pygame.sprite import Sprite
import pygame
class Enemy(Sprite):
    def __init__(self, x,y , enemy_bullet_group):
        super().__init__()
        self.image = pygame.image.load("assets/enemy.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.speed = 3
        self.direction = 1
        self.enemy_bullet_group = enemy_bullet_group

    def update(self):
        self.rect.x += self.direction * self.speed