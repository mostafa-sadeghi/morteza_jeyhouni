from enemy import Enemy
from constants import *
class Game:
    def __init__(self, player, enemy_group, player_bullet_group, enemy_bullet_group):
        self.score = 0
        self.level_number = 0
        self.player = player
        self.enemy_group = enemy_group
        self.player_bullet_group = player_bullet_group
        self.enemy_bullet_group = enemy_bullet_group

    def start_new_level(self):
        self.level_number += 1
        for row in range(self.level_number * 2):
            for col in range(10):
                enemy = Enemy(col * 64, row * 64, self.enemy_bullet_group)
                self.enemy_group.add(enemy)


    def update(self):
        on_edge = False
        for enemy in self.enemy_group:
            if enemy.rect.right >= WINDOW_WIDTH or enemy.rect.left <= 0:
                on_edge = True
                break
        if on_edge:
            for enemy in self.enemy_group:
                enemy.direction *= -1



