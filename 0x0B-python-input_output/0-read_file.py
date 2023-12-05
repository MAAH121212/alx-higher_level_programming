#!/usr/bin/python3
"""i/o file"""


def read_file(filename=""):
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read())
