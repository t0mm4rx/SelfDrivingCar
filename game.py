"""
    Entry-point of this project. If you edit this, make sure to create a copy of this file.
    It:
    - loads a config file
    - create the map
    - instantiate players
    - start the game loop, draw and update everything 60 times/second
"""

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame, sys
from pygame.locals import *
from Car import *
from Road import *
import json

if (len(sys.argv) != 2):
    print("Error, you need to provide a config file !")
    print("python game.py config.json")
    exit()

if (os.path.isfile(sys.argv[1])):
    config = json.loads(open(sys.argv[1]).read())
else:
    print("The config file your provided doesn't exist !")
    exit()

pygame.init()

screen = pygame.display.set_mode((1200, 1000), 0, 32)
clock = pygame.time.Clock()
pygame.display.set_caption('Racing game')

font_20 = pygame.font.SysFont("monospace", 20)

road = Road(config['map'], screen)
cars = []

for car in config['players']:
    for car2 in cars:
        if (car2.name == car['name']):
            print("Two players can't have the same name")
            exit()
        if (car2.playable and car['playable']):
            print("Only one car can be playable")
            exit()
    cars.append(Car(car["folder"], car['name'], road, car["playable"], car["debug"], screen))

def draw():
    clock.tick(60)
    screen.fill( (50, 50, 70) )

    label_fps = font_20.render("FPS: {}".format(round(clock.get_fps())), 1, (255,255,255))
    screen.blit(label_fps, (10, 10))

    road.draw()
    for car in cars:
        car.draw()

    pygame.display.update()


while True:
    draw()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
