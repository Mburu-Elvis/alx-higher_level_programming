#!/usr/bin/python3
"""Module containing append_write function"""


def append_write(filename="", text=""):
    """Function that appends string to a file"""
    with open(filename, 'a', encoding="UTF8") as myfile:
        myfile.write(text)
        return len(text)