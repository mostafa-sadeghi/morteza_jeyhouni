from pygame.sprite import Sprite
import pygame
import random
from config import *


class Monster(Sprite):
    def __init__(self, x, y, image, type):
        super().__init__()
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.velocity = random.randint(1, 5)

        self.x_dir = random.choice([-1, 1])
        self.y_dir = random.choice([-1, 1])

    def update(self):
        self.rect.x += self.x_dir * self.velocity
        self.rect.y += self.y_dir * self.velocity
        if self.rect.left < 0 or self.rect.right > WINDOW_WIDTH:
            self.x_dir = -1 * self.x_dir
        if self.rect.bottom > WINDOW_HEIGHT - 164 or self.rect.top < 100:
            self.y_dir = -1 * self.y_dir
