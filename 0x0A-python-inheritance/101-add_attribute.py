#!/usr/bin/python3
"""the function add_attribute"""


def add_attribute(self, key, value):
    """function that adds a new attribute
    to an object if it’s possible"""
    if hasattr(self, '__dict__') is False:
        raise TypeError("can't add new attribute")
    else:
        setattr(self, key, value)
