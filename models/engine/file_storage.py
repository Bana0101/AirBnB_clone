#!/usr/bin/python3
""" module documentation"""
import json
from os import path
#from models.base_model import BaseModel


class FileStorage:
    """ A class for serializing instance to a JSON file """

    __file_path = "file.json"
    __objects = {}
#   classes = {"BaseModel": BaseModel, "User": User}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        srl_objs = {}
        for key, obj in self.__objects.items():
            srl_objs[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(srl_objs, file)

    def reload(self):
        if path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
            for key, objt in data.items():
                class_name, obj_id = key.split('.')
                clas = globals()[class_name]
                obj = clas(**objt)
                self.__objects[key] = obj
