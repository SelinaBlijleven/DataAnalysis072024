"""
list_building.py

Often, we want to build lists from other objects. This file shows a few common applications.
"""


def list_from_string(txt: str) -> list:
    """
    List from string
    :param txt:     Text to turn into a list
    :return:        List of all words
    """
    return txt.split()


def square_list(numbers: list) -> list:
    """
    Take a list and square each number in the list. This can easily be adapted
    to perform other tasks for each element in a list.

    :param numbers:
    :return:
    """
    squares = []

    for n in numbers:
        squares.append(n * n)

    return squares


def square_list_alt(numbers: list) -> list:
    """ Square all numbers in a list using list comprehension """
    # List comprehension
    return [x ** 2 for x in numbers]
