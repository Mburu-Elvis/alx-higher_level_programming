#!/usr/bin/python3
"""MOdule containing read_file function."""


def read_file(filename=""):
    """Function that reads a text file and prints it to stdout."""
    with open(filename, encoding="UTF8") as my_file:
        for line in my_file:
            print(line, end="")
