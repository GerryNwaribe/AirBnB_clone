#!/usr/bin/env python3

import json
from datetime import datetime


class FileStorage():
  __file_path = "file.json"
  __objects = {}

  def __init__(self, file_path='file.json'):
    self.__file_path = file_path
    self.__objects = {}

  def all(self):
    return self.__objects

  def new(self, obj):
    if '__class__' in obj:
      _id = obj['id']
      _cls = obj['__class__']
      _cls_id = f"{_cls}.{_id}"

      # Check if the object already exists in __objects
      if _cls_id not in self.__objects:
          # Create an instance of the class and add it to __objects
          obj_class = globals()[_cls]
          obj_instance = obj_class(**obj)
          self.__objects[_cls_id] = obj_instance

  def save(self):
    _all_obj = self.__objects    # Holds all objects after reloading the file
    x = {}    # Holds the objects to be saved
    for o in _all_obj.keys():
      x[o] = _all_obj[o].to_dict()
    with open(self.__file_path,  "w") as f:
      json.dump(x, f)
  
  """def save(self):
    with open(self.__file_path, 'w') as f:
      json.dump({key: obj.__dict__ for key, obj in self.__objects.items()}, f)

    # Print the contents of the file
    with open(self.__file_path, 'r') as f:
      contents = f.read()
      print(contents)"""

  def reload(self):
    try:
      with open(self.__file_path) as f:
        _ob = json.load(f)
        print(_ob)
        for o in _ob.values():
          _cls = o.pop("__class__")    # del o["__class__"]
          _r = eval(_cls)(**o)
          self.new(_r)

    except FileNotFoundError:
      return