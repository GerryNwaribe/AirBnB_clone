#!/usr/bin/python3
"""Class"""


import json


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        return self.__objects

    def new(self, obj):
        _id = obj['id']
        _cls = obj['__class__']
        _cls_id = _cls + '.' + _id
        self.__objects[_cls_id] = obj

    def save(self):
        """serializes dict to json"""
        with open(self.__file_path, 'w') as f:
            # f.write(json.dumps(self.__objects))
            json.dump(self.__objects, f)

    def reload(self):
        """deserializes json to dict"""
        with open(self.__file_path, 'r') as f:
            try:
                self.__objects = json.load(f)
            except FileNotFoundError:
                pass
