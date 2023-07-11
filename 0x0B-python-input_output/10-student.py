#!/usr/bin/python3
"""a student class the defines a student"""


class Student:
    """the student class"""
    def __init__(self, first_name, last_name, age):
        """the init method for the student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """a method to retrive a dictionary rep of student instance"""
        if attrs is not None and all(isinstance(x, str) for x in attrs):
            d = {}
            for k, v in self.__dict__.items():
                if k in attrs:
                    d[k] = v
            return d
        else:
            return self.__dict__
