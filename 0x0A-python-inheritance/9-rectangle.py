#!/usr/bin/python3
"""the Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """function that create a rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Function that return the rectangle area

        Returns:
            int: rectangle area
        """
        return self.__height * self.__width

    def __str__(self):
        """Function that define the __str__ method"""
        return f"[Rectangle] {self.__width}/{self.__height}"
