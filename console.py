#!/usr/bin/python3
'''Creating a console '''
import cmd


class HBNBCommand(cmd.Cmd):
    '''THis defines our interpreter
        Attributes:
        prompt (str): The command prompt.
    '''
    prompt = "(hbnb) "

    def do_quit(self, arg):
        '''Exits the prompt'''
        return True

    def do_EOF(self, arg):
        '''Exits the program when 'Ctr-D' is pressed'''
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
