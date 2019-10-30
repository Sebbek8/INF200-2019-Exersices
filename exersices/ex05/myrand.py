# -*- coding: utf-8 -*-

__author__ = 'sebastian kihle'
__email__ = 'sebaskih@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        self.seed = seed
        self.counter = 0
        self.r = [seed]

    def rand(self):
        """Adds element to the list, so that the list always is long enough
        and calculated the LCG"""
        self.r.append("placeholder value")
        a = 7**5
        m = 2**31 - 1
        self.r[self.counter + 1] = a * self.r[self.counter] % m
        self.counter += 1
        return self.r[self.counter]

    def random_sequence(self, length):
        return RandIter(self, length)

    def infinite_random_sequence(self):
        """
        Generate an infinite sequence of random numbers.

        Yields
        ------
        int
            A random number.
        """
        while True:
            yield self.rand()


class RandIter:
    def __init__(self, random_number_generator, length):
        """

        Arguments
        ---------
        random_number_generator :
            A random number generator with a ``rand`` method that
            takes no arguments and returns a random number.
        length : int
            The number of random numbers to generate
        """
        self.generator = random_number_generator
        self.length = length
        self.num_generated_numbers = None

    def __iter__(self):
        """
        Initialise the iterator.

        Returns
        -------
        self : RandIter

        Raises
        ------
        RuntimeError
            If iter is called twice on the same RandIter object.
        """
        if self.num_generated_numbers is not None:
            raise RuntimeError()
        self.num_generated_numbers = 0
        return self

    def __next__(self):
        """
        Generate the next random number.

        Returns
        -------
        int
            A random number.

        Raises
        ------
        RuntimeError
            If the ``__next__`` method is called before ``__iter__``.
        StopIteration
            If ``self.length`` random numbers are generated.
        """
        if self.num_generated_numbers is None:
            raise RuntimeError()
        if self.num_generated_numbers == self.length:
            raise StopIteration()

        self.num_generated_numbers += 1
        return self.generator.rand()


"""
random_number_generator = LCGRand(1)
for rand in random_number_generator.random_sequence(10):
    print(rand)

i = 0
while i < 100:
    rand = random_number_generator.infinite_random_sequence()
    print(f'The {i}-th random number is {rand}')
    i += 1
"""
