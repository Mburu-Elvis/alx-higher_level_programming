#!/usr/bin/python3
import unittest
import sys
sys.path.append('..')
from models.base import Base
from models.rectangle import Rectangle
"""Module to test the Base class"""


class TestBase(unittest.TestCase):
    """TestBase class instatiation, uses Base.TestCase as base class"""


    def test_initMethod(self):
        """Method to test the Base class constructor"""
        obj = Base(id=5)
        self.assertEqual(obj.id, 5)

    def test_init_with_no_id(self):
        """Method to test id"""
        obj1 = Base()
        obj2 = Base()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_nb_objects_increment(self):
        """Method to test nb_objects increment"""
        obj = Base()
        self.assertEqual(obj.id, Base._Base__nb_objects)

    def test_to_json_string(self):
        """Method to test to_json_string method of class Base."""
        obj = Base()
        my_str = [{"a": 1, "b": 2}, {"c": 3, "d": 4}]
        str1 = obj.to_json_string(my_str)
        self.assertEqual(my_str, my_str)

    def test_create(self):
        """method to test create method of class Base"""
        dict1 =  {"width": 3, "height": 10}
        rect = Rectangle.create(**dict1)
        self.assertEqual(rect.width, 3)

    def test_load_from_file(self):
        """method to test load_from_file metho of Base class."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles = [r1, r2]
        Rectangle.save_to_file(list_rectangles)
        rect = Rectangle.load_from_file()
        self.assertEqual(rect[0].id , r1.id)

    def test_save_to_file(self):
        """method to test save_to_file method Base class."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        rect = Rectangle.load_from_file()
        self.assertEqual(rect[0].height, r1.height)

    def test_json_string(self):
        """method to test from_json_string"""
        x = [1, 3, 4]
        x_str = Base.to_json_string(x)
        y = Base.from_json_string(x_str)
        self.assertEqual(x, y)

if __name__ == "__main__":
    unittest.main()
