#!/usr/bin/env python3
from gpiozero import LED
from time import sleep

ledred = LED(21)
ledwhite = LED(17)
ledblue = LED(11)

while True:
    ledred.on()
    ledwhite.on()
    ledblue.on()
    sleep(1)
    ledred.off()
    ledwhite.off()
    ledblue.off()
    sleep(1)
