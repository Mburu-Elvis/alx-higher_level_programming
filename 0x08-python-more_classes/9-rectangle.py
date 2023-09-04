#!/usr/bin/python3
"""Module defining class Rectangle"""


class Rectangle:
    """Class definition"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """the object instatiation function."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """function to calculate the area of the rectangle."""
        return (self.width * self.height)

    def perimeter(self):
        """function to calculate the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return (0)
        return (2 * (self.width) + 2 * (self.height))

    def __str__(self):
        """str function"""
        if self.height == 0 or self.width == 0:
            return ""
        rect = ""
        for i in range(self.height):
            for k in range(self.width):
                rect += str(self.print_symbol)
            if i != self.height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        """repr function"""
        return f"{type(self).__name__}({self.width}, {self.height})"

    def __del__(self):
        """destructor"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 > area_2:
            return rect_1
        elif area_2 > area_1:
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        width = size
        height = size
        return cls(width, height)
