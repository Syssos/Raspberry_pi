#!/usr/bin/env python3
from gpiozero import LED


class colors():
    """
    """
    def white():
        white = LED(17)
        return white

    def blue():
        blue = LED(11)
        return blue

    def yellow():
        yellow = LED(12)
        return yellow

    def turn_on(LED):
        LED.on()
        return 1

    def turn_off(LED):
        LED.off()
        return 1
