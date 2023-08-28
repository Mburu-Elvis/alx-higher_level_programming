#!/usr/bin/python

def safe_print_integer(value):
    '''function that prints an integer'''

    num = False
    try:
        print("{:d}".format(value))
        num = True
    except ValueError:
        num = False
    return num
