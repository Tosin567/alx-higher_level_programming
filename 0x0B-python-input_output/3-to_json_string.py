#!/usr/bin/python3
"""a module that returns the json representation of an object"""
import json


def to_json_string(my_obj):
    """function to convert object to json"""
    return json.dumps(my_obj)
