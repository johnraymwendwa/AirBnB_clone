#!/usr/bin/python3
'''deals with file storage'''
import json
#from models.base_model import BaseModel


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

        try:
            print(mydict)
        except Exception:
            print("FAiled")

        mydict_str = json.dumps(mydict)
        with open(self.__file_path, 'w') as f:
            f.write(mydict_str)
            print("save method was colled")

    def reload(self):
        '''deserializes a JSON to a dict'''
        try:
            with open(self.__file_path, 'r') as f:
                mydict = json.load(f)
                self.new(mydict)
                #for obj_dict in mydict.values():
                    #cls = obj_dict['__class__']
                    #self.new(eval('{}({})'.format(cls, '**obj_dict')))

        except FileNotFoundError:
            pass
