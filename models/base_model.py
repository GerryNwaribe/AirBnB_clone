<<<<<<< HEAD
#!/usr/bin/python3
""" This file contains the base model for the project. """

import uuid
import datetime
import models


class BaseModel():
    """ This class defines the base model for the project. """

    def __init__(self, *args, **kwargs):
        """ Initialization of the BaseModel class. """
        self.updated_at = datetime.datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == 'updated_at' or key == 'created_at':
                    value = datetime.datetime.fromisoformat(value)
                if not key.startswith('__'):
                    setattr(self, key, value)  # OR self.__dict__[k] = v
        else:
            models.storage.new(self)

    def to_dict(self):
        """Returns a dictionary containing all the keys/values of the instance.
        """
        _all_att = self.__dict__.copy()
        _all_att['created_at'] = self.created_at.isoformat()
        _all_att['updated_at'] = self.updated_at.isoformat()
        _all_att["__class__"] = self.__class__.__name__
        return _all_att

    def save(self):
        """Updates: public instance attribute updated_at -> current datetime.
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def __str__(self):
        """ String representation of the class. """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
=======
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
>>>>>>> 035fd5af54c8782ed23d287e1ad12b93547ca0b8
