import pygame
pygame.init()
WIDTH = 1000
HEIGHT = 640
player = pygame.Rect(40, 100, 50, 50)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg_color = "white"
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                bg_color = "red"
            elif event.key == pygame.K_b:
                bg_color = "blue"
        
    screen.fill(bg_color)
    pygame.draw.rect(screen, "purple", player)
    pygame.display.update()