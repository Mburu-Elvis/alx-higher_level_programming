#!/usr/bin/python3
"""Module containing the lookup function."""


def lookup(obj):
    """function that returns the list of attributes and method in an object"""
    return dir(obj)
