#!/usr/bin/python3
""" a basemodel class """
import datetime, uuid

class BaseModel:
    """ the basemodel class """

    id = None
    created_at = None
    updated_at = None

    def __init__(self, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now().isoformat()
        for key, value in kwargs.items():
            setattr(self, key, value)

    def save(self):
        self.updated_at = datetime.datetime.now().isoformat()

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def to_dict(self):
        dic = {self.__class__: self.__class__.__name__}
        for key, value in self.__dict__.items():
            dic.update({key: value})
        return dic
