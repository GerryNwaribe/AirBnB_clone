#!/usr/bin/env python3
"""User model"""


from models.base_model import BaseModel


class City(BaseModel):
  """City class"""
  state_id = ""    # it will be the State.id
  name = ""

  def __init__(self, **kwargs):
    """Inits City"""
    super().__init__(**kwargs)