#!/usr/bin/env python3
from gpiozero import LED
from time import sleep
from signal import pause


class colors():
    """
    """
    def getcolor(self, arg):
        if (arg == "yellow"):
            return LED(12)
        elif (arg == "blue"):
            return LED(11)
        elif (arg == "white"):
            return LED(17)
        else:
            print ("please enter a valid color")

    def flash(self):
        print (self)
        self.blink()


    def turn_on_or_off(self, arg):
        if (arg == "on"):
            self.on()
        elif (arg == "off"):
            self.off()
        else:
            print ("Please enter on or off")

