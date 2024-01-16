#!/usr/bin/python3
"""This module defines the BaseModel class"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def to_dict(self):
      """ Returns a dictionary containing all the keys/values of the instance. """
      _all_att = self.__dict__.copy()
      _all_att['created_at'] = self.created_at.isoformat()
      _all_att['updated_at'] = self.updated_at.isoformat()
      _all_att["__class__"] = self.__class__.__name__

      return _all_att

    def save(self):
      """ Updates the public instance attribute updated_at with the current datetime. """
      self.updated_at = datetime.datetime.now()
      models.storage.save()

    def __str__(self):
        """Return a string representation of the BaseModel instance"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """Update updated_at attribute with datetime, save to storage"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict