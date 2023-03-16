#!/usr/bin/python3
'''Creating a console '''
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, args):
        '''Exits the prompt'''
        return True

    def do_EOF(self, line):
        '''Exits the program when 'Ctr-D' is pressed'''
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
