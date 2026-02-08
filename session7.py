import pygame
import random
pygame.init()
WIDTH = 600
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))

r = 80
g = 100
b = 255

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)

    screen.fill((r, g, b))
    pygame.display.update()