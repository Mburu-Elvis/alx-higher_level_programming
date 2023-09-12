#!/usr/bin/python3
"""Module containing write_file function."""


def write_file(filename="", text=""):
    with open(filename, 'w') as myfile:
        myfile.write(text)
        return len(text)
