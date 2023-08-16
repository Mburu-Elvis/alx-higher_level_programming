#!/usr/bin/python3


def best_score(a_dictionary):
    best = None
    if a_dictionary is not None:
        keys = list(a_dictionary)
        num = a_dictionary[keys[0]]
        for key in keys:
            if a_dictionary[key] >= num:
                best = key
                num = a_dictionary[key]
    return (best)
