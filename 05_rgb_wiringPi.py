#!/usr/bin/env python
import wiringpi as piwiring
import time


colors = [0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0xFF00FF, 0x00FFFF]
pins = {'GPIO_R': 17, 'GPIO_G': 18, 'GPIO_B': 21}  # pins is a dict


def setup():

    piwiring.wiringPiSetupGpio()
    for i in pins:
        piwiring.pinMode(pins[i], piwiring.SOFT_PWM_OUTPUT)
        piwiring.pwmWrite(pins[i], 0)

    piwiring.softPwmCreate(pins['GPIO_R'], 0, 100)
    piwiring.softPwmCreate(pins['GPIO_G'], 0, 100)
    piwiring.softPwmCreate(pins['GPIO_B'], 0, 100)



def loop():
    try:
        while True:
            for col in colors:
                setcolor(col)
                time.sleep(0.5)
    except KeyboardInterrupt:
        piwiring.pwmWrite(pins['GPIO_R'], piwiring.LOW)
        piwiring.pwmWrite(pins['GPIO_G'], piwiring.LOW)
        piwiring.pwmWrite(pins['GPIO_B'], piwiring.LOW)


def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


def setcolor(col):   # For example : col = 0x112233
    r_val = (col & 0xFF0000) >> 16  # get red value
    g_val = (col & 0x00FF00) >> 8   # get green value
    b_val = (col & 0x0000FF) >> 0   # get blue value

    r_val = map(r_val, 0, 255, 0, 100)  # change a num(0 ~255) to 0 ~100
    g_val = map(g_val, 0, 255, 0, 100)
    b_val = map(b_val, 0, 255, 0, 100)

    piwiring.softPwmWrite(pins['GPIO_R'], int(100 - r_val))  # change duty cycle
    piwiring.softPwmWrite(pins['GPIO_G'], int(100 - g_val))
    piwiring.softPwmWrite(pins['GPIO_B'], int(100 - b_val))


def destroy():
    piwiring.pwmWrite(pins['GPIO_R'], piwiring.LOW)
    piwiring.pwmWrite(pins['GPIO_G'], piwiring.LOW)
    piwiring.pwmWrite(pins['GPIO_B'], piwiring.LOW)


if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()