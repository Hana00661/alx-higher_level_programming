#!/usr/bin/python3
"""This module create a new class Square"""


class Square():
    """A square class."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialization square."""

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """
        Create area

        Returns:
            area of the Square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with #
        Prints square in a position
        """
        if self.__size > 0:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end="")
                for i in range(self.__size):
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

    @property
    def position(self):
        """Getter function of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter function of position. position of the square"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value
