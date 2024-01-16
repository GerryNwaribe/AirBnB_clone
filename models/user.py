#!/usr/bin/env python3
"""User model"""


from models.base_model import BaseModel


class User(BaseModel):
    """User class"""
    def __init__(self, *args, **kwargs):
        """Initialization of User class"""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.last_name = ""
        self.first_name = ""
