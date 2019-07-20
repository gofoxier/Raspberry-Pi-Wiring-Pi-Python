#!/usr/bin/env python
import wiringpi as piwiring
import time

# must run in sudo right
GPIO_pos = 18


def setup():
    piwiring.wiringPiSetupGpio()
    piwiring.pinMode(GPIO_pos, piwiring.PWM_OUTPUT)
    # piwiring.pwmSetRange(1024)
    # piwiring.pwmSetClock(1000)
    piwiring.pwmWrite(GPIO_pos, 0)


def loop():
    while True:
        for dc in range(0, 101, 4):   # Increase duty cycle: 0~100
            piwiring.pwmWrite(GPIO_pos, dc)     # Change duty cycle
            time.sleep(0.05)
        time.sleep(1)
        for dc in range(100, -1, -4): # Decrease duty cycle: 100~0
            piwiring.pwmWrite(GPIO_pos, dc)
            time.sleep(0.05)
        time.sleep(1)


def destroy():
    piwiring.pwmWrite(GPIO_pos, 0)


if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()