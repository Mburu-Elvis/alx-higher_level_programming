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

if __name__ == "__main__":
    unittest.main()
