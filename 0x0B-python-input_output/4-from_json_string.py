#!/usr/bin/python3
"""Module containing from_json_string function."""
import json


def from_json_string(my_str):
    """Function that returns an object rep in JSON"""
    return json.loads(my_str)
