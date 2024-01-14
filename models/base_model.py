#!/usr/bin/python3
""" a basemodel class """

from datetime import datetime
import uuid


class BaseModel:
    """ the basemodel class """

    def save(self):
        self.updated_at = datetime.now()

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
            self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def to_dict(self):
        dic = {}
        dic["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if (key in ["created_at", "updated_at"]
                    and isinstance(value, datetime)):
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
