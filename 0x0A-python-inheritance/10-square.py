#!/usr/bin/python3
"""Square module."""
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """define a square"""
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return self.__size ** 2
