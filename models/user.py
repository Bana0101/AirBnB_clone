#!/usr/bin/python3
""" import BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ Initialize User instance """
        super().__init__(*args, **kwargs)
