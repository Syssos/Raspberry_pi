#!/usr/bin/env python3
import cmd
from Colors import colors
from time import sleep
from gpiozero import LED

class LEDcontrol(cmd.Cmd):

    prompt = ("LED ~:$ ")
    __light = LED(0)

    def do_quit(self, args):
        ''' Quit command to exit the program.
        '''
        return True

    def do_EOF(self, args):
        ''' Exits after receiving the EOF signal.
        '''
        return True

    def emptyline(self):
        ''' Prevents printing anything when an empty line is passed.
        '''
        pass

    def do_select(self, args):
       self.__light = colors.getcolor(self, args)

    def do_power(self, args):
        if args is None:
            print ("please enter an option")
        else:
            colors.turn_on_or_off(self.__light, args)

    def do_blink(self, args):
        colors.flash(self.__light)


if __name__ == "__main__":
    LEDcontrol().cmdloop()
