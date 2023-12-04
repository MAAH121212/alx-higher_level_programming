#!/usr/bin/python3
"""module for lookup method."""


class MyList(list):
    """that prints the list, but sorted (ascending sort)"""
    def print_sorted(self):
        print(sorted(self))
