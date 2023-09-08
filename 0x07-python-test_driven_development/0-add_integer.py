#!/usr/bin/python3
"""Module defining function add_integer.

>>> print(add_integer(2, 4))
6
"""


def add_integer(a, b=98):
    """function to add two integers.

    defualt value of b is 98"""
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError(f'{a} must be an integer')
    if not isinstance(b, int):
        raise TypeError(f'{b} must be an integer')
    return (a + b)
