#!/usr/bin/python3
from sys import argv


def infinite_add():
    x = len(argv)
    result = 0
    for i in range(1, x):
        result += int(argv[i])
    print(result)


if __name__ == '__main__':
    infinite_add()
