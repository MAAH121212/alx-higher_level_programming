#!/usr/bin/python3
"""i/o file"""


def read_file(filename=""):
    with open('my_file_0.txt', 'r', encoding="utf-8") as f:
        print(f.read())
