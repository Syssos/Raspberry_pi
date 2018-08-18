#!/usr/bin/env python3
# LED light to indicate internet access
from urllib.request import urlopen, URLError
from gpiozero import LED
from time import sleep


def internet_on():
    try:
        urlopen('http://216.58.192.142', timeout=1)
        return True
    except URLError as err:
        return False

if __name__ == "__main__":

    led = LED(11)

    while True:
        test = internet_on()
        if (test == False):
            pass
        else:
            led.on()
            sleep(1)
            led.off()
            sleep(1)
