#!/usr/bin/python3

def safe_print_division(a, b):
    '''function that divides 2 integers and prints result'''

    result = 0
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: ", end="")
        if result is None:
            print("{}".format(result))
        else:
            print("{:.1f}".format(result))
        return (result)
