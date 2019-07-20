#!/usr/bin/env python
import wiringpi as piwiring
import time


# must run in sudo right
MotorPin1 = 17
MotorPin2 = 18
MotorEnable = 27


def setup():
    piwiring.wiringPiSetupGpio()
    piwiring.pinMode(MotorPin1, piwiring.OUTPUT)
    piwiring.digitalWrite(MotorPin1, piwiring.LOW)
    piwiring.pinMode(MotorPin2, piwiring.OUTPUT)
    piwiring.digitalWrite(MotorPin2, piwiring.LOW)
    piwiring.pinMode(MotorEnable, piwiring.OUTPUT)
    piwiring.digitalWrite(MotorEnable, piwiring.LOW)
piwiring.wiringPiISR

def loop():
    while True:
        print('Motor clockwise...')
        piwiring.digitalWrite(MotorEnable, piwiring.HIGH)   # motor driver enable
        piwiring.digitalWrite(MotorPin1, piwiring.HIGH)     # clockwise
        piwiring.digitalWrite(MotorPin2, piwiring.LOW)
        time.sleep(5)

        print('Motor stop...')
        piwiring.digitalWrite(MotorEnable, piwiring.LOW)    # motor stop
        time.sleep(5)

        print('Motor anticlockwise...')
        piwiring.digitalWrite(MotorEnable, piwiring.HIGH)   # motor driver enable
        piwiring.digitalWrite(MotorPin1, piwiring.LOW)      # anticlockwise
        piwiring.digitalWrite(MotorPin2, piwiring.HIGH)
        time.sleep(5)

        print('Motor stop...')
        piwiring.digitalWrite(MotorEnable, piwiring.LOW)   # motor stop
        time.sleep(5)


def destroy():
    piwiring.digitalWrite(MotorEnable, piwiring.LOW)
    piwiring.digitalWrite(MotorPin1, piwiring.LOW)
    piwiring.digitalWrite(MotorPin2, piwiring.LOW)


if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
