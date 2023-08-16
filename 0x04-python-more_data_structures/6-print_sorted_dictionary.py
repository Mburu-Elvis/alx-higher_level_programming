#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    '''print a sorted dictionary'''
    sort_dict = sorted(list(a_dictionary))
    for i in sort_dict:
        print("{}: {}".format(i, a_dictionary[i]))
