#!/usr/bin/python3
"""i/o file."""


def append_write(filename="", text=""):
    """write a file"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
