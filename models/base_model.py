#!/usr/bin/python3
""" a basemodel class """

from datetime import datetime
from models import storage
import uuid


class BaseModel:
    """ the basemodel class """

    def __init__(self, *args, **kwargs):
        if not kwargs or '__class__' not in kwargs:
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(
                                value, "%Y-%m-%dT%H:%M:%S.%f"
                                )
                    setattr(self, key, value)
            storage.new(self)

    def save(self):
        self.updated_at = datetime.now()
        storage.save(self)

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def to_dict(self):
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic

    @classmethod
    def from_dict(cls, data):
        if data:
            ins = cls()
            for key, value in data.items():
                if key == "__class__":
                    ins.__class__.__name__ = data["__class__"]
                elif (key in ["created_at", "updated_at"]
                        and isinstance(value, str)):
                    value = datetime.datetime.fromisoformat(value)
                setattr(ins, key, value)
        else:
            ins = cls()
        return ins
