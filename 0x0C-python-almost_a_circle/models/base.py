#!/usr/bin/python3
"""Module containing the base class"""
import json


class Base:
    """The Base class block"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """method that returns the JSON string rep of list_dictionaries."""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
