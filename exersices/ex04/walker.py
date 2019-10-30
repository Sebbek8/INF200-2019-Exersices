# -*- coding: utf-8 -*-

__author__ = 'sebastian kihle'
__email__ = 'sebaskih@nmbu.no'

import random


class Walker:
    def __init__(self, startpoint, home):
        self.startpoint = startpoint
        self.home = home
        # Starts with 0 steps
        self.steps = 0
        self.position = startpoint

    def move(self):
        """Uses randint to have 50% chance of moving backwards and forwards"""
        step = random.randint(1, 2)
        if step == 2:
            step = -1
        self.steps += 1
        # Counts the total amount of steps
        self.position += step
        self.is_at_home()
        return self.get_steps()

    def is_at_home(self):
        """Check if person is at home"""
        if self.position == self.home:
            return True
        else:
            return False

    def get_position(self):
        """Gets current position"""
        return self.position

    def get_steps(self):
        """Gets current amount of steps"""
        return self.steps


if __name__ == "__main__":

    # List of all the distances
    distances = [1, 2, 5, 10, 20, 50, 100]

    # Double for-loop to do each distance 5 times
    for distance in distances:
        # Defines temporary list that contains the 5 values, and resets
        templist = []
        for _ in range(5):
            w = Walker(0, distance)
            # Walk until you are home
            while not w.is_at_home():
                w.move()
            # Add the steps to the temporary list
            templist.append(w.get_steps())
        print("Distance:   {0} -> Path lengths: {1}".format(distance,
                                                            templist))
