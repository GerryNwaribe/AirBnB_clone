#!/usr/bin/env python3
"""Place model"""


from models.base_model import BaseModel


class User(BaseModel):
  """Place class"""
  city_id = ""           # string - empty string: it will be the City.id
  user_id = ""           # string - empty string: it will be the User.id
  name = ""              # string - empty string
  description = ""       # string - empty string
  number_rooms = 0       # integer - 0
  number_bathrooms = 0   # integer - 0
  max_guest = 0          # integer - 0
  price_by_night = 0     # integer - 0
  latitude = 0.0         # float - 0.0
  longitud = 0.0         # float - 0.0
  amenity_ids = []       # list of string - empty list: it will be the list of Amenity.id later

  def __init__(self, **kwargs):
    """Inits Place"""
    super().__init__(**kwargs)