#!/usr/bin/python3
"""
Create unique storage instance
"""
from models.engine.file_storage import FileStorage
from .base_model import BaseModel
from .user import User

storage = FileStorage()
storage.reload()
classes = [BaseModel, User]
