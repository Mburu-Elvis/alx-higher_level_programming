#!/usr/bin/python3

"""Defines a Rectangle class."""


class Rectangle:
    """Defining the Rectangle Class."""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle.
        Args:
            width(int): The width of the new rectangle.
            height(int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height Getter."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Return the printable string representation of the Rectangle.

        Represents the Rectangle with '#'.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width] * self.height)

    def __repr__(self):
        """Return a string representation of the rectangle object."""
        rect = "Rectangle("+ str(self.__width) + ","
        rect = rect + str(self.__height) + ")"
        return rect

