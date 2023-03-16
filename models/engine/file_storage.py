#!/usr/bin/python3
'''deals with file storage'''
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    '''class to store to JSON'''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''returns a dict of objects'''
        return self.__objects

    def new(self, obj):
        '''adds key-value pairs to __objects with formatting'''
        if obj:
            key = ("{}.{}".format(type(obj).__name__, obj.id))
            self.__objects[key] = obj

    def save(self):
        '''serializes a dict to a JSON file'''
        mydict = {}
        for key,obj in self.__objects.items():
            mydict[key] = obj.to_dict()
        
        mydict_str = json.dumps(mydict)
        with open(self.__file_path, 'w') as f:
            f.write(mydict_str)

    def reload(self):
        '''deserializes a JSON to a dict'''
        try:
            with open(self.__file_path, 'r') as f:
                mydict = json.load(f)
                for obj_dict in mydict.values():
                    cls = obj_dict['__class__']
                    del obj_dict['__class__']
                    self.new(eval(cls) (**obj_dict))

        except FileNotFoundError:
            pass
