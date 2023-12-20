#!/usr/bin/python3
"""This module is create a new class Square"""


class Square():
    """A square class."""
    def __init__(self, size=0):
        """Initialization square."""

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Create area

        Returns:
            area of the Square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Getter function of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter function of size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
