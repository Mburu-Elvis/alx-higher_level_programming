#!/usr/bin/python3
"""Module defining text_indentation function."""


def text_indentation(text):
    """function that prints a text with 2 new lines after '.', '?' and ':'"""
    if not isinstance(text, str) or text == None:
        raise TypeError("text must be a string")
    prev = False
    for char in text:
        if text[0] == " " or prev == True:
            prev = False
            continue
        print(char, end="")
        prev = False
        if char == '.' or char == '?' or char == ':':
            print("\n")
            prev = True
