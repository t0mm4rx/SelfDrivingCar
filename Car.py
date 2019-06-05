import numpy as np
import pygame
import Utils
import random
from AI import *

class Car():

    def __init__(self, ai, name, road, playable, debug, screen):
        module = __import__('controllers.{}.ai'.format(ai), fromlist=['ai'])
        self.road = road
        self.direction = np.array([1, 0], "float16")
        self.pos = np.array([100, 100], "float16")
        self.speed = np.array([0, 0], "float16")
        self.acc = 0
        self.screen = screen
        self.playable = playable
        self.name = name

        self.friction_x = .03
        self.friction_y = .01
        self.max_speed = 8
        self.rotation_speed = 5

        self.sensor_length = 300
        self.sensors = [
            {
                'angle': 0,
                'value': self.sensor_length,
                'vector': None,
                'point': None
            },
            {
                'angle': -30,
                'value': self.sensor_length,
                'vector': None,
                'point': None
            },
            {
                'angle': 30,
                'value': self.sensor_length,
                'vector': None,
                'point': None
            },
            {
                'angle': 90,
                'value': self.sensor_length,
                'vector': None,
                'point': None
            },
            {
                'angle': -90,
                'value': self.sensor_length,
                'vector': None,
                'point': None
            }
        ]

        self.debug = debug

        self.font_20 = pygame.font.SysFont("monospace", 20)
        self.color = (random.randint(0, 255),random.randint(0, 255), random.randint(0, 255))
        self.controller = module.Controller()
        self.controller.start(road)

    def draw(self):

        # Handling inputs
        inputs = None
        if (self.playable):
            keys = pygame.key.get_pressed()
            left = keys[pygame.K_LEFT]
            up = keys[pygame.K_UP]
            right = keys[pygame.K_RIGHT]
            down = keys[pygame.K_DOWN]
            inputs = [up, right, down, left]
        else:
            left = self.controller.left
            right = self.controller.right
            up = self.controller.up
            down = self.controller.down

        if (up):
            self.acc = .1
        elif (down):
            self.acc = -.1
        else:
            self.acc = 0

        if (right):
            self.direction = Utils.normalize(Utils.rotate(self.direction, -self.rotation_speed *Utils.length(self.speed) / self.max_speed))
        if (left):
            self.direction = Utils.normalize(Utils.rotate(self.direction, self.rotation_speed *Utils.length(self.speed) / self.max_speed))



        # Updating motion
        if (np.abs(np.dot(self.speed, self.direction)) <= self.max_speed):
            self.speed = np.add(self.speed, np.array([self.acc * self.direction[0], self.acc * self.direction[1]]))
        self.pos = np.add(self.speed, self.pos)

        # Friction
        self.speed = np.multiply(self.speed, 1 - self.friction_y)

        x_force = 1 - np.abs(np.dot( Utils.normalize(self.speed), Utils.normalize(self.direction) ))
        tangente = np.multiply(Utils.normalize(Utils.rotate(self.direction, 90)), self.friction_x * x_force * Utils.length(self.speed))
        if (np.dot(tangente, self.speed) > 0):
            tangente = Utils.rotate(tangente, 180)
        self.speed = np.add(self.speed, tangente)

        # Sensors
        for s in self.sensors:
            s['vector'] = s2_vector = Utils.rotate(np.multiply(Utils.normalize(self.direction), self.sensor_length), s['angle'])

            min = self.sensor_length
            point = None
            for l in self.road.lines:
                if (Utils.points_collide(l[0], l[1], self.pos, np.add(self.pos, s['vector']))):
                    inter = Utils.get_intersect( self.pos, np.add(s['vector'], self.pos), l[0], l[1] )
                    if (Utils.point_in_line(l[0], l[1], inter)):
                        if (Utils.distance(self.pos, inter) < min):
                            point = (int(inter[0]),int(inter[1]))
                            min = Utils.distance(self.pos, inter)
            s['value'] = min
            s['point'] = point

        # Drawing the white rect
        surface = pygame.Surface( (100, 100), pygame.SRCALPHA, 32 )
        pygame.draw.rect(surface, self.color, (50 - 10, 50 - 20, 20, 40))

        loc = surface.get_rect().center
        rot_surface = pygame.transform.rotate(surface, Utils.heading(self.direction))

        self.screen.blit(rot_surface, (self.pos[0] - rot_surface.get_rect().width / 2, self.pos[1] - rot_surface.get_rect().height / 2))

        label_name = self.font_20.render(self.name, 1, (255,255,255))
        self.screen.blit(label_name, (self.pos[0], self.pos[1] - 40))

        # Drawing vectors -- debug
        if (self.debug):
            pygame.draw.line(self.screen, (0, 255, 0), self.pos, np.add(self.pos, np.multiply(self.speed, 30)), 5)
            pygame.draw.line(self.screen, (0, 0, 255), self.pos, np.add(self.pos, np.multiply(self.direction, 30)), 5)
            pygame.draw.line(self.screen, (255, 0, 0), self.pos, np.add(self.pos, np.multiply(tangente, 300)), 5)

            # Drawing sensors
            for s in self.sensors:
                pygame.draw.line(self.screen, (255, 255, 0), self.pos, np.add(self.pos, s['vector']), 2)
                if (s['point'] != None):
                    pygame.draw.circle(self.screen, (255, 0, 0), s['point'], 5)

        self.controller.play(self.sensors, self.speed, self.direction, inputs)
