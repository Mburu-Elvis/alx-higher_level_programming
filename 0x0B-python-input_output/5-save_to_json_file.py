#!/usr/bin/python3
"""Module containing save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """writes 'my_obj' to a text file"""
    with open(filename, 'w', encoding='UTF8') as myfile:
        json.dump(my_obj, myfile)