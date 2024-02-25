#!/usr/bin/python3
""" This module contains the base class for all models."""

from models.engine.file_storage import FileStorage
from os import getenv
"""This is the base class for all models."""

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
