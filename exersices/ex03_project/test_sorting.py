# -*- coding: utf-8 -*-

__author__ = 'sebastian kihle'
__email__ = 'sebaskih@nmbu.no'


def bubble_sort(data):

    """ Makes list of the data """
    the_list = list(data)

    length = len(the_list)
    """ Iterate from the start to the back,
        then go to back - 1 """
    while length >= 1:
        innerloop(the_list)
        length -= 1

    return the_list


def innerloop(the_list):

    """ Compares values, and changes postions if they
        are in wrong order """
    for index in range(len(the_list)-1):
        if the_list[index] > the_list[index+1]:
            smaller = the_list[index+1]
            bigger = the_list[index]
            the_list[index] = smaller
            the_list[index+1] = bigger

    return the_list


def test_empty():
    """Test that the sorting function works for empty list"""
    assert bubble_sort([]) == [], "List should be empty"


def test_single():
    """Test that the sorting function works for single-element list"""
    assert len(bubble_sort([1])) == 1, "length of list should be one"
    assert bubble_sort([3]) == [3], "should return same value as input"


def test_sorted_is_not_original():
    """
    Test that the sorting function returns a new object.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now sorted_data shall be a different object than data,
    not just another name for the same object.
    """
    assert bubble_sort([2, 3, 1]) != [2, 3, 1], "list should not be unchanged"


def test_original_unchanged():
    """
    Test that sorting leaves the original data unchanged.

    Consider

    data = [3, 2, 1]
    sorted_data = bubble_sort(data)

    Now data shall still contain [3, 2, 1].
    """
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert data == [3, 2, 1], "input list should be unchanged"
    assert data != sorted_data, "input should not be equal to output for " \
                                "unsorted list."


def test_sort_sorted():
    """Test that sorting works on sorted data."""
    data = [3, 1, 2]
    new_data = bubble_sort(data)
    newest_data = bubble_sort(new_data)
    assert new_data == newest_data, "sorting the same data twice should work"


def test_sort_reversed():
    """Test that sorting works on reverse-sorted data."""
    assert bubble_sort([3, 2, 1]) == [1, 2, 3], "a reversed list should be " \
                                                "sorted in acending order"


def test_sort_all_equal():
    """Test that sorting handles data with identical elements."""
    assert bubble_sort([5, 5, 5, 5]) == [5, 5, 5, 5]


def test_sorting():
    """
    Test sorting for various test cases.

    This test case should test sorting of a range of data sets and
    ensure that they are sorted correctly. These could be lists of
    numbers of different length or lists of strings.
    """
    assert bubble_sort([3, 2, 1]) == [1, 2, 3], "doesnt work for test list 1"

    assert bubble_sort([5, 2, 9, 11]) == [2, 5, 9, 11], "doesnt work for " \
                                                        "test list 2"

    assert bubble_sort([37, 417, -3, 83, 44]) == [-3, 37, 44, 83, 417], \
        "does not work for test list 3"

    assert bubble_sort(["b", "c", "a"]) == ["a", "b", "c"], \
        "function should work with both number and strings. test list 4 failed"
