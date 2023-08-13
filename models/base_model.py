#!/usr/bin/python3
"""defines all common attributes/methods for other classes"""


import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """*args, **kwargs arguments for the constructor of a BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if not k == "__class__":
                    if k == "created_at" or k == "updated_at":
                        v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, k, v)
                    setattr(self, k, v)
        else:
            models.storage.new(self)

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}){}".format(self.__class__.__name__, self.id, self.__dict__)


    def save(self):
        """updates the public instance attribute updated_at with the current
        datetime"""
        self.updated_at = datetime.now()
        models.storage.save()


    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of
        the instance"""
        data = self.__dict__.copy()
        data["__class__"] = self.__class__.__name__
        data["updated_at"] = self.updated_at.isoformat()
        data["created_at"] = self.created_at.isoformat()
        return data
