#!/usr/bin/python3
'''Creating a console '''
import cmd
import sys
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''THis defines our interpreter
        Attributes:
        prompt (str): The command prompt.
    '''
    prompt = "(hbnb) "
    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"}

    def do_update(self, arg):
        '''Updates the attributes of a specified class'''
        line = parse(arg)
        objs = models.storage.all()
        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")
        else:
            key = '{}.{}'.format(line[0], line[1])
            try:
                obj = objs[key]
                if len(line) == 2:
                    print("** attribute name missing **")
                elif len(line) == 3:
                    print("** value missing **")
                else:
                    try:
                        eval(line[3])
                    except (SyntaxError, NameError):
                        line[3] = "'{}'".format(line[3])
                    setattr(obj, line[2], eval(line[3]))
                    obj.save()
            except KeyError:
                print("** no instance found **")
        models.storage.save()

    def do_all(self, arg):
        '''Prints all instances of a class'''
        line = parse(arg)
        objs = models.storage.all()
        obj_list = []
        if len(line) >= 1:
            if line[0] not in self.__classes:
                print("** class doesn't exist **")
            else:
                for key, obj in objs.items():
                    if key.startswith(line[0]):
                        obj_list.append(obj.__str__())
                print(obj_list)
        else:
            for obj in objs.values():
                obj_list.append(obj.__str__())
            print(obj_list)

    def do_destroy(self, arg):
        '''Destroys an object'''
        line = parse(arg)
        if (len(line) == 0):
            print("** class name missing **")
        elif (line[0] not in self.__classes):
            print("** class doesn't exist **")
        elif (len(line) < 2):
            print("** instance id missing **")
        else:
            objs = models.storage.all()
            key = '{}.{}'.format(line[0], line[1])
            try:
                obj = objs[key]
                objs.pop(key)
                del obj
                models.storage.save()
            except KeyError:
                print("** no instance found **")

    def do_create(self, arg):
        '''Creates a new class instance, prints its id and saves it'''
        line = parse(arg)
        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            obj = eval("{}()".format(line[0]))
            print(obj.id)
            models.storage.save()

    def do_show(self, arg):
        '''Prints the string representation of an instance'''
        line = parse(arg)
        if (len(line) == 0):
            print("** class name missing **")
        elif (line[0] not in self.__classes):
            print("** class doesn't exist **")
        elif (len(line) < 2):
            print("** instance id missing **")
        else:
            objs = models.storage.all()
            print(objs)
            key = '{}.{}'.format(line[0], line[1])
            try:
                obj = objs[key]
                print(obj)
            except KeyError:
                print("** no instance found **")

    def do_quit(self, arg):
        '''Exits the prompt'''
        return True

    def do_EOF(self, arg):
        '''Exits the program when 'Ctr-D' is pressed'''
        print()
        return True


def parse(line):
    """Parses a given string, and returns a list"""
    return shlex.split(line)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
