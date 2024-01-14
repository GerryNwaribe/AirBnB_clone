#!/usr/bin/env python3
"""User model"""


from models.base_model import BaseModel


class User(BaseModel):
    """User class"""
    email = ""
    password = ""
    last_name = ""
    first_name = ""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
