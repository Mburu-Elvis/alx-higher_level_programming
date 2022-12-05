#!/usr/bin/python3
def print_list_integer(my_list=[]):
    item = 0
    str = "{}"
    while item < len(my_list):
        print(str.format(my_list[item]))
        item += 1
