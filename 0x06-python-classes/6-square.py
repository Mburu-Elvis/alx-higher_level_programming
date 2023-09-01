#!/usr/bin/python3
"""Module defining a Square class"""


class Square:
    """Definition of the attributes of a square"""

    def __init__(self, size=0, position=0):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """__size attribute getter."""
        return (self.__size)
    @property
    def position(self):
        """__position attibute getter."""
        return (self.__size)

    @position.setter
    def position(self, value):
        """__position attribute setter."""
        if len(position) != 2 or not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        """Prints the square with #"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for k in range(self.__size):
                print("#", end="")
            print()
