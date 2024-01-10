#!/usr/bin/python3
from datetime import datetime
import uuid

class BaseModel:
    self.id = str(uuid.uuid4())
    self.created_at: datetime.now()
    self.updated_at: datetime.now()
    
    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        return("[{}] [{}] {}".format(self.__class__.__name__, self.id, self.__dict__))
    
    def save(self):
        """updates the public instance 
        attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """returns a dictionary containing 
        all keys/values of __dict__ of the instance"""
        diction = self.__dict__.copy()
        diction['__class__'] = self.__class__.__name__
        diction['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]
        diction['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]
        return diction
