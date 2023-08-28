#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    '''Function that prints x elements of a list'''

    try:
        for i in range(x):
            print(f"{my_list[i]}", end="")
    except IndexError:
        i -= 1
    i += 1
    print()
    return (i)
