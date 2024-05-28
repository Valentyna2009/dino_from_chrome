import pygame
from pygame.locals import *
import random

# gets everything ready for using Pygame
pygame.init()

clock = pygame.time.Clock()
fps = 70

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500


# create the game screeen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# name of game
pygame.display.set_caption('Dino from Chrome')

# define game variables
ground_scroll = 0
scroll_speed = 4

# load images
bg = pygame.image.load('dino_from_chrome/bg3.jpg')
ground = pygame.image.load('dino_from_chrome/dino-ground.png')

i = ground.get_height()
eto_samoe = SCREEN_HEIGHT - i
toxyj_nj = (SCREEN_HEIGHT - eto_samoe) + 38


class Dino(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 3):
            images = pygame.image.load(f'dino_from_chrome/DinoRun{num}.png')
            self.images.append(images)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):

        # handle the animation
        self.counter += 0.5
        dino_cooldown = 5

        if self.counter > dino_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]

dino_group = pygame.sprite.Group()
dinny = Dino(SCREEN_WIDTH / 4, toxyj_nj)
dino_group.add(dinny)

running = True

while running:
    # это показывает, с какой скоростью будет прокручиваться земля. Чем больше фпс, тем быстрее
    clock.tick(fps)
    
    # draw background
    screen.blit(bg, (0, 0))

    dino_group.draw(screen)
    dino_group.update()

    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0

    # draw and scroll the ground
    screen.blit(ground, (ground_scroll, int(SCREEN_HEIGHT / 4)))

    # если нажать на крестик, то окно закроется
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # show all the images on the screen
    pygame.display.update()

pygame.quit()