#!/usr/bin/python3
"""Module containing class Rectangle."""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle that inherits from Base."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for class Rectangle."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter."""
        return self.__width

    @width.setter
    def width(self, width):
        """setter to attribute width."""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height getter."""
        return self.__height

    @height.setter
    def height(self, height):
        """setter to height attribute."""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x getter."""
        return self.__x

    @x.setter
    def x(self, x):
        """setter to  x attribute."""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter."""
        return self.__y

    @y.setter
    def y(self, y):
        """setter to y attribute."""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """method to calculate the area of the rectangle."""
        return (self.width * self.height)

    def display(self):
        """Method to display the rectangle."""
        for i in range(self.height):
            for k in range(self.width):
                print("#", end='')
            print()

    def __str__(self):
        """the str method of Rectangle class."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
