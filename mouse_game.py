import pygame
import random
pygame.init()
WIDTH = 1000
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))

mouse_image = pygame.image.load("martin.png")
mouse_image = pygame.transform.scale_by(mouse_image, 0.5)
mouse_rect = mouse_image.get_rect(midbottom=(WIDTH/2, HEIGHT))

cheese_image = pygame.image.load("cheese.png")
cheese_image = pygame.transform.scale_by(cheese_image, 0.16)
cheese_rect = cheese_image.get_rect(midtop=(WIDTH/2, 0))
bomb_image = pygame.image.load("bomb.png")
bomb_image = pygame.transform.scale_by(bomb_image, 0.3)
bomb_rect = bomb_image.get_rect(midtop=(WIDTH/2 - 100, 0))
bg_color = "white"
FPS = 60
C = pygame.time.Clock()

f = pygame.font.SysFont("arial", 22)
score = 0
health = 5
score_text = f.render(f"score : {score}", True, "green")
health_text = f.render(f"health : {health}", True, "green")

bomb_sound = pygame.mixer.Sound("Big Boing.wav")

running = True
while running == True:
    C.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    screen.fill(bg_color)
    if health > 0:
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            mouse_rect.x -= 5
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            mouse_rect.x += 5
        if mouse_rect.colliderect(cheese_rect): 
            score += 1
            bomb_sound.play()
            cheese_rect = cheese_image.get_rect(midtop=(random.randint(50, 900), 0))
        if mouse_rect.colliderect(bomb_rect):
            health -= 1
            bomb_rect = bomb_image.get_rect(midtop=(random.randint(50, 900), 0))
        if cheese_rect.bottom >= HEIGHT:
            cheese_rect = cheese_image.get_rect(midtop=(random.randint(50, 900), 0))
        if bomb_rect.bottom >= HEIGHT:
            bomb_rect = bomb_image.get_rect(midtop=(random.randint(50, 900), 0))
        score_text = f.render(f"score : {score}", True, "green")
        health_text = f.render(f"health : {health}", True, "green")
        cheese_rect.y += 5
        bomb_rect.y += 5
        screen.blit(mouse_image, mouse_rect)
        screen.blit(cheese_image, cheese_rect)
        screen.blit(bomb_image, bomb_rect)
        screen.blit(score_text, (50, 50))
        screen.blit(health_text, (50, 80))
    else:
        pass
    pygame.display.update()