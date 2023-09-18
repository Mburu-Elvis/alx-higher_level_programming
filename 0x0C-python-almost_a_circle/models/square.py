#!/usr/bin/python3
"""Module containing the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square whose base class is Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """class Square constructor."""
        super().__init__(size, size, x, y, id=id)
        self.size = size

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
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update method that assign attributes."""
        if not (args):
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
            return
        no_args = len(args)
        if no_args == 1:
            self.id = args[0]
        elif no_args == 2:
            self.id = args[0]
            self.width = args[1]
        elif no_args == 3:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
        elif no_args == 4:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
        else:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
