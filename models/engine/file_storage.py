#!/usr/bin/python3
""" File storage module. """

import json
import os


class FileStorage():
    """ File storage class. """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """ Initialize the file storage. """
        pass

    def all(self):
        """ Return the dictionary of objects. """
        return self.__objects

    def new(self, obj):
        """ Add a new object to the dictionary. """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """ Save the dictionary to the file. """
        _all_obj = self.__objects
        x = {}
        for o in _all_obj.keys():
            x[o] = _all_obj[o].to_dict()
        with open(self.__file_path,  "w") as f:
            json.dump(x, f)

    def reload(self):
        """ Reload the dictionary from the file. """
        if not os.path.isfile(FileStorage.__file_path):
            return
        try:
            with open(self.__file_path) as f:
                _ob = json.load(f)
                for o in _ob.values():
                    _cls = o.pop("__class__")
                    _r = eval(_cls)(**o)
                    self.new(_r)
        except (FileNotFoundError, EOFError, json.JSONDecodeError):
            pass
