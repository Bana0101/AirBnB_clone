#!/usr/bin/python3
""" import documentation """
import cmd


class HBNBCommand(cmd.Cmd):
    """ Hbnb documentation"""
    prompt = '(hbnb) '
    valide_classname = ["BaseModel"]

    def do_create(self, arg):
        """ create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return

        if arg not in self.valide_classname:
            print("** class doesn't exist **")
            return

        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valide_classname:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

    def do_destroy(self, arg):
        """ deletes an instance based on the class name and id"""
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valide_classname:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

    def do_update(self, arg):
        """ update an instance based on the class name and id"""
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valide_classname:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attr_name = args[2]
        if attr_name not in ["id", "created_at", "updated_at"]:
            if len(args) < 4:
                print("** value missing **")
                return

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
