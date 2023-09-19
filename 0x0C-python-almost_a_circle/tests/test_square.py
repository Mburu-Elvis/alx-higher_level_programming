#!/usr/bin/python3
"""Modeule containing TestSquare class."""
from models.square import Square
import unittest


class TestSquare(unittest.TestCase):
    """Class containing test cases for class Square."""
    def test_init_method(self):
        """method to test Square.__init__ method."""
        square = Square(size=4, x=3, y=4, id=9)
        self.assertEqual(square.height, 4)

    def test_update(self):
        """method to test update metho of Square class."""
        square = Square(size=2, x=3, y=4, id=1)
        square.update(size=4)
        self.assertTrue(square.size, 4)
