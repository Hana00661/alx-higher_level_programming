#!/usr/bin/python3
"""the function read_file"""


def read_file(filename=""):
    """function that read and print a file"""
    with open(filename) as file:
        print(file.read(), end="")
