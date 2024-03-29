#!/usr/bin/python3
"""Module containing class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square definition."""
    def __init__(self, size):
        """object instantiation."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns the area of the square"""
        return (self.__size * self.__size)
