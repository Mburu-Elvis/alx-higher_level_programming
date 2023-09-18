#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
"""Module to test the Base class"""


class TestRectangle(unittest.TestCase):
    """TestBase class instatiation, uses Base.TestCase as base class"""


    def test_initMethod(self):
        """Method to test the Base class constructor"""
        rectangle = Rectangle(width=4, height=8, x=1, y=3)
        self.assertEqual(rectangle.width, 4)
        self.assertEqual(rectangle.height, 8)

    def test_init_with_no_id(self):
        """Method to test id"""
        rectangle1 = Rectangle(4, 8, 1, 3)
        rectangle2 = Rectangle(4, 8, 1, 3)
        self.assertNotEqual(rectangle1.id, rectangle2.id)

    def test_area(self):
        """Method to test area method of Recatngle class."""
        rect = Rectangle(3, 4, 2, 1)
        area = rect.area()
        self.assertEqual(area, 12)

    def test_str(self):
        """Method to test the __str__ method of Rectangle."""
        rect1 = Rectangle(2, 4, 5, 8, 2)
        rect2 = Rectangle(2, 4, 2, 8)
        rect3 = rect1
        self.assertNotEqual(rect1, rect2)
        self.assertEqual(rect1, rect3)

if __name__ == "__main__":
    unittest.main()
