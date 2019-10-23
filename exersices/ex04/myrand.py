# -*- coding: utf-8 -*-

__author__ = 'sebastian kihle'
__email__ = 'sebaskih@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        self.seed = seed
        self.counter = 0
        self.r = [seed]

    def rand(self):
        """Adds element to the list, so that the list always is long enough"""
        self.r.append("placeholder value")
        a = 7**5
        m = 2**31 - 1
        self.r[self.counter + 1] = a * self.r[self.counter] % m
        self.counter += 1
        return self.r[self.counter]


class ListRand:
    def __init__(self, numbers):
        self.numbers = numbers
        self.counter = -1

    def rand(self):
        self.counter += 1
        if self.counter > len(self.numbers) - 1:
            raise RuntimeError
        return self.numbers[self.counter]


if __name__ == '__main__':
    lc = LCGRand(125)
    print("First random number by LCG: {0}".format(lc.rand()))
    print("Second random number by LCG: {0}".format(lc.rand()))
    print("Third random number by LCG: {0}".format(lc.rand()))

    lr = ListRand([2, 7, 19, 3])
    print("First random number by list of numbers: {0}".format(lr.rand()))
    print("Second random number by list of numbers: {0}".format(lr.rand()))
    print("Third random number by list of numbers: {0}".format(lr.rand()))
