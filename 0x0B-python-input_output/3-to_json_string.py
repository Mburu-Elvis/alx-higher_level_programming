#!/usr/bin/python3
"""Module containing to_json_string function."""
import json


def to_json_string(my_obj):
    return json.dumps(my_obj, sort_keys=True)