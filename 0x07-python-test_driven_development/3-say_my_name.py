#!/usr/bin/python3
"""Module having say_my_name."""


def say_my_name(first_name, last_name=""):
    """function that prints My name is <first_name><last_name>"""
    if not isinstance(first_name, str) or first_name == None:
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str) or last_name == None:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
