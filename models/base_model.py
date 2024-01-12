#!/usr/bin/python3
""" a basemodel class """
import datetime, uuid

class BaseModel:
    """ the basemodel class """

    id = str(uuid.uuid4())
    created_at = None
    updated_at = None

    def save(self):
        self.updated_at = datetime.datetime.now().isoformat()

    def __init__(self, *args, **kwargs):
        self.created_at = datetime.datetime.now().isoformat()
        self.save()
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def to_dict(self):
        dic = {"__class__": self.__class__.__name__}
        for key, value in self.__dict__.items():
            if key in ["created_at", "updated_at"] and isinstance(value, datetime.datetime):
                dic[key] = value.isoformat()
            else:
                dic[key] = value
        return dic
