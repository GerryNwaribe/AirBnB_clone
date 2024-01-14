#!/usr/bin/env python3
"""State model"""


from models.base_model import BaseModel


class State(BaseModel):
    """State class"""
    name = ""

    def __init__(self, **kwargs):
        """Inits State"""
        super().__init__(**kwargs)
