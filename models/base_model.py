#!/usr/bin/python3
""" This file contains the base model for the project. """


from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """ This class defines the base model for the project. """

    def __init__(self, *args, **kwargs):
        """ Initialization of the BaseModel class.
        Args:
            arg: Inputs
            kwargs: Key-word Args
        """
        self.updated_at = datetime.now()
        self.id = str(uuid4())
        self.created_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == 'updated_at' or key == 'created_at':
                    # OR setattr(self, key, datetime.strptime(value, time_format))
                    value = datetime.fromisoformat(value)
                if key != '__class__':
                    self.__dict__[key] = value  # Or setattr(self, key, value)

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
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """ String representation of the class. """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
