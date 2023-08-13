#!/usr/bin/python3
"""This Initiates the HBnB console."""
from shlex import split
import re
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

# Dictionary to map class names to classes
CLASSES = {
    "Amenity": Amenity,
    "BaseModel": BaseModel,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}


def _parse_key_value_args(arg):
    cBraces = re.search(r"\{(.*?)\}", arg)
    sBrackets = re.search(r"\[(.*?)\]", arg)
    if cBraces is None:
        if sBrackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:sBrackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(sBrackets.group())
            return retl
    else:
        lexer = split(arg[:curlyBraces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curlyBraces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Command interpreter.
    Attrs:
        prompt: Command prompt.
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """ignore on empty line"""
        pass

    def default(self, arg):
        """Defined default behaviors"""
        argdict = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "update": self.do_update,
            "destroy": self.do_destroy,
        }
        mtch = re.search(r"\.", arg)
        if mtch is not None:
            argl = [arg[:mtch.span()[0]], arg[mtch.span()[1]:]]
            mtch = re.search(r"\((.*?)\)", argl[1])
            if mtch is not None:
                command = [argl[1][:mtch.span()[0]], mtch.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_all(self, arg):
        """KnowledgeBase: all or all <class> or <class>.all()
        returns a string rep of all instances of given class.
        If none is specified, displays all instantiated objects."""
        argl = _parse_key_value_args(arg)
        if len(argl) > 0 and argl[0] not in CLASSES:
            print("** class doesn't exist **")
        else:
            objl = []
            for o in storage.all().values():
                if len(argl) > 0 and argl[0] == o.__class__.__name__:
                    objl.append(o.__str__())
                elif len(argl) == 0:
                    objl.append(o.__str__())
            print(objl)

    def do_show(self, arg):
        """KnowledgeBase: show <class> <id> or <class>.show(<id>)
        Returns a string rep of a class instance of given id.
        """
        argl = _parse_key_value_args(arg)
        objDict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in CLASSES:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objDict:
            print("** no instance found **")
        else:
            print(objDict["{}.{}".format(argl[0], argl[1])])

    def do_create(self, arg):
        """KnowledgeBase: create <class>
        Initiates a new class instance and print its id.
        """
        argl = _parse_key_value_args(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in CLASSES:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_count(self, arg):
        """KnowledgeBase: count <class> or <class>.count()
        number of instances of a given class."""
        argl = _parse_key_value_args(arg)
        count = 0
        for o in storage.all().values():
            if argl[0] == o.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """KnowledgeBase: update <class> <id> <attribute_name>
        <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        This updates a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        argl = _parse_key_value_args(arg)
        objDict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in CLASSES:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objDict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            o = objDict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in o.__class__.__dict__.keys():
                valtype = type(o.__class__.__dict__[argl[2]])
                o.__dict__[argl[2]] = valtype(argl[3])
            else:
                o.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            o = objDict["{}.{}".format(argl[0], argl[1])]
            for i, j in eval(argl[2]).items():
                if (i in o.__class__.__dict__.keys() and
                        type(o.__class__.__dict__[i]) in {str, int, float}):
                    valtype = type(o.__class__.__dict__[i])
                    o.__dict__[i] = valtype(j)
                else:
                    o.__dict__[i] = v
        storage.save()

    def do_destroy(self, arg):
        """KnowledgeBase: destroy <class> <id> or <class>.destroy(<id>)
        This deletes a class instance of a given id."""
        argl = _parse_key_value_args(arg)
        objDict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in CLASSES:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objDict.keys():
            print("** no instance found **")
        else:
            del objDict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
