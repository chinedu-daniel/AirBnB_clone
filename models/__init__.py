#!/usr/bin/python3
"""
Create unique storage instance
"""
from models.engine.file_storage import FileStorage
from .base_model import BaseModel
from .user import User
from .amenity import Amenity
from .city import City
from .place import Place
from .review import Review
from state import State

storage = FileStorage()
storage.reload()
classes = [BaseModel, User]
