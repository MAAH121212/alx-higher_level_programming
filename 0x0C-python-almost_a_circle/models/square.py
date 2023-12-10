#!/usr/bin/python3
"""Sqare module."""


Rectangle = __import__('rectangle').Rectangle


class Square(Rectangle):
    """Square identifier"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.height = value
        self.width = value

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".\
            format(type(self).__name__, self.id, self.x, self.y, self.width)
