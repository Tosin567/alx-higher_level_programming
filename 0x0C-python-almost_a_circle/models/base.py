#!/usr/bin/python3
"""a first class named Base"""


class Base:
    """the Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """the init method"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
