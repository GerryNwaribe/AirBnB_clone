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
    """Returns a dictionary containing all the keys/values of the instance."""
    _all_att = self.__dict__.copy()
    _all_att['created_at'] = self.created_at.isoformat()
    _all_att['updated_at'] = self.updated_at.isoformat()
    _all_att["__class__"] = self.__class__.__name__
    return _all_att

  def save(self):
    """Updates the public instance attribute updated_at with the current datetime."""
    self.updated_at = datetime.datetime.now()
    models.storage.save()

  def __str__(self):
    """ String representation of the class. """
    return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
