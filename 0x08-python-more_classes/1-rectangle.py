#!/usr/bin/python3
""" A class Rectangle that defines a rectangle
     (based on 0-rectangle.py)
"""


class Rectangle:
    """ this class working on privet attributes
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__height = height
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        """width retriver.
        Returns:
            int: the width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """Width retriver.

        Returns:
            int: the width of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
