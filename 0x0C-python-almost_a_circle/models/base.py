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

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = f"{cls.__name__}.json"
        dict_list = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(dict_list)
        with open(filename, 'w') as file:
            file.write(json_string)
