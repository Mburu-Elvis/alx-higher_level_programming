#!/usr/bin/python3
"""Module defining class Rectangle"""


class Rectangle:
    """Class definition"""
    def __init__(self, width=0, height=0):
        """the object instatiation function."""
        if not isinstance(height, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """the width getter function."""
        return self.__width

    @width.setter
    def width(self, value):
        """the width setter function."""
        self.__width = value

    @property
    def height(self):
        """The height getter function."""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle."""
        self.__height = value
