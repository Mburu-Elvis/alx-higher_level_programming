#!/usr/bin/python3
"""Module containing class MyInt"""


class MyInt(int):
    """class definition"""
    def __eq__(self, other):
        """inversion of =="""
        return super().__ne__(other)

    def __ne__(self, other):
        """inversion of !="""
        return super().__eq__(other)
