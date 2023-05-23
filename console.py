import cmd
import sys


class MyCmd(cmd.Cmd):
    prompt = "(hbnb) "

<<<<<<< HEAD
    def do_quit(self, line):
=======
    def do_quit(self, arg):
>>>>>>> main
        """
        Exits the command loop
        """
        return True
<<<<<<< HEAD
    
    def do_EOF(self, arg):
        """Handle the end of input.
=======
>>>>>>> main

    def do_EOF(self, arg):
        """
        handle EOF
        """
        return True

    def emptyline(self):
        """
        Handle user empty line
        """
        pass

if __name__ == '__main__':
    # Check if input is available from a pipe
    if not sys.stdin.isatty():
        # Read each line from standard input and process it as a command
        for line in sys.stdin:
            line = line.strip()
            if line:
                MyCmd().onecmd(line)
    else:
        # Interactive mode
        MyCmd().cmdloop()
