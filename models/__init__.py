#!/usr/bin/python3
""" __init__ file """

from models.engine.file_storage import FileStorage
from datetime import datetime
import uuid


storage = FileStorage()

storage.reload()
storage.save()

# def __init__(self, *args, **kwargs):
#    self.id = str(uuid.uuid4())
#    self.created_at = datetime.now()
#    self.save()
# if
