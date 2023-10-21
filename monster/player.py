import pygame
from pygame.sprite import Sprite
from config import *


class Player(Sprite):
    def __init__(self):
        self.image = pygame.image.load("monster/assets/knight.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = WINDOW_HEIGHT
        self.rect.centerx = WINDOW_WIDTH/2
        self.lives = 3
        self.velocity = 5
        self.catch_sound = pygame.mixer.Sound("monster/assets/catch.wav")
        self.die_sound = pygame.mixer.Sound("monster/assets/die.wav")
        self.warps = 2

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def reset(self):
        self.rect.bottom = WINDOW_HEIGHT
        self.rect.centerx = WINDOW_WIDTH/2

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.top > 100:
            self.rect.y -= self.velocity

        if keys[pygame.K_DOWN] and self.rect.bottom < WINDOW_HEIGHT - 100:
            self.rect.y += self.velocity

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity

        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.velocity

    def escape(self):
        if self.warps > 0:
            self.reset()
            self.warps -= 1
