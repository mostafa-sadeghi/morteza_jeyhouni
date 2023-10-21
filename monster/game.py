import pygame
from config import *
from random import randint, choice

from monster import Monster


class Game:
    def __init__(self, player, monster_group):
        self.score = 0
        self.level_number = 0
        self.player = player
        self.monster_group = monster_group
        self.font = pygame.font.Font("monster/assets/Abrushow.ttf", 32)

        blue_monster = pygame.image.load("monster/assets/blue_monster.png")
        green_monster = pygame.image.load("monster/assets/green_monster.png")
        purple_monster = pygame.image.load("monster/assets/purple_monster.png")
        yellow_monster = pygame.image.load("monster/assets/yellow_monster.png")

        self.all_monsters_images = [
            blue_monster, green_monster, purple_monster, yellow_monster]

        self.target_type = randint(0, 3)
        self.target_image = self.all_monsters_images[self.target_type]
        self.target_rect = self.target_image.get_rect()
        self.target_rect.bottom = 100
        self.target_rect.centerx = WINDOW_WIDTH/2

    def draw(self, screen):
        COLORS = (
            (0, 0, 255),
            (0, 255, 0),
            (230, 20, 170),
            (233, 162, 10),
        )
        score_text = self.font.render(
            f'Score: {self.score}', True, (255, 255, 255))
        level_text = self.font.render(
            f'level: {self.level_number}', True, (255, 255, 255))
        lives_text = self.font.render(
            f'lives: {self.player.lives}', True, (255, 255, 255))
        warps_text = self.font.render(
            f'warps: {self.player.warps}', True, (255, 255, 255))

        score_rect = score_text.get_rect(topleft=(10, 10))
        level_rect = level_text.get_rect(topleft=(10, 40))
        lives_rect = lives_text.get_rect(topright=(WINDOW_WIDTH - 50, 10))
        warps_rect = warps_text.get_rect(topright=(WINDOW_WIDTH - 50, 40))

        screen.blit(score_text, score_rect)
        screen.blit(level_text, level_rect)
        screen.blit(lives_text, lives_rect)
        screen.blit(warps_text, warps_rect)
        screen.blit(self.target_image, self.target_rect)
        pygame.draw.rect(
            screen, COLORS[self.target_type], (0, 100, WINDOW_WIDTH, WINDOW_HEIGHT-200), 3)

    def start_new_level(self):
        self.level_number += 1
        self.player.lives += 1
        self.player.warps += 1

        for i in range(self.level_number):
            self.monster_group.add(
                Monster(100, 100, self.all_monsters_images[0], 0))
            self.monster_group.add(
                Monster(200, 200, self.all_monsters_images[1], 1))
            self.monster_group.add(
                Monster(300, 300, self.all_monsters_images[2], 2))
            self.monster_group.add(
                Monster(400, 400, self.all_monsters_images[3], 3))

    def choose_new_target(self):
        remained_monsters = self.monster_group.sprites()
        new_target = choice(remained_monsters)
        self.target_image = new_target.image
        self.target_type = new_target.type

    def update(self):
        # we want to find collided monster
        collided_monster = pygame.sprite.spritecollideany(
            self.player, self.monster_group)
        # if knight collided with any monsters
        if collided_monster:
            # check if knight collided with right monster(target monster)
            if collided_monster.type == self.target_type:
                collided_monster.remove(self.monster_group)
                self.score += 1
                self.player.catch_sound.play()
                if self.monster_group:
                    self.choose_new_target()
                else:
                    self.start_new_level()
            # check if knight collided with wrong monster
            else:
                self.player.lives -= 1
                self.player.die_sound.play()
                self.player.reset()
