#!/usr/bin/python3
"""subclasses module."""


def inherits_from(obj, a_class):
    """Write a function that returns True if the object is an instance"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
