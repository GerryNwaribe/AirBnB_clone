#!/usr/bin/env python3
"""User model"""


from models.base_model import BaseModel


class User(BaseModel):
    """User class"""
    email = ""
    password = ""
    last_name = ""
    first_name = ""

    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       if not kwargs:
           self.email = ""
           self.password = ""
           self.last_name = ""
           self.first_name = ""
