#!/usr/bin/python3
"""This module is createing a new class Square"""


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

    def my_print(self):
        """Prints the square with #"""
        if self.__size > 0:
            for i in range(self.size):
                for i in range(self.size):
                    print("#", end="")
                print()
        else:
            print()

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
