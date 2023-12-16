#!/usr/bin/python3
"""Square module."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square identifier"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.height = value
        self.width = value

    def __str__(self):
        """Representation"""
        return "[{}] ({}) {}/{} - {}".\
            format(type(self).__name__, self.id, self.x, self.y, self.width)
