import pygame
from pygame.locals import *
import random

# gets everything ready for using Pygame
pygame.init()

clock = pygame.time.Clock()
fps = 150

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500


# create the game screeen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# name of game
pygame.display.set_caption('Dino from Chrome')

# define game variables
ground_scroll = 0
scroll_speed = 6
game_over = False
game_start = False
cactus_frequency = 1500
# it means when we start the game, the pipes were created
last_cactus = pygame.time.get_ticks() - cactus_frequency


# load images
bg = pygame.image.load('dino_from_chrome/bg3.jpg')
ground = pygame.image.load('dino_from_chrome/dino-ground.png')
dino_jump = pygame.transform.scale(pygame.image.load('dino_from_chrome/DinoJump.png'), (87, 94))
ground_rect = ground.get_rect()

i = ground.get_height() # 352
eto_samoe = SCREEN_HEIGHT - i # 148
toxyj_nj = (SCREEN_HEIGHT - eto_samoe) + 38 # 390


class Dino(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # the animation of dino
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 3):
            images = pygame.image.load(f'dino_from_chrome/DinoRun{num}.png')
            self.images.append(images)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.jumped = False
        
    def update(self):

        print(f' V = {self.vel}, y = {self.rect.y}')
        # скорость всегда будет больше. если она == 8, то останется 8
        self.vel += 0.01
        #if self.vel == 8:
         #   self.vel = 8

        # jumping
        key_pressed = pygame.key.get_pressed()

        if key_pressed[K_SPACE] and game_start == True and self.jumped == False:
            # it makes the dino jumping
            self.jumped = True
            self.rect.y -= 20
            self.vel = -0.005
        elif self.rect.y <= int(SCREEN_HEIGHT / 1.47): #self.jumped == True: # 340 отвечает за то, что динозавр находится на той линии
            self.jumped = False
            self.rect.y += self.vel * 15
        else:
            self.jumped = False
            self.vel = 0.0

        # handle the animation
        self.counter += 0.5
        dino_cooldown = 5

        if self.counter > dino_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]

class Cactus(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('dino_from_chrome/Cactus/LargeCactus1.1.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def update(self):
        # заставляет кактус двигаться. Ich bin Magie digga!! Digga ich bin Magie!!!!!
        self.rect.x -= scroll_speed
        # если они уxодят за пределы экрана, они погибают
        if self.rect.right < 0:
            self.kill()



dino_group = pygame.sprite.Group()
cactus_group = pygame.sprite.Group()

dinny = Dino(SCREEN_WIDTH / 4, int(SCREEN_HEIGHT / 1.47))
dino_group.add(dinny)

btm_cactus = Cactus(SCREEN_WIDTH, int(SCREEN_HEIGHT / 1.4))
cactus_group.add(btm_cactus)

running = True

while running:
    # это показывает, с какой скоростью будет прокручиваться земля. Чем больше фпс, тем быстрее
    clock.tick(fps)
    
    # draw background
    screen.blit(bg, (0, 0))

    dino_group.draw(screen)
    dino_group.update()
    cactus_group.draw(screen)
    #cactus_group.update()

    # draw and scroll the ground
    screen.blit(ground, (ground_scroll, int(SCREEN_HEIGHT / 4))) # ground on the screen is 125

    # check if the dino hits cactus
    if pygame.sprite.groupcollide(dino_group, cactus_group, False, False) or dinny.rect.top < 0:
        game_over = True


    if game_over == False and game_start == True:
        # generate new cactuses
        time_now = pygame.time.get_ticks()
        if time_now - last_cactus > cactus_frequency:
            new_cactus = Cactus(SCREEN_WIDTH, int(SCREEN_HEIGHT / 1.4))
            # add the cactus on the screen
            cactus_group.add(new_cactus)
            last_cactus = time_now

        cactus_group.update()
        
        ground_scroll -= scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll = 0


    # если нажать на крестик, то окно закроется
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and game_start == False and game_over == False:
                game_start = True

    # show all the images on the screen
    pygame.display.update()

pygame.quit()