import numpy as np
import pygame
import Utils

class Car():

    def __init__(self, ai, screen):
        self.direction = np.array([1, 0], "float16")
        self.pos = np.array([100, 100], "float16")
        self.speed = np.array([0, 0], "float16")
        self.acc = 0
        self.screen = screen

        self.friction_x = .03
        self.friction_y = .01
        self.max_speed = 8
        self.rotation_speed = 5

        self.debug = False

    def draw(self):

        # Handling inputs
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_UP]):
            self.acc = .1
        elif (keys[pygame.K_DOWN]):
            self.acc = -.1
        else:
            self.acc = 0

        if (keys[pygame.K_RIGHT]):
            self.direction = Utils.normalize(Utils.rotate(self.direction, -self.rotation_speed * Utils.length(self.speed) / self.max_speed))
        if (keys[pygame.K_LEFT]):
            self.direction = Utils.normalize(Utils.rotate(self.direction, self.rotation_speed * Utils.length(self.speed) / self.max_speed))


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


        # Drawing the white rect
        surface = pygame.Surface( (100, 100), pygame.SRCALPHA, 32 )
        pygame.draw.rect(surface, (255, 255, 255), (50 - 10, 50 - 20, 20, 40))

        loc = surface.get_rect().center
        rot_surface = pygame.transform.rotate(surface, Utils.heading(self.direction))

        self.screen.blit(rot_surface, (self.pos[0] - rot_surface.get_rect().width / 2, self.pos[1] - rot_surface.get_rect().height / 2))
        pygame.display.flip()

        # Drawing vectors -- debug
        if (self.debug):
            pygame.draw.line(self.screen, (0, 255, 0), self.pos, np.add(self.pos, np.multiply(self.speed, 30)), 5)
            pygame.draw.line(self.screen, (0, 0, 255), self.pos, np.add(self.pos, np.multiply(self.direction, 30)), 5)
            pygame.draw.line(self.screen, (255, 0, 0), self.pos, np.add(self.pos, np.multiply(tangente, 300)), 5)
