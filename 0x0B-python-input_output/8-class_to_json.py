#!/usr/bin/python3
"""JSON module."""


def class_to_json(obj):
    """a function that returns the dictionary description with simple data"""
    return obj.__dict__
