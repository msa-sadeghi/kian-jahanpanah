import pygame

pygame.init()

from player import Player

my_player = Player()
WIDTH = 1000
HEIGHT = 640


f = pygame.font.SysFont("arial", 24)
f.render("salam", True, "red")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
FPS = 60
running = True

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("#1e1e1e")
    my_player.draw(screen)
    my_player.move()
    my_player.animation()
    pygame.display.update()
    clock.tick(FPS)
