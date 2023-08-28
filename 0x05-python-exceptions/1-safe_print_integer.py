#!/usr/bin/python

def safe_print_integer(value):
    '''function that prints an integer'''

    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
