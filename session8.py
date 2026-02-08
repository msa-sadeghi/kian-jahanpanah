import pygame
pygame.init()

WIDTH = 1000
HEIGHT = 640

mouse_image = pygame.image.load("martin.png")
mouse_rect = mouse_image.get_rect(topleft=(10, 10))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         mouse_rect.x -= 5
        #     if event.key == pygame.K_RIGHT:
        #         mouse_rect.x += 5
        #     if event.key == pygame.K_UP:
        #         mouse_rect.y -= 5
        #     if event.key == pygame.K_DOWN:
        #         mouse_rect.y += 5
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        mouse_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        mouse_rect.x += 5
    # screen.fill("pink")
    screen.fill((100, 50, 200))
    screen.blit(mouse_image, mouse_rect)
    pygame.display.update()