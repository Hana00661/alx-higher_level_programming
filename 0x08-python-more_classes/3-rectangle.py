#!/usr/bin/python3
"""Defines a class Rectangle
"""


class Rectangle:
    """
    Class that defines properties of rectangle (based on 2-rectangle.py)

    Attributes:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
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
        return self.__width

    @property
    def height(self):
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

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + 2 * self.__height

    def __str__(self):
        lisr = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for h in range(self.__height):
            for w in range(self.__width):
                lisr = lisr + '#'
            if h < self.__height - 1:
                lisr = lisr + '\n'
        return lisr
