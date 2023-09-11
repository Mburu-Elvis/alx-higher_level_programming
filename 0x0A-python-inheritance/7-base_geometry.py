#!/usr/bin/python3
"""Module thats contains BaseGeometry class"""


class BaseGeometry:
    """Class BaseGeometry"""
    def area(self):
        """method to calculate area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method to validates value"""
        if not isinstance(value, int) or type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
