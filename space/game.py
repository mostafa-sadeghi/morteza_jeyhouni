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
        self.start_new_level_sound = pygame.mixer.Sound("assets/new_round.wav")

    def start_new_level(self):
        self.level_number += 1
        for row in range(self.level_number * 1):
            for col in range(10):
                enemy = Enemy(col * 64, row * 64 + 50, self.enemy_bullet_group)
                self.enemy_group.add(enemy)

    def check_collisions(self):
        if pygame.sprite.groupcollide(self.player_bullet_group, self.enemy_group, True, True):
            self.score += 1
        if not self.enemy_group:
                self.start_new_level_sound.play()
                self.start_new_level()



    def update(self):
        on_edge = False
        for enemy in self.enemy_group:
            if enemy.rect.right >= WINDOW_WIDTH or enemy.rect.left <= 0:
                on_edge = True
                break
        if on_edge:
            breach = False
            for enemy in self.enemy_group:
                enemy.direction *= -1
                enemy.rect.y += 30 * self.level_number
                if enemy.rect.bottom >= WINDOW_HEIGHT - 100:
                    breach = True
            if breach:
                self.reset_game()


    def reset_game(self):
      
        self.score = 0
        self.level_number = 0
        self.player.lives = 3
        self.enemy_group.empty()
        self.enemy_bullet_group.empty()
        self.player_bullet_group.empty()
        self.start_new_level()

    def draw(self):
        font = pygame.font.Font("assets/Facon.ttf", 24)
        score_text = font.render(f"Score:{self.score}",True, (10,230,210))
        score_rect = score_text.get_rect()
        score_rect.topleft = (0,0)
        screen.blit(score_text, score_rect)
        lives_text = font.render(f"lives:{self.player.lives}",True, (10,230,210))
        lives_rect = lives_text.get_rect()
        lives_rect.topright = (WINDOW_WIDTH,0)
        screen.blit(lives_text, lives_rect)
        level_text = font.render(f"level:{self.level_number}",True, (10,230,210))
        level_rect = level_text.get_rect()
        level_rect.topright = (WINDOW_WIDTH/2,0)
        screen.blit(level_text, level_rect)


# TODO   enemy shoot
# TODO   next level
# TODO   convert to exe