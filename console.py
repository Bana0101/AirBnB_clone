#!/usr/bin/python3
""" import documentation """
import cmd


class HBNBCommand(cmd.Cmd):
    """ Hbnb documentation"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ Exist the program"""
        return True

    def do_EOF(self, arg):
        """ Exist the program"""
        print()
        return True

    def emptyline(self):
        """ Do nothing on empty iput line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
