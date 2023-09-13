#!/usr/bin/python3
"""Module containing load_from_json_file."""
import json


def load_from_json_file(filename):
    """creates an object from 'JSON' file"""
    with open(filename, 'r', encoding="UTF8") as myfile:
        return json.load(myfile)
