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
    w1list = []
    w2list = []
    w3list = []
    w4list = []
    w5list = []
    w6list = []
    w7list = []
    for _ in range(5):
        w1 = Walker(0, 1)
        while not w1.position == w1.home:
            w1.move()
        w1list.append(w1.get_steps())

        w2 = Walker(0, 2)
        while not w2.position == w2.home:
            w2.move()
        w2list.append(w2.get_steps())

        w3 = Walker(0, 5)
        while not w3.position == w3.home:
            w3.move()
        w3list.append(w3.get_steps())

        w4 = Walker(0, 10)
        while not w4.position == w4.home:
            w4.move()
        w4list.append(w4.get_steps())

        w5 = Walker(0, 20)
        while not w5.position == w5.home:
            w5.move()
        w5list.append(w5.get_steps())

        w6 = Walker(0, 50)
        while not w6.position == w6.home:
            w6.move()
        w6list.append(w6.get_steps())

        w7 = Walker(0, 100)
        while not w7.position == w7.home:
            w7.move()
        w7list.append((w7.get_steps()))

    print("Distance:   1 -> Path lengths: {0}".format(w1list))
    print("Distance:   2 -> Path lengths: {0}".format(w2list))
    print("Distance:   5 -> Path lengths: {0}".format(w3list))
    print("Distance:   10 -> Path lengths: {0}".format(w4list))
    print("Distance:   20 -> Path lengths: {0}".format(w5list))
    print("Distance:   50 -> Path lengths: {0}".format(w6list))
    print("Distance:   100 -> Path lengths: {0}".format(w7list))
