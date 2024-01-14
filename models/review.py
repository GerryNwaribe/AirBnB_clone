#!/usr/bin/python3
"""Reviews Class"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Review class"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, **kwargs):
        """Inits Review"""
        super().__init__(**kwargs)
