#!/usr/bin/python3
"""Module containing to_json_string function."""
import json


def to_json_string(my_obj):
    """function that returns a string to json"""
    return json.dumps(my_obj, sort_keys=True)
