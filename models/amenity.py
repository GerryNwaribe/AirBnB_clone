#!/usr/bin/env python3
"""Amenity model"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class"""
    name = ""

    def __init__(self, **kwargs):
        """Inits Amenity"""
        super().__init__(**kwargs)
