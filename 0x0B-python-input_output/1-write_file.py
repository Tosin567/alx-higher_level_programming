#!/usr/bin/python3
""" A function that writes a string to a text file
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """write file to filename and return lenght of text"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
