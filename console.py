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
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
            Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
            Exit the program when End-of-File (EOF) character is encountered
        """
        print()  # Print a new line before exiting
        return True

    def emptyline(self):
        """
            Do nothing when an empty line is entered
        """
        pass

    def do_create(self, arg):
        """
            Create a new instance of BaseModel, save it, and print the ID
        """
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """
            Print the string representation of an instance
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all().keys():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
            Delete an instance based on the class name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all().keys():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
            Print string representations of all instances
        """
        if not arg:
            print([str(value) for value in storage.all().values()])
        elif arg not in storage.classes.keys():
            print("** class doesn't exist **")
        else:
            class_instances = [str(value) for key, value in storage.all().items() if key.split(".")[0] == arg]
            print(class_instances)

    def do_update(self, arg):
        """
            Update an instance based on the class name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in storage.classes.keys():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all().keys():
                instance = storage.all()[key]
                attr_name = args[2]
                attr_value = args[3]
                setattr(instance, attr_name, attr_value)
                instance.save()
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
