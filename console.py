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
    HBNBCommand().cmdloop()
