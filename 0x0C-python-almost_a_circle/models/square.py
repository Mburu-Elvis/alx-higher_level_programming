#!/usr/bin/python3
"""Module containing the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square whose base class is Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """class Square constructor."""
        super().__init__(id=id, width=size, height=size, x=x, y=y)

    def __str__(self):
        """str method for class Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """method to get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """seter method for the width and height."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            return ValueError("size must be > 0")
        self.__width = value
        self.__height = value
