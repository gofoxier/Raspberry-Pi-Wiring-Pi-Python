#!/usr/bin/env python
import wiringpi as piwiring
import time

# must run in sudo right
GPIO_pos = 17


def setup():
    piwiring.wiringPiSetupGpio()
    piwiring.pinMode(GPIO_pos, piwiring.OUTPUT)
    piwiring.digitalWrite(GPIO_pos, piwiring.LOW)


def loop():
    while True:
        piwiring.digitalWrite(GPIO_pos, piwiring.LOW)
        time.sleep(0.5)
        piwiring.digitalWrite(GPIO_pos, piwiring.HIGH)
        time.sleep(0.5)

def destroy():
    piwiring.digitalWrite(GPIO_pos, piwiring.LOW)


if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()