#!/usr/bin/python3
'''deals with file storage'''
import json


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
            key = ("{}.{}".format(type(obj).__name__), obj.id)
            self.__objects[key] = obj

    def save(self):
        '''serializes a dict to a JSON file'''
        mydict = {}
        for key in self.__objects:
            mydict[key] = obj.to_dict()

        with open(self.__file_path, 'a+') as f:
            json.dump(mydict, f)

    def reload(self):
        '''deserializes a JSON to a dict'''
        mydict = {}
        try:
            with open(self.__file_path, 'r') as f:
                json.load(mydict, f)

        except FileNotFoundError:
            pass
