#!/usr/bin/python3
import sys
import cmd 

if not sys.stdin.isatty():
    print()
    
class MyConsole(cmd.Cmd):
    prompt = ">>"
    
    def exitloop(self):
        sys.exit()

if __name__ == "__main__":
    MyConsole().cmdloop()