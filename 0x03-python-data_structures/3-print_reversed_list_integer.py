#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    i = len(my_list) - 1
    new_list = my_list[i::-1]
    for x in range(i + 1):
        print('{:d}'.format(new_list[x]))
