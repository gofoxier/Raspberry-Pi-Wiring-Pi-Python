#!/usr/bin/env python
import wiringpi as piwiring
import time

RoDTPin = 0  # pin11  Encoder Pin 1
RoCLKPin = 1  # pin12 Encoder Pin 2
RoSWPin = 2  # pin13   Push button ** this pin not connected in the diagram. Please connect the pin.

globalCounter = 0
flag = 0
Last_RoCLK_Status = 0
Current_RoCLK_Status = 0


def setup():
    piwiring.wiringPiSetup()
    piwiring.pinMode(RoDTPin, piwiring.INPUT)
    piwiring.pinMode(RoCLKPin, piwiring.INPUT)
    piwiring.pullUpDnControl(RoSWPin, piwiring.PUD_UP)
    rotaryClear()


def rotaryDeal():
    global flag
    global Last_RoCLK_Status
    global Current_RoCLK_Status
    global globalCounter

    Last_RoCLK_Status = piwiring.digitalRead(RoCLKPin)

    while not piwiring.digitalRead(RoDTPin):
        Current_RoCLK_Status = piwiring.digitalRead(RoCLKPin)
        flag = 1
    if flag == 1:
        flag = 0
        if (Last_RoCLK_Status == 0) and (Current_RoCLK_Status == 1):
            globalCounter += 1
            print('globalCounter = %d' % globalCounter)
        if (Last_RoCLK_Status == 1) and (Current_RoCLK_Status == 0):
            globalCounter -= 1
            print('globalCounter = %d' % globalCounter)


def clear(ev=None):
    global globalCounter
    globalCounter = 0
    print('globalCounter = %d' % globalCounter)
    time.sleep(1)


# Push button run "clear" event to reset the globalCounter to zero
def rotaryClear():
    piwiring.wiringPiISR(RoSWPin, piwiring.INT_EDGE_FALLING, clear)  # wait for falling


def loop():
    global globalCounter
    while True:
        rotaryDeal()

def destroy():
    piwiring.wiringPiSetup()    # reset

if __name__ == '__main__':  # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
