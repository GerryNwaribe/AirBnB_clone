#!/usr/bin/env python3
""" This is a simple console application that allows the user to enter a number and"""


import cmd
import models.base_model


class HBNBCommand(cmd.Cmd):
  """This class inherits from the cmd.Cmd class and defines the cmm that can be exe"""
  prompt = "(hbnb) "
  cls_name = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

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
    if not arg:  # If the class name is missing
      print("** class name missing **")
    elif arg not in self.cls_name:
      print("** class doesn't exist **")
    else:
      obj = models.base_model.BaseModel() # Creates a new instance of BaseModel
      obj.save()  # saves it (to the JSON file) and prints the id
      print(obj.id)

  def do_show(self, arg):
    """Prints the string representation of an instance based on the class name and id"""
    _x = arg.split()
    _r = [x.strip() for x in _x]
    if not _r:  # If the class name is missing
      print("** class name missing **")
    elif _r[0] not in self.cls_name:
      print("** class doesn't exist **")
    else:
      obj = models.base_model.BaseModel()
      obj.id = _r[1]
      obj.save()
      print(obj.__dict__)
    
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
    """Prints all string representation of all instances based on the class name"""
    _x  = arg.split()
    _r = [x.strip() for x in _x]
    if arg:
      if _r[0] not in self.cls_name:
        print("** class doesn't exist **")
        return
    x = [str(obj) for obj in models.storage.all().values()]   # A list of strings
    print(x)

  def do_update(self, arg):
    """Updates an instance based on the class name and id"""
    # update <class name>   <id>                   <attribute name>   "<attribute value>"
    # update BaseModel      49faff9a-910505c55907  first_name         "Betty"
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
  HBNBCommand().cmdloop()