import pygame
import random
pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
FPS = 60
clock = pygame.time.Clock()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


dog_left = pygame.image.load("dog.png")
dog_right = pygame.transform.flip(dog_left, True, False)

dog = dog_right
dog_rect = dog.get_rect()
dog_rect.bottom = WINDOW_HEIGHT
dog_rect.centerx = WINDOW_WIDTH/2
DOG_NORMAL_VELOCITY = 5
DOG_BOOST_VELOCITY = 15
dog_velocity = DOG_NORMAL_VELOCITY
STARTING_BOOST_LEVEL = 100
boost_level = STARTING_BOOST_LEVEL
font = pygame.font.Font("myfont.otf", 24)
boost_text = font.render(f"Boost Level: {boost_level}", True, (255, 255, 255))
boost_rect = boost_text.get_rect()
boost_rect.topright = (WINDOW_WIDTH - 40, 10)


burger_image = pygame.image.load("burger.png")
burger_rect = burger_image.get_rect()
burger_rect.topleft = (random.randint(0, WINDOW_WIDTH-48), -100)

score = 0

score_text = font.render(f'Score: {score}', True, (0, 0, 255))
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)
burger_points = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and dog_rect.top > 0:
        dog_rect.y -= dog_velocity

    if keys[pygame.K_DOWN] and dog_rect.bottom < WINDOW_HEIGHT:
        dog_rect.y += dog_velocity

    if keys[pygame.K_LEFT] and dog_rect.left > 0:
        dog_rect.x -= dog_velocity
        dog = dog_left

    if keys[pygame.K_RIGHT] and dog_rect.right < WINDOW_WIDTH:
        dog_rect.x += dog_velocity
        dog = dog_right

    if keys[pygame.K_SPACE] and boost_level > 0:
        dog_velocity = DOG_BOOST_VELOCITY
        boost_level -= 1
    else:
        dog_velocity = DOG_NORMAL_VELOCITY

    burger_rect.y += 5
    if burger_rect.y > WINDOW_HEIGHT:
        burger_rect.topleft = (random.randint(0, WINDOW_WIDTH-48), -100)

    boost_text = font.render(
        f"Boost Level: {boost_level}", True, (255, 255, 255))

    burger_points = int((WINDOW_HEIGHT - burger_rect.y)/10) + 5

    if dog_rect.colliderect(burger_rect):
        if boost_level < STARTING_BOOST_LEVEL:
            boost_level += 10
        score += burger_points
        burger_rect.topleft = (random.randint(0, WINDOW_WIDTH-48), -100)

    score_text = font.render(f'Score: {score}', True, (0, 0, 255))

    display_surface.fill((0, 0, 0))
    display_surface.blit(boost_text, boost_rect)
    display_surface.blit(dog, dog_rect)
    display_surface.blit(burger_image, burger_rect)
    display_surface.blit(score_text, score_rect)
    pygame.display.update()
    clock.tick(FPS)
