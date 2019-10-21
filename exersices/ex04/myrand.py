# -*- coding: utf-8 -*-

__author__ = 'sebastian kihle'
__email__ = 'sebaskih@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        self.seed = seed
        self.counter = 0
        self.r = [seed]

    def rand(self):
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
