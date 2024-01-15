#!/usr/bin/python3
"""the Base class"""

class Base:
    """the Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """function that create a instance of Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
