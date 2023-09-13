#!/usr/bin/python3
"""Module containing write_file function."""


def write_file(filename="", text=""):
    """function that writes 'text' to 'filename'."""
    with open(filename, 'w') as myfile:
        myfile.write(text)
        return len(text)
