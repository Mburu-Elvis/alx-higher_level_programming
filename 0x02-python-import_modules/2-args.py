#!/usr/bin/python3
from sys import argv


def display_args():
    x = len(argv) - 1
    if x == 1:
        print('{:d} argument:'.format(x))
    elif x == 0:
        print('{:d} arguments.'.format(x))
    else:
        print('{:d} arguments:'.format(x))
    for i in range(1, x + 1):
        print('{:d}: {}'.format(i, argv[i]))


if __name__ == '__main__':
    display_args()
