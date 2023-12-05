#!/usr/bin/python3
"""Square module."""
Rectangle = __import__('9-rectangle.py').BaseGeometry


class Square(Rectangle):
    """define a square"""
    def __init__(self, size):
        super().__init__(size, size)
        self.size = size
        self.integer_validator("size", size)

    def area(self):
        return self.size ** 2
