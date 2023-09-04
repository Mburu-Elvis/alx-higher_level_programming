#!/usr/bin/python3
"""Module defining class Rectangle"""


class Rectangle:
    """Class definition"""
    def __init__(self, width=0, height=0):
        """the object instatiation function."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """the width getter function."""
        return self.__width

    @width.setter
    def width(self, value):
        """the width setter function."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The height getter function."""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
