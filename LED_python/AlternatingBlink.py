#!/usr/bin/env python3
from gpiozero import LED
from time import sleep

ledred = LED(21)
ledwhite = LED(17)
ledgreen = LED(11)

while True:
    ledred.on()
    sleep(1)
    ledwhite.on()
    sleep(1)
    ledred.off()
    ledgreen.on()
    sleep(1)
    ledwhite.off()
    sleep(1)
    ledgreen.off()
