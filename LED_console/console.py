#!/usr/bin/env python3
import cmd
from models.Colors import colors
from time import sleep
from gpiozero import *

class LEDcontrol(cmd.Cmd):

    prompt = ("LED ~:$ ")
    __light = LED(0)
    __color = ""
    
    def do_quit(self, args):
        ''' Quit command to exit the program.
        '''
        return True

    def do_EOF(self, args):
        ''' Exits after receiving the EOF signal.
        '''
        print ("Goodbye")
        return True

    def emptyline(self):
        ''' Prevents printing anything when an empty line is passed.
        '''
        pass

    def do_select(self, args):
        if (self.__color == args):
            print ("color already selected")
        else:
            self.__light = colors.getcolor(self, args)
        self.__color = args

    def do_power(self, args):
        if args is None:
            print ("please enter an option")
        else:
            colors.turn_on_or_off(self.__light, args)

    def do_blink(self, args):
        colors.flash(self.__light)

    def default(self, args):
        ''' Catches all the function names that are not expicitly defined.
        '''
        functions = {"select": self.do_select, "power": self.do_power,
                     "blink": self.do_blink}
        args = (args.replace("(", ".").replace(")", ".")
                .replace('"', "").replace(",", "").split("."))
        
        try:
            cmd_arg = args[0] + " " + args[2]
            func = functions[args[1]]
            func(cmd_arg)
        except BaseException:
            print("Unknown LED cmd:", args[0])

    def do_internet(self, args):
        test = colors.internet_on()
        if (test == False):
            pass
        else:
            colors.flash(self.__light)

    def do_stop(self, args):
        colors.execstop(self.__light)
        
if __name__ == "__main__":
    LEDcontrol().cmdloop()
