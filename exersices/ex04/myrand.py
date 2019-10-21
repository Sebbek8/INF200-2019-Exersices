# -*- coding: utf-8 -*-

__author__ = 'sebastian kihle'
__email__ = 'sebaskih@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        self.seed = seed

    def rand(self):
        r = self.seed
        a = 7**5
        m = 2**31 - 1
        r = a * r % m
        return r


class ListRand:
    def __init__(self, numbers):
        self.numbers = numbers

    def rand(self):
        return self.numbers.pop()
