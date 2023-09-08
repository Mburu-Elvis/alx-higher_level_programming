#!/usr/bin/python3
"""Module containing the print_square function."""


def print_square(size):
    """function that prints a square with character '#'."""
    if not isinstance(size, int):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be  >= 0")
    for length in range(size):
        for width in range(size):
            print("#", end="")
        print()
