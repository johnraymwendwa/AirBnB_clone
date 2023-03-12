#!/usr/bin/python3
'''This qill be the base class'''
import uuid
from datetime import datetime as date


class BaseModel:
    '''Contains the building objects'''
    def __init__(self, *args, **kwargs):
        '''creates instance attributes'''
        if kwargs:
            for key, val in kwargs.items():
                if key != "__class__":
                    if key == 'created_at' or key == 'updated_at':
                        val = date.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = date.now()
            self.updated_at = date.now()

    def __str__(self):
        '''returns a string of info'''
        return ("[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__))

    def save(self):
        '''updates the updated_at attr'''
        self.updated_at = date.now()

    def to_dict(self):
        '''creates a dictionary containing all attributes'''
        mydict = {}
        mydict["__class__"] = type(self).__name__
        for (key, val) in self.__dict__.items():
            if key == "created_at":
                mydict[key] = date.isoformat(val)
            elif key == "updated_at":
                mydict[key] = date.isoformat(val)
            else:
                mydict[key] = val
        return mydict
