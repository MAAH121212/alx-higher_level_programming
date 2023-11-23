#!/usr/bin/python3
"""square module."""


class Square:
    """Defines a square."""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise ValueError("size must be an integer")
        else:
            self.__size = value
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
