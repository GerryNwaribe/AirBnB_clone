#!/usr/bin/python3
""" This module contains the base class for all models."""

from models.engine.file_storage import FileStorage

"""This is the base class for all models."""
storage = FileStorage()
storage.reload()
