#!/usr/bin/python3
"""
Defines the HBnB console.
"""

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """
    Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        arg_parts = split(arg)
        if "." in arg_parts[0]:
            first_part, second_part = arg_parts[0].split(".", 1)
            match = re.search(r"\((.*?)\)", second_part)
            if match:
                command = [first_part, match.group()[1:-1]]
                argdict = {
                    "all": self.do_all,
                    "show": self.do_show,
                    "destroy": self.do_destroy,
                    "count": self.do_count,
                    "update": self.do_update
                }
                if command[0] in argdict:
                    call = f"{arg_parts[0]} {command[1]}"
                    return argdict[command[0]](call)
        print(f"* Unknown syntax: {arg}")
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """
        Usage: create <class>
        Create a new class instance and print its id.
        """
        arg_parts = split(arg)
        if not arg_parts:
            print("* class name missing *")
        elif arg_parts[0] not in HBNBCommand.__classes:
            print("* class doesn't exist *")
        else:
            new_instance = eval(arg_parts[0])()
            new_instance.save()
            print(new_instance.id)

    # Rest of the methods...

if _name_ == "_main_":
    HBNBCommand().cmdloop()
