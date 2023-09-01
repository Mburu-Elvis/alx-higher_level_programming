#!/usr/bin/python3
"""A module containing a Square class."""


class Square:
    """Definition of the class square."""

    def __init__(self, size):
        """Object initialzation at creation."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return (self.__size * self.__size)
