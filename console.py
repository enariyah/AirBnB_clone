#!/usr/bin/python3
"""Module containing the AirBnB command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
class_names = {
    'BaseModel': BaseModel,
    'User': User,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Place': Place,
    'Review': Review
}


class HBNBCommand(cmd.Cmd):
    """Command interpreter for AirBnB clone"""
    prompt = "(hbnb) "

    def emptyline(self):
        """Does nothing"""
        pass

    def do_quit(self, line):
        """quit command exits the program"""
        return True

    def do_EOF(self, line):
        """EOF command exits the program"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        if line:
            if line in class_names:
                print(class_names[line]().id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line: str):
        """Prints the string representation of an instance"""
        if line:
            args = line.strip().split()
            if args[0] not in class_names:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = f"{args[0]}.{args[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if line:
            args = line.strip().split()
            if args[0] not in class_names:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = f"{args[0]}.{args[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()
        else:
            print("** class name missing **")

    def do_all(self, line):
        """Prints all string representation of all instances"""
        if line:
            if line not in class_names:
                print("** class doesn't exist **")
            else:
                class_dict = []
                for key, val in storage.all().items():
                    if key.startswith(line):
                        class_dict += [str(val)]
                print(class_dict)
        else:
            class_dict = []
            for key in storage.all():
                class_dict += [str(storage.all()[key])]
            print(class_dict)

    def do_update(self, line):
        """Updates an instance based on the Class name and id"""
        if line:
            args = line.strip().split()
            if args[0] not in class_names:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                key = f"{args[0]}.{args[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    setattr(storage.all()[key], args[2], args[3])
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
