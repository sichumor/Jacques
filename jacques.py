# Golem meant to help with meal planning
import rolodex as cl
import datetime
from random import choice

# This is a generic class for the command-line bots
# I wanted to design. I called them Golems. Jacques
# was a cooking Golem, there was one I'd use to
# register the miles I walked each day, and another
# to log personal journal entries. You get the idea.
# The class below is very basic: it was to be used
# for all the Golems, with the real nuts and bolts
# happening in their command-line files. Jacques'
# is called 'rolodex', which is imported above.
class Golem:
    def __init__(self,name):
        self.name = name
        self.commands = {}

    def greeting(self):
        cl.generate_greeting()

    def farewell(self):
        cl.generate_farewell()

    # Each golem has a dictionary that maps a keyword
    # (like 'help') to a function. Type the keyword,
    # execute the function. This routine keeps executing
    # keyword commands until the user types 'dismiss'.
    def loop(self):
        self.greeting()
        command = ""
        while command != "dismiss":
            command = input("(command) ")
            if command not in self.commands and command != "dismiss":
                cl.message("Sorry, I don't understand that.",0.8)
            else:
                self.commands[command](self)
        self.farewell()

# summon golem with given name
def load_golem(name):
    golem = Golem(name)
    # command list will be defined in the command list file
    golem.commands = cl.load_commands()
    return golem

if __name__ == "__main__":
    golem = load_golem('Jacques')
    golem.loop()
