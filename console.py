#!/usr/bin/python3
""" import documentation """
import cmd


class HBNBCommand(cmd.Cmd):
    """ Hbnb documentation"""
    prompt = '(hbnb) '
    class_name = ["BaseModel"]

    def do_create(self, arg):
        """ create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return

        if arg not in self.class_name:
            print("** class doesn't exist **")
            return

        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

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
