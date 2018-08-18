#!/usr/bin/env python3
from gpiozero import *
from time import sleep
from signal import pause
from urllib.request import urlopen, URLError


class colors():
    """
    """
    def getcolor(self, arg):
        if (arg == "yellow"):
            try:
                return LED(12)
            except exc.GPIOPinInUse as error:
                print("in use")
        elif (arg == "blue"):
            try:
                return LED(11)
            except exc.GPIOPinInUse as error:
                print("in use")
        elif (arg == "white"):
            try:
                return LED(17)
            except exc.GPIOPinInUse as error:
                print("in use")
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

    def internet_on():
        try:
            urlopen('http://216.58.192.142', timeout=1)
            return True
        except URLError as err:
            return False

    def execstop(self):
        self.off()
        print("LED stopped")
        
