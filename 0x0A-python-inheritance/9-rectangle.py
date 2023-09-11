#!/usr/bin/python3
"""Module containing class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """instantiation of the object."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return (self.__width * self.__height)

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
