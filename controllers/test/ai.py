import sys
sys.path.append('../..')
from AI import AI

class Controller(AI):

    def start(self, map):
        print("Controller test")
        self.up = True

    def play(self, sensors, speed, heading, inputs):
        pass
