"""
    Empty controller.
    This controller does nothing, it's the default template.
    To control the car, you can change self.up, self.right, self.left and self.down in play 
"""

import sys
sys.path.append('../..')
from AI import AI

class Controller(AI):

    def start(self, map):
        print("Controller empty")

    def play(self, sensors, speed, heading, inputs):
        print(heading)
