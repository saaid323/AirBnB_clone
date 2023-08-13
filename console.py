#!/usr/bin/python3
""" Console for HBNB project """

import cmd
import shlex
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

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

class HBNBCommand(cmd.Cmd):
    """ Command line interpreter for HBNB project """
    prompt = '(hbnb) '

    def _parse_key_value_args(self, args):
        """ Parse arguments in key=value format """
        kv_args = {}
        for arg in args:
            if "=" in arg:
                key, value = arg.split('=', 1)
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except ValueError:
                        try:
                            value = float(value)
                        except ValueError:
                            continue
                kv_args[key] = value
        return kv_args

    def _get_instance_key(self, class_name, instance_id):
        """ Get the instance key in storage """
        return "{}.{}".format(str(class_name), instance_id)

    def do_create(self, arg):
        """ Create a new instance of a class """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name in CLASSES:
            kv_args = self._parse_key_value_args(args[1:])
            instance = CLASSES[class_name](**kv_args)
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ Print string representation of an instance """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name in CLASSES:
            if len(args) > 1:
                instance_key = self._get_instance_key(class_name, args[1])
                instances = models.storage.all()
                if instance_key in instances:
                    print(instances[instance_key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


    def do_all(self, args):
        """Prints string representations of instances"""
        args = _parse_key_value_args(args)
        if len(args) == 0:
           instances = [str(obj) for obj in storage.all().values()]
        elif args[0] in CLASSES:
             instances = [str(obj) for obj in storage.all().values() if obj.__class__.__name__ == args[0]]
        else:
            print("** class doesn't exist **")
        return False
        print("[", end="")
        print(", ".join(instances), end="")
        print("]")

    def do_update(self, arg):
        """Update an instance based on the class name, id, attribute & value"""
        args = parse(arg)
        if len(args) == 0:
           print("** class name missing **")
        elif args[0] in CLASSES:
             if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in storage.all().values():
                   if len(args) > 2:
                      attribute = args[2]
                      try:
                         value = int(args[3])
                      except ValueError:
                          try:
                             value = float(args[3])
                          except ValueError:
                              value = args[3]
                      setattr(storage.all()[k], attribute, value)
                      storage.save()
                   else:
                       print("** attribute name missing **")
                else:
                    print("** no instance found **")
             else:
                 print("** instance id missing **")
        else:
            print("** class doesn't exist **")


    def do_destroy(self, arg):
        """Deletes an instance based on the class and id"""
        args = parse(arg)
        if len(args) == 0:
           print("** class name missing **")
        elif args[0] in CLASSES:
           if len(args) > 1:
              k = args[0] + "." + args[1]
              if k in storage.all().values():
                 del storage.all()[k]
                 storage.save()
              else:
                  print("** no instance found **")
           else:
               print("** instance id missing **")
        else:
            print("** class doesn't exist **")


    def do_EOF(self, arg):
        """Exits console"""
        return True

    def emptyline(self):
        """the emptyline method """
        return False

    def do_quit(self, arg):
        """Quits the command to exit program"""
        return True
# Start the command line interpreter
if __name__ == "__main__":
    HBNBCommand().cmdloop()
