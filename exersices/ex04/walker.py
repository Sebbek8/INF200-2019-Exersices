# -*- coding: utf-8 -*-

__author__ = 'sebastian kihle'
__email__ = 'sebaskih@nmbu.no'

import random


class Walker:
    def __init__(self, startpoint, home):
        self.startpoint = startpoint
        self.home = home
        self.steps = 0
        self.position = startpoint

    def move(self):
        step = random.randint(1, 2)
        if step == 2:
            step = -1
        self.steps += 1
        self.position += step
        self.is_at_home()
        return self.get_steps()

    def is_at_home(self):
        if self.position == self.home:
            return True
        else:
            return False

    def get_position(self):
        return self.position

    def get_steps(self):
        return self.steps

if __name__ == "__main__":
    while not self.position == self.home: