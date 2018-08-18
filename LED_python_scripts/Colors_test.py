#!/usr/bin/env python3
import cmd
from Colors import colors
from time import sleep


class LEDcontrol(cmd.Cmd):

    prompt = ("LED ~:$ ")
    
    def do_yellowblink(self, args):
        yel = colors.yellow()
        while True:
            colors.turn_on(yel)
            sleep(1)
            colors.turn_off(yel)
            sleep(1)
        return 1

if __name__ == "__main__":
    LEDcontrol().cmdloop()
