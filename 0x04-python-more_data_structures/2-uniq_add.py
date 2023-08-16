#!/usr/bin/python3


def uniq_add(my_list=[]):
    ''' A function that adds the unique elements'''
    a = set(my_list)
    sum = 0
    for i in a:
        sum += i
    return (sum)
