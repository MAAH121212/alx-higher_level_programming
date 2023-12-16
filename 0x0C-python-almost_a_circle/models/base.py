#!/usr/bin/python3
"""semi circle module."""
import json


class Base:
    """Base class module."""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is not None:
            list_obj = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w") as f:
            f.write(cls.to_json_string(list_obj))
