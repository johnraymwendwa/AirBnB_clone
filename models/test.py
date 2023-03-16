#!/usr/bin/python3
'''creates an instance of the FileStorage class'''
from engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

print(type(storage))
print(isinstance(storage, FileStorage))