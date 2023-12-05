#!/usr/bin/python3
"""Json module."""


import json


def load_from_json_file(filename):
    """Write a function that returns the JSON"""
    with open(filename, 'r') as f:
        return json.load(f)
