#!/usr/bin/python3

import json
from models.base_model import BaseModel


class FileStorage():
  __file_path = "file.json"
  __objects = {}

  def __init__(self):
    pass

  def all(self):
    return self.__objects

  def new(self, obj):
    self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

  def save(self):
    _all_obj = self.__objects    # Holds all objects after reloading the file
    x = {}    # Holds the objects to be saved
    for o in _all_obj.keys():
      x[o] = _all_obj[o].to_dict()
    with open(self.__file_path,  "w") as f:
      json.dump(x, f)

  def reload(self):
    try:
      with open(self.__file_path) as f:
        _ob = json.load(f)
        for o in _ob.values():
          _cls = o.pop("__class__")    # del o["__class__"]
          _r = eval(_cls)(**o)
          self.new(_r)
    except FileNotFoundError:
      pass