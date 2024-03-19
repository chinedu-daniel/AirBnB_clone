#!/usr/bin/python3
"""
Create unique storage instance
"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
