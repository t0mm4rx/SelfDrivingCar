"""
    This is the road class. Don't edit this.
    It loads the given file, and calculates the bounds of the road.
    It also renders the road.
"""

import numpy as np
import pygame
import json
import Utils

class Road():

    def __init__(self, filename, screen):
        self.load_file(filename)
        self.screen = screen

    def load_file(self, filename):
        file = json.loads(open('maps/{}'.format(filename)).read())
        self.points = file['points']
        self.road_width = file['width']

        self.bounds = []

        for i in range(len(self.points)):
            if (i == 0):
                p1 = self.points[len(self.points) - 1]
            else:
                p1 = self.points[i - 1]
            p2 = self.points[i]
            if (i == len(self.points) - 1):
                p3 = self.points[0]
            else:
                p3 = self.points[i + 1]

            v1 = Utils.normalize(np.array([ p2[0] - p1[0], p2[1] - p1[1] ]))
            v2 = Utils.normalize(np.array([ p3[0] - p2[0], p3[1] - p2[1] ]))
            v3 = np.multiply(Utils.rotate(Utils.normalize( np.add(v1, v2) ), 90), self.road_width)
            v4 = np.multiply(Utils.rotate(Utils.normalize( np.add(v1, v2) ), -90), self.road_width)

            self.bounds.append([ int(p2[0] + v3[0]), int(p2[1] + v3[1]) ])
            self.bounds.append([ int(p2[0] + v4[0]), int(p2[1] + v4[1]) ])

        self.polygons = []
        for i in range(len(self.points)):
            a = i * 2
            self.polygons.append([
                self.bounds[a],
                self.bounds[a + 1],
                self.bounds[(a + 3) % len(self.bounds)],
                self.bounds[(a + 2) % len(self.bounds)],
            ])

        self.lines = []
        for p in self.polygons:
            self.lines.append([
                p[0],
                p[3]
            ])
            self.lines.append([
                p[1],
                p[2]
            ])

    def draw(self):

        for p in self.polygons:
            pygame.draw.polygon(self.screen, (100, 100, 200), p)

        for i in range(len(self.points)):
            if (i == 0):
                p1 = self.points[len(self.points) - 1]
            else:
                p1 = self.points[i - 1]
            p2 = self.points[i]
            pygame.draw.line(self.screen, (255, 255, 255), p1, p2)
            pygame.draw.circle(self.screen, (255, 255, 255), p1, 5)

        for b in self.bounds:
            pygame.draw.circle(self.screen, (255, 255, 255), b, 5)

        for l in self.lines:
            pygame.draw.line(self.screen, (255, 255, 255), l[0], l[1])
