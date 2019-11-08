# -*- coding: utf-8 -*-

__author__ = 'sebastian kihle'
__email__ = 'sebaskih@nmbu.no'

from walker_sim import Walker, Simulation


class BoundedWalker(Walker):
    def __init__(self, start, home, left_limit, right_limit):
        """
        Initialise the walker

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        super().__init__(start, home)
        self.start = start
        self.home = home
        self.left_limit = left_limit
        self.right_limit = right_limit

    def single_run(self):
        while not self.is_at_home:
            self.move()
            if self.get_position() < self.left_limit:
                self.position += 1
            if self.get_position() > self.right_limit:
                self.position -= 1
        return self.get_steps()


class BoundedSimulation(Simulation):
    def __init__(self, start, home, seed, left_limit, right_limit):
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
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        super().__init__(start, home, seed)
        self.start = start
        self.home = home
        self.seed = seed
        self.left_limit = left_limit
        self.right_limit = right_limit

    def single_walk(self):

        f = BoundedWalker(self.start, self.home, self.right_limit,
                          self.left_limit)
        while not f.is_at_home():
            f.move()
            if f.get_position() < self.left_limit:
                f.position += 1
            if f.get_position() > self.right_limit:
                f.position -= 1
        return f.get_steps()

    def run_simulation(self, num_walks):
        walk_list = []
        for _ in range(num_walks):
            walk_list.append(self.single_walk())
        return walk_list


if __name__ == "__main__":
    left_boundaries = [0, -10, -100, -1000, -10000]

    for value in left_boundaries:
        w = BoundedSimulation(0, 20, 0, value, 20)
        print("Left boundary {0} with these results:".format(value),
              w.run_simulation(20))
