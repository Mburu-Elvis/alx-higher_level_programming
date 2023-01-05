#!/usr/bin/python3
"""Defining a Rectangle Propertied."""


class Rectangle:
    """Defining the Rectangle Class."""
    def __init__(self, width=0, height=0):
        """Init function."""
        self.width = width
        self.height = height
    @property
    def width(self):
        """width getter."""
        return self._width
    @width.setter
    def width(self, value):
        """Width Setter."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
        """Height Getter."""    
        return self._height
    @height.setter
    def height(self, value):
        """Height Setter."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("heigth must be >= 0")
        self.__height = value
