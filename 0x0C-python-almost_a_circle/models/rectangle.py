#!/usr/bin/python3
"""Rectangle"""


from moduls.base import Base

class Rectangle(Base):
    """define a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width
        self.validator("width", value, True)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height
        self.validator("height", value)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x
        self.validator("x", value)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
        self.validator("y", value, False)

    def validator(self, name, value, eq=False):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        elif not eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
