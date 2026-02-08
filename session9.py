import pygame
pygame.init()

WIDTH = 1000
HEIGHT = 640

screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill("white")

    pygame.draw.line(screen, "darkgreen", (40, 200), (350, 200), 10)
    pygame.draw.circle(screen, "cyan", (500, 320), 30, 4)
    pygame.draw.rect(screen, "red",  (200, 350, 80, 80), 5)
    pygame.display.update()