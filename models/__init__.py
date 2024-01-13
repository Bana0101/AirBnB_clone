#!/usr/bin/python3
""" __init__ file """

import datetime
import uuid


def __init__(self, *args, **kwargs):
    self.id = str(uuid.uuid4())
    self.created_at = datetime.datetime.now().isoformat()
    self.save()
