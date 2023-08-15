#!/usr/bin/python3


def multiple_returns(sentence):
    a, b = 0, ''
    if sentence is None or sentence == "":
        b = None
        a = 0
    else:
        a, b = len(sentence), sentence[0]
    return (a, b)
