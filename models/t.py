#!/usr/bin/python3
""" a basemodel class """

import datetime
import uuid
from models.__init__ import __init__


class BaseModel:
    """ the basemodel class """

    id = None
    created_at = None
    updated_at = None

    def save(self):
        self.updated_at = datetime.datetime.now().isoformat()

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now().isoformat()
        self.save()
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def to_dict(self):
        dic = {}
        dic["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if (key in ["created_at", "updated_at"]
                    and isinstance(value, datetime.datetime)):
                dic[key] = value.isoformat()
            else:
                dic[key] = value
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
