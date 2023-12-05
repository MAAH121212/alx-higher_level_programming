#!/usr/bin/python3
"""JSON Module"""


import json


def save_to_json_file(my_obj, filename):
    """Write a function that returns the JSON"""
    with open(filename, 'w') as f:
        return json.dump(my_obj, f)
