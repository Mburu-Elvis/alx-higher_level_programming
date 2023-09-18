#!/usr/bin/python3
import unittest
import sys
sys.path.append('..')
from models.base import Base
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

if __name__ == "__main__":
    unittest.main()
