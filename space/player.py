import pygame
from pygame.sprite import Sprite
from constants import *
from player_bullet import PlayerBullet
class Player(Sprite):
    def __init__(self, bullet_group):
        self.image = pygame.image.load("assets/player_ship.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = WINDOW_HEIGHT
        self.rect.centerx = WINDOW_WIDTH/2
        self.bullet_group = bullet_group
        self.speed = 4
        self.lives = 3
        self.fire_sound = pygame.mixer.Sound("assets/player_fire.wav")
        self.hit_sound = pygame.mixer.Sound("assets/player_hit.wav")
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.speed
    def fire(self):
        if len(self.bullet_group) < 200:
            PlayerBullet(self.rect.centerx, self.rect.top, self.bullet_group)
            self.fire_sound.play()