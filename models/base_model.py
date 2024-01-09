#!/usr/bin/python3
""" Class: BaseModel (AirBnb) """

import uuid     # Universally Unique Identifier.
import datetime     # Managing date & TIme.

class BaseModel():
    """ BaseModel:
            Defines all common attributes/methods for other classes in AirBNB
    """
    def __init__(self):
        """Class Constructor:

            Args:
                id: string - assign with an uuid when an instance is created
                created_at: assign with the current datetime when an instance is created
                updated_at: assign with the current datetime when an instance is created and it will be updated every time you change your object
        """
        self.updated_at = datetime.datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")


    def save(self):
        """updates the public instance attribute updated_at with the current datetime
        """

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance
        """
        return (self.__dict__)
