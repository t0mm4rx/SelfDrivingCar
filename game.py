import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame, sys
from pygame.locals import *
from Car import *
from Road import *

pygame.init()

screen = pygame.display.set_mode((1200, 1000), 0, 32)
clock = pygame.time.Clock()
pygame.display.set_caption('Racing game')

font_20 = pygame.font.SysFont("monospace", 20)

road = Road("road1.json", screen)
car = Car(None, screen)

def draw():
    clock.tick(60)
    screen.fill( (50, 50, 70) )

    label_fps = font_20.render("FPS: {}".format(round(clock.get_fps())), 1, (255,255,255))
    screen.blit(label_fps, (10, 10))

    road.draw()
    car.draw()

    pygame.display.update()


while True:
    draw()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
