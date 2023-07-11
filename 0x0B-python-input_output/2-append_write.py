#!/usr/bin/python3
"""a module to append a string to a file"""


def append_write(filename="", text=""):
    """a function to append a text to a file"""
    with open(filename, "a+", encoding="UTF8") as f:
        f.write(text)
    return len(text)
