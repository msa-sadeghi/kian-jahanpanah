import pygame
from pygame.sprite import Sprite
import os


class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.health = 5
        self.score = 0
        self.animation_types = ("Idle", "Run")
        self.all_images = []
        for i in range(len(self.animation_types)):
            imgs = []
            n = len(os.listdir(f"assets/boy/{self.animation_types[i]}"))
            for j in range(1, n + 1):
                im = pygame.image.load(f"assets/boy/{self.animation_types[i]}/{self.animation_types[i]} ({j}).png")
                im = pygame.transform.scale_by(im, 0.3)
                imgs.append(im)
            self.all_images.append(imgs)
        self.animation_index = 0
        self.frame_index = 0
        self.image = self.all_images[self.animation_index][self.frame_index]
        self.rect = self.image.get_rect(topleft=(100, 300))
        self.frames = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def animation(self):
        self.frames += 1
        if self.frames >= 10:
            self.frames = 0
            self.frame_index += 1
            if self.frame_index >= len(self.all_images[self.animation_index]):
                self.frame_index = 0
        self.image = self.all_images[self.animation_index][self.frame_index]

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
