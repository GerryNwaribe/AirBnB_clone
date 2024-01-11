#!/usr/bin/python3
""" This file contains the base model for the project. """


import datetime     # Managing date & TIme.
import uuid     # Universally Unique Identifier.
import models



class BaseModel():
    """ BaseModel:
            Defines all common attributes/methods for other classes in AirBNB
    """
    # att = ['updated_at', 'created_at', 'id']

    def __init__(self, *args, **kwargs):
        """ Initialization of the BaseModel class. """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'updated_at' or key == 'created_at':
                    value = datetime.datetime.fromisoformat(value)
                if not key.startswith('__'):
                    setattr(self, key, value)

        else:
            self.updated_at = datetime.datetime.now()
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            storage.new(self.__dict__)

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>
        """
        _all_att = dict(vars(self))    # OR = self.__dict__

        """_dynamic_att = {key: value for key, value in _all_att.items()
                    if key not in BaseModel.att}
        _native_att = {key: value for key, value in _all_att.items()
                    if key not in _dynamic_att}

        _dynamic_att = dict(sorted(_dynamic_att.items()))
        _dynamic_att.update(_native_att)"""
        return (f"[{self.__class__.__name__}] ({self.id}) {_all_att}")

    def save(self):
        """updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance
        """
        _all_att = vars(self)    # OR = self.__dict__

        iso_created_at = self.created_at.isoformat()
        iso_updated_at = self.updated_at.isoformat()

        """_dynamic_att = {key: value for key, value in _all_att.items()
                    if key not in BaseModel.att}
        _native_att = {key: value for key, value in _all_att.items()
                   if key not in _dynamic_att}"""

        if 'created_at' in _all_att:
            _all_att['created_at'] = iso_created_at
        if 'updated_at' in _all_att:
            _all_att['updated_at'] = iso_updated_at

        # _dynamic_att = dict(sorted(_dynamic_att.items()))
        _all_att["__class__"] = self.__class__.__name__
        # _dynamic_att.update(_native_att)
        return (_all_att)
