#!/usr/bin/python3
import os
import hidden_4


def find_hidden():
    hidden = dir(hidden_4)
    for i in hidden:
        if i[0] == '_' and i[1] == '_':
            pass
        else:
            print(i)


if __name__ == '__main__':
    find_hidden()
