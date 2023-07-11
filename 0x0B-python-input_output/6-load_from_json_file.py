#!/usr/bin/python3
"""load from json module"""
import json


def load_from_json_file(filename):
    """function to load from json"""
    with open(filename, encoding="UTF8") as f:
        obj = f.read()
    return json.loads(obj)
