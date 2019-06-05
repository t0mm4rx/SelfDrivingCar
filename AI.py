"""
    This is the controller interface. Don't edit this.
    Each car has a controller that extends this abstract class.
    start is called once at the beginning of the race.
    play is called every frames.
"""

class AI:

    def __init__(self):
        self.up = False
        self.left = False
        self.down = False
        self.right = False

    def play(self, sensors, speed, heading, inputs):
        pass

    def start(self, map):
        pass
