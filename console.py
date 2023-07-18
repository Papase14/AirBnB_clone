#!/usr/bin/python3
"""
    console
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
        Entry to command interpreter
    """
    prompt = "(hbnb) "
    classes = {
        "Amenity": Amenity,
        "BaseModel": BaseModel,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
        "User": User
    }

    def do_EOF(self, arg):
        """
            Exit on Ctrl-D
        """
        print()
        return True

    def do_quit(self, arg):
        """
            Exit on quit
        """
        return True

    def help_quit(self):
        """
        Help documentation for quit command.
        """
        print("Quit command to exit the program")

    def emptyline(self):
        """
            Overwrite default behavior to repeat last cmd
        """
        pass

    def do_create(self, arg):
        """
            Create instance specified by user
        """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            instance = eval(arg)()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """
            Print string representation: name and id
        """
        if len(arg) == 0:
            print("** class name missing **")
            return
        args = parse(arg)
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[name])
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """
            Destroy instance specified by user; Save changes to JSON file
        """
        if len(arg) == 0:
            print("** class name missing **")
            return
        args = parse(arg)
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    del storage.all()[name]
                    storage.save()
        except IndexError:
            print("** instance id missing **")

    def do_all(self, arg):
        """
            Print all objects or all objects of specified class
        """
        if not arg:
            print([str(value) for value in storage.all().values()])
        else:
            class_name = arg.split()[0]
            if class_name not in storage.all_classes():
                print("** class doesn't exist **")
            else:
                class_instances = storage.all_classes()[class_name]
                print([str(instance) for instance in class_instances])

    def do_update(self, arg):
        """
            Update if given exact object, exact attribute
        """
        args = parse(arg)
        if len(args) >= 4:
            key = "{}.{}".format(args[0], args[1])
            cast = type(eval(args[3]))
            arg3 = args[3]
            arg3 = arg3.strip('"')
            arg3 = arg3.strip("'")
            setattr(storage.all()[key], args[2], cast(arg3))
            storage.all()[key].save()
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")

    def do_count(self, arg):
        """
            Display count of instances specified
        """
        if arg in HBNBCommand.classes:
            count = 0
            for key, objs in storage.all().items():
                if arg in key:
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")

    def default(self, arg):
        """
            Accepts class name followed by arguement
        """
        args = arg.split('.')
        class_arg = args[0]
        if len(args) == 1:
            print("*** Unknown syntax: {}".format(arg))
            return
        try:
            args = args[1].split('(')
            command = args[0]
            if command == 'all':
                HBNBCommand.do_all(self, class_arg)
            elif command == 'count':
                HBNBCommand.do_count(self, class_arg)
            elif command == 'show':
                args = args[1].split(')')
                id_arg = args[0]
                id_arg = id_arg.strip("'")
                id_arg = id_arg.strip('"')
                arg = class_arg + ' ' + id_arg
                HBNBCommand.do_show(self, arg)
            elif command == 'destroy':
                args = args[1].split(')')
                id_arg = args[0]
                id_arg = id_arg.strip('"')
                id_arg = id_arg.strip("'")
                arg = class_arg + ' ' + id_arg
                HBNBCommand.do_destroy(self, arg)
            elif command == 'update':
                args = args[1].split(',')
                id_arg = args[0].strip("'")
                id_arg = id_arg.strip('"')
                name_arg = args[1].strip(',')
                val_arg = args[2]
                name_arg = name_arg.strip(' ')
                name_arg = name_arg.strip("'")
                name_arg = name_arg.strip('"')
                val_arg = val_arg.strip(' ')
                val_arg = val_arg.strip(')')
                arg = class_arg + ' ' + id_arg + ' ' + name_arg + ' ' + val_arg
                HBNBCommand.do_update(self, arg)
            else:
                print("*** Unknown syntax: {}".format(arg))
        except IndexError:
            print("*** Unknown syntax: {}".format(arg))


def parse(arg):
    """
        Helper method to parse user typed input
    """
    return tuple(arg.split())


if __name__ == "__main__":
    storage.reload()
    HBNBCommand().cmdloop()
