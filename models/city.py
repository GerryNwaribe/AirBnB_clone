#!/usr/bin/env python3
"""User model"""


from models.base_model import BaseModel


class City(BaseModel):
    """City class"""
    state_id = ""
    name = ""
