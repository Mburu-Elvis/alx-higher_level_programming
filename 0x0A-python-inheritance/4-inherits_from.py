#!/usr/bin/python3
"""Module that contains inherits_from function"""


def inherits_from(obj, a_class):
    """functions that checks if object is an instance of class"""
    if isinstance(type(obj), a_class) or not type(obj) is  a_class:
        return True
    return False
