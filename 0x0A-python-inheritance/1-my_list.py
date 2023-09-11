#!/usr/bin/python3
"""Module containing MyList class"""


class MyList(list):
    """A class MyList that inherits from list"""
    def print_sorted(self):
        """public the lists a sorted list"""
        print(sorted(self))
