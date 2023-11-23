#!/usr/bin/python3
"""square module."""


class Square:
    """Defines the area"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = positi

    @property
    def position(self):
        return (self.__positio)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise ValueError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        [print("") for p in range(self.__position[1])]
        for i in range(self.__size):
            [print("_", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print("")
