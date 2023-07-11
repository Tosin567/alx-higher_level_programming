#!/usr/bin/python3
"""a class student that defines a student"""


class Student:
    """the class student"""
    def __init__(self, first_name, last_name, age):
        """the init method for the class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary represetation of a student"""
        return self.__dict__
