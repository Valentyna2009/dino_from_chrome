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

running = True

while running:
    # это показывает, с какой скоростью будет прокручиваться земля. Чем больше фпс, тем быстрее
    clock.tick(fps)
    
    # draw background
    screen.blit(bg, (0, 0))
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0

    # draw and scroll the ground
    screen.blit(ground, (ground_scroll, int(SCREEN_HEIGHT / 4)))

    # если нажать на крестик, то окно закроется
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # show all the images in the ground
    pygame.display.update()

pygame.quit()