# -*- coding: utf-8 -*-

__author__ = 'sebastian kihle'
__email__ = 'sebaskih@nmbu.no'


def median(data):
    """
    Returns median of data.

    :param data: An iterable of containing numbers
    :return: Median of data

    Source:
    https://github.com/yngvem/INF200-2019-Exercises/blob/master/exersices/
    ex03.rst
    """

    sdata = sorted(data)
    n = len(sdata)
    if len(data) == 0:
        raise ValueError

    return (sdata[n//2] if n % 2 == 1
            else 0.5 * (sdata[n//2 - 1] + sdata[n//2]))


def test_single_value():
    assert median([1]) == 1, "should return the single value for a single " \
                             "value list"


def test_correct_median():
    assert median([1, 2, 3]) == 2, "failed test list 1"

    assert median([2, 5, 9, 11]) == 7, "failed test list 2"

    assert median([12, 9, 6, 3]) == 7.5, "failed test list 3"

    assert median([19, 3, 7, 4, 11, ]) == 7, "failed test list 4"


def test_original_data_unchanged():
    data = [1, 5, 7, 9, 15]
    median(data)
    assert data == [1, 5, 7, 9, 15]


def test_tuples_and_lists():
    liste = [1, 4, 7]
    assert median(tuple(liste)) == 4
    assert median(liste) == 4


test_tuples_and_lists()


def test_valueerror():
    try:
        median([])
    except ValueError:
        pass
    else:
        assert False
