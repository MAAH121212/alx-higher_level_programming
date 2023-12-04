#!/usr/bin/python3
"""subclasses module."""


class BaseGeometry:
    """Base Class"""

    def area(self):
        """error handler"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checking value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
