#!/usr/bin/python3
"""json module."""


class Student:
    """student and json"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        try:
            for i in attrs:
                if type(i) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        dict_v = dict()
        for k, v in self.__dict__.items():
            if k in attrs:
                dict_v[k] = v
        return dict_v

    def reload_from_json(self, json):
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value
