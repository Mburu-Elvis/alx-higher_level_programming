#!/usr/bin/python3
"""Module containing class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """object instantiation."""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns the area of the square"""
        return (self.__size * self.__size)

    def __str__(self):
        """magic method to print the object"""
        return f"[Square] {self.__size}/{self.__size}"
