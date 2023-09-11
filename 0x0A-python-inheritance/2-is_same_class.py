#!/usr/bin/python3
"""A module that contains is_name_class"""


def is_same_class(obj, a_class):
    """function that returns True if the object is an instance of a class"""
    if type(obj) is a_class:
        return True
    else:
        return False
