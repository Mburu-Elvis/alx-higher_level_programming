#!/usr/bin/python3
"""Module defining a Square class"""


class Square:
    """Definition of the attributes of a square"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """__size attribute getter."""
        return (self.__size)

    @size.setter
    def size(self, size):
        """__size attribute setter."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size mut be >= 0")
        self.__size = size

    def area(self):
        """returns the are of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square with \#"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for k in range(self.__size):
                print("#", end="")
            print()
