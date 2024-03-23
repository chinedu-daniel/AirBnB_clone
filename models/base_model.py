#!/usr/bin/python3
"""
Base class for the entire project
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    Base for all classes in the console project

    Attributes:
        id(str): unique identifier of an instance of the class
        created_at(datetime): time by which the instance is created
        updated_at(datetime): time by which the instance is updated

    Methods:
        __str__:
        save(self):
        to_dict(self):

    """
    def __init__(self, *args, **kwargs) -> None:
        """
        initialize the instance of a class
        """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)

    def __str__(self) -> str:
        """
        Returns the string representation of the class
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Update the attribute:
        updated_at with the current time
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        The dictionary representation of the class's insteance
        """
        dict_ = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                dict_[key] = value.isoformat()
            else:
                dict_[key] = value
        dict_["__class__"] = self.__class__.__name__
        return dict_
