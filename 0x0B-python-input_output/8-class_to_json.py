#!/usr/bin/python3
"""the class_to_json function"""


def class_to_json(obj):
    """function that returns the dictionary description
    with simple data structure"""
    return obj.__dict__
