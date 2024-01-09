#!/usr/bin/python3
"""the Student class"""


class Student:
    """the Student class"""
    def __init__(self, first_name, last_name, age):
        """function that create a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method that that retrieves a
        dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        dic = {}
        for a in attrs:
            if a in self.__dict__:
                dic[a] = self.__dict__[a]
        return dic
