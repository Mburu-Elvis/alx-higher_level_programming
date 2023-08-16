#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    temp = dict(a_dictionary)
    for key in list(temp):
        temp[key] = temp[key] * 2
    return temp
