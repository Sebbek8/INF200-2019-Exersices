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


class Simulation:
    def __init__(self, start, home, seed):
        """
        Initialise the simulation

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        seed : int
            Random generator seed
        """
        self.start = start
        self.home = home
        self.seed = random.seed(seed)

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """
        w = Walker(self.start, self.home)
        while not w.is_at_home():
            w.move()
        return w.get_steps()

    def run_simulation(self, num_walks):
        """
        Run a set of walks, returns list of number of steps taken.

        Arguments
        ---------
        num_walks : int
            The number of walks to simulate

        Returns
        -------
        list[int]
            List with the number of steps per walk
        """
        walk_list = []
        for _ in range(num_walks):
            walk_list.append(self.single_walk())
        return walk_list


if __name__ == "__main__":
    for _ in range(2):
        sim1 = Simulation(0, 10, 12345)
        sim2 = Simulation(10, 0, 12345)
        print(sim1.run_simulation(20))
        print(sim2.run_simulation(20))

    sim3 = Simulation(0, 10, 54321)
    sim4 = Simulation(10, 0, 54321)
    print(sim3.run_simulation(20))
    print(sim4.run_simulation(20))
