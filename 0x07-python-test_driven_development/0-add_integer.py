#!/usr/bin/python3
"""Module defining function add_integer.

>>> print(add_integer(2, 4))
6
"""


def add_integer(a, b=98):
    """function to add two integers.

    default value of b is 98"""
    try:
        if isinstance(a, float):
            a = int(a)
        if isinstance(b, float):
            b = int(b)
        if not isinstance(a, int):
            raise TypeError('a must be an integer')
        if not isinstance(b, int):
            raise TypeError('b must be an integer')
        return (a + b)
    except Exception as e:
        if a is None:
            raise ValueError("a must be an integer")
        else:
            raise ValueError("b must be an integer")
