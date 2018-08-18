#!/usr/bin/env python3
from gpiozero import LED
from time import sleep


def colors():
    white = LED(17)
    yellow = LED(12)
    blue = LED(11)

    print("Usage: Enter color of LED to change")
    while True:
        var_c = input("$")
        if (var_c == "white"):
            var_o = input("on or off?")
            if (var_o == "on"):
                white.on()
            if (var_o == "off"):
                white.off()
        elif (var_c == "blue"):
            var_o = input("on or off?")
            if (var_o == "on"):
                blue.on()
            if (var_o == "off"):
                blue.off()
        elif (var_c == "yellow"):
            var_o = input("on or off?")
            if (var_o == "on"):
                yellow.on()
            if (var_o == "off"):
                yellow.off()
        elif (var_c == "exit"):
            print ("goodbye")
            return            
        else:
            print ('error')

if __name__ == "__main__":
    colors()
