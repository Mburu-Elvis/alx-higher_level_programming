#!/usr/bin/python3

"""Module defining a square."""


class Square:
    """Defines the structure of a square."""

    def __init__(self, size=0):
        """Object instantiation during creation."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
