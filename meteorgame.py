#import libraries
import pygame
from pygame.locals import *
import random


#initialize variables
size = width, height = (800,800)
space_w = int(width/5)
startind = False
speed = 10

pygame.init()
run = True

#set window size
screen = pygame.display.set_mode(size)

#set title
pygame.display.set_caption("space geme")

#images load
spacebg = pygame.image.load(Games_Files/space BG.png")
spacebg_loc = spacebg.get_rect()

title = pygame.image.load("Game_Files/Gametile.png")
title_loc = title.get_rect()
title_loc.center = width/2 height/2

gamestart = pygame.image.load("Game_Files/start msg.png")
gamestart_loc = gamestart.get.rect()
gamestart_loc.center = width/2, height/2

spaceship = pygame.image.load("Game_Files/start msg.png")
spaceship_loc = spaceship.get.rect()
spaceship_loc.center = space_w, height/2 * .8

spaceship = pygame.image.load("Game_Files/Gameover.png")
gameover_loc = gameover.get.rect()
gameover_loc.center = space_w, height/2 * .8

meteor = pygame.image.load("Game_Files/start msg.png")
meteor_loc = meteor.get.rect()
meteor_loc.center = width/2, height/2 * .1

#apply changes
screen.blit(spacebg,spacebg_loc)
screen.blit(gamestart,gamestart_loc)
screen.blit(spaceship,spaceship_loc)
screen.blit(meteor,meteor_loc)
screen.blit(title,title_loc)
pygame.display.update()

#start game sequence
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_s:
                starind = True
            run = False

        while startind:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key in [K_a, K_LEFT]:
                        spaceship_loc = spaceship_loc.move(-space_w,0)
                    if event.key in [K_d, K_RIGHT]:
                        spaceship_loc = spaceship_loc.move(-space_w,0)
                if event.type == QUIT
                    run = False
                    startind = False
                meteor_loc[1] = meteor_loc[1] + speed
                if meteor_loc[1] > height
                    meteor_loc.center = space_w * random.randint(1,5), -100

                screen.blit(spacebg,spacebg_loc)
                screen.blit(spaceship,spaceship_loc)
                screen.blit(meteor,meteor_loc)
                screen.blit(title,title_loc)

#gameover
                if spaceship_loc[0] = meteor_loc[0] and scapeship_loc[1] < meteor_loc[1] + 175 and spaeship_loc{1} > meteor_loc[1] - 175:
                    screen.blit(gameover, gameover_loc)
                    pygame.display.update()
                    startind = False
                pygame.display.update()

#quite game
pygame.quit()