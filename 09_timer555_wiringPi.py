#!/usr/bin/env python
import wiringpi as piwiring


SigPin = 0    # pin11

g_count = 0

def count(ev=None):
	global g_count
	g_count += 1

def setup():
	piwiring.wiringPiSetup()
	piwiring.pinMode(SigPin, piwiring.INPUT)
	piwiring.pullUpDnControl(SigPin, piwiring.PUD_UP)    # Set Pin's mode is input, and pull up to high level(3.3V)
	piwiring.wiringPiISR(SigPin, piwiring.INT_EDGE_RISING, count)  # wait for falling

def loop():
	while True:
		print('g_count = %d' % g_count)

def destroy():
	piwiring.wiringPiSetup()    # reset   # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

