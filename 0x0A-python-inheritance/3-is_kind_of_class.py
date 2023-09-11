#!/usr/bin/python3
"""Module containing is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Function to check if obj is an instance of a_class of it's Base"""
    if isinstance(obj, a_class):
        return True
    return False
