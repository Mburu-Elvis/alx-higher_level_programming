#!/usr/bin/python3
"""MOdule containing read_file function."""


def read_file(filename=""):
    """Function that reads a text file and prints it to stdout."""
    with open(filename, encoding="utf-8") as my_file:
        file_read = my_file.read()
        print(file_read)
