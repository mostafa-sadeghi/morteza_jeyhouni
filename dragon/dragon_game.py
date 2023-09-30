import random
import pygame
from pyscreeze import center
pygame.init()
WIDTH = 1000
HEIGHT = 600
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
dragon = pygame.transform.scale(
    pygame.image.load("dragon/dragon.png"), (128, 128))
dragon = pygame.transform.flip(dragon, True, False)
dragon_rect = dragon.get_rect()
dragon_rect.topleft = (25, HEIGHT/2)
meat = pygame.image.load("dragon/meat.png")
meat_rect = meat.get_rect(
    center=(WIDTH + 100, random.randint(100, HEIGHT - 50)))
FPS = 60
score = 0
lives = 3
font = pygame.font.SysFont("arial", 62)


score_text = font.render(f"Score: {score}", True, (255, 0, 0))
score_rect = score_text.get_rect(topleft=(5, 20))

lives_text = font.render(f"Lives: {lives}", True, (255, 0, 0))
lives_rect = lives_text.get_rect(topright=(WIDTH, 20))

game_over_text = font.render(f"Game Over...", True, (255, 255, 255))
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WIDTH/2, HEIGHT/2)

continue_text = font.render(
    f"Press Any key to continue...", True, (255, 255, 255))
continue_rect = continue_text.get_rect()
continue_rect.center = (WIDTH/2, HEIGHT/2 + 60)

clock = pygame.time.Clock()

pygame.mixer.music.load("dragon/angry.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)


dragon_sound = pygame.mixer.Sound("dragon/dragon_sound.mp3")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and dragon_rect.top >= 0:
        dragon_rect.y -= 5
    if keys[pygame.K_DOWN] and dragon_rect.bottom <= HEIGHT:
        dragon_rect.y += 5

    meat_rect.x -= 5

    if meat_rect.x <= 0:
        lives -= 1
        meat_rect.center = (WIDTH + 100, random.randint(100, HEIGHT - 50))

    if dragon_rect.colliderect(meat_rect):
        dragon_sound.play()
        score += 1
        meat_rect.center = (WIDTH + 100, random.randint(100, HEIGHT - 50))

    if lives == 0:
        display_surface.blit(game_over_text, game_over_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()
        pygame.mixer.music.stop()
        lives = 3
        score = 0

        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    is_paused = False
                    pygame.mixer.music.play(-1)

    lives_text = font.render(f"Lives: {lives}", True, (255, 0, 0))
    score_text = font.render(f"Score: {score}", True, (255, 0, 0))

    display_surface.fill((0, 0, 0))
    display_surface.blit(dragon, dragon_rect)
    display_surface.blit(meat, meat_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(lives_text, lives_rect)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
