<<<<<<< HEAD
#!/usr/bin/python3
""" This is a simple console application"""


import cmd
import models.base_model


class HBNBCommand(cmd.Cmd):
    """This class inherits from the cmd.Cmd class
    and defines the cmmd"""
    prompt = "(hbnb) "
    cls_name = ["BaseModel", "User", "State",
                "City", "Amenity", "Place", "Review"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Handles EOF (Ctrl+D) to exit the program"""
        print()
        return True

    def emptyline(self):
        """Empty line should do nothing"""
        pass

    def do_create(self, arg):
        """Creates a new instance of a class based on the argument passed"""
        _x = arg.strip()
        _r = [x.strip() for x in _x]
        if not arg:
            print("** class name missing **")
        elif arg not in self.cls_name:
            print("** class doesn't exist **")
        else:
            obj = models.base_model.BaseModel()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id"""
        _x = arg.split()
        _r = [x.strip() for x in _x]

        if len(_r) < 1:
            print("** class name missing **")
        elif _r[0] not in self.cls_name:
            print("** class doesn't exist **")
        elif len(_r) < 2:
            print("** instance id missing **")
        elif f"{_r[0]}.{_r[1]}" not in models.storage.all().keys():
            print("** no instance found **")
        else:
            obj = models.storage.all()[f"{_r[0]}.{_r[1]}"]
        print(obj)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        _x = arg.split()
        _r = [x.strip() for x in _x]
        if len(_r) < 1:
            print("** class name missing **")
        elif _r[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(_r) < 2:
            print("** instance id missing **")
        elif f"{_r[0]}.{_r[1]}" not in models.storage.all().keys():
            print("** no instance found **")
        else:
            models.storage.all().pop(f"{_r[0]}.{_r[1]}")
        models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based on the class name"""
        _x = arg.split()
        _r = [x.strip() for x in _x]
        if arg:
            if _r[0] not in self.cls_name:
                print("** class doesn't exist **")
            return
        x = [str(obj) for obj in models.storage.all().values()]
        print(x)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""

        _x = arg.split()
        _r = [x.strip() for x in _x]
        _l = len(_r)
        if _l < 1:
            print("** class name missing **")
        elif _r[0] not in self.cls_name:
            print("** class doesn't exist **")
        elif _l < 2:
            print("** instance id missing **")
        elif f"{_r[0]}.{_r[1]}" not in models.storage.all().keys():
            print("** no instance found **")
        elif _l < 3:
            print("** attribute name missing **")
        elif _l < 4:
            print("** value missing **")
        else:
            obj = models.storage.all()[f"{_r[0]}.{_r[1]}"]
        obj.__setattr__(_r[2], _r[3])
        obj.save()


if __name__ == '__main__':
=======
#!/usr/bin/env python3
import cmd
import sys


if not sys.stdin.isatty():
    print()

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    
    def do_quit(self, arg):
        """Quit command to exit the program"""
        sys.exit(0)

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def do_EOF(self, arg):
        """Handle EOF (Ctrl+D) to exit the program"""
        print()
        sys.exit(0)
        
    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
        else:
            try:
                class_name = arg
                my_class = globals()[class_name]
                new_instance = my_class()
                new_instance.save()
                print(new_instance.id)
            except KeyError:
                print("** class doesn't exist **")
            
if __name__ == "__main__":
>>>>>>> 035fd5af54c8782ed23d287e1ad12b93547ca0b8
    HBNBCommand().cmdloop()
