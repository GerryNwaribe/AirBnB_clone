#!/usr/bin/python3
""" File storage module. """

import json
from models.base_model import BaseModel
from models.user import User


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
      _all_obj = self.__objects    # Holds all objects after reloading the file
      x = {}    # Holds the objects to be saved
      for o in _all_obj.keys():
        x[o] = _all_obj[o].to_dict()
      with open(self.__file_path,  "w") as f:
          json.dump(x, f)

  def reload(self):
      """ Reload the dictionary from the file. """
      try:
          with open(self.__file_path) as f:
              _ob = json.load(f)
              for o in _ob.values():
                  _cls = o.pop("__class__")    # del o["__class__"]
                  _r = eval(_cls)(**o)
                  self.new(_r)
                  """_cls = o.pop("__class__", None)
        if _cls:
            cls = getattr(FileStorage, _cls, None)
            if cls:
                instance = cls(**o)
                self.new(instance)"""
      except FileNotFoundError:
          pass
