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
        if no_args >= 1:
            self.id = args[0]
        if no_args >= 2:
            self.size = args[1]
        if no_args >= 3:
            self.x = args[2]
        if no_args >= 4:
            self.y = args[3]

    def to_dictionary(self):
        """method to return a dictionary of Square attributes"""
        my_dict = {}
        my_dict['id'] = self.id
        my_dict['size'] = self.size
        my_dict['x'] = self.x
        my_dict['y'] = self.y
        return my_dict
