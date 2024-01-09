#!/usr/bin/python3
"""the MyInt class"""


class MyInt(int):
    """the class MyInt"""
    def __init__(self, i):
        """function that create an object"""
        self.__i = i

    def __ne__(self, i):
        """function that return equal value"""
        return self.__i == self.__i

    def __eq__(self, i):
        """function that return non-equal value"""
        return self.__i != self.__i
