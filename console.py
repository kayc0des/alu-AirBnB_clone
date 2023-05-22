import cmd
import sys


class MyCmd(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, line):
        """
        Exits the command loop
        """
        return True
    
    def do_EOF(self, arg):
        """Handle the end of input.

        This function is called when the user enters the end-of-file command.
        It will exit the command-line interpreter.
        """
        print("Exiting...")
        return True
    
    def emptyline(self):
        """Handle an empty line.

        This function is called when the user enters an empty line.
        It does nothing in this implementation.
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