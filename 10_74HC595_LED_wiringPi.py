#!/usr/bin/env python
# ================================================
#
#	This program is for SunFounder SuperKit for Rpi.
#
#	Extend use of 8 LED with 74HC595.
#
#	Change the	WhichLeds and sleeptime value under
#	loop() function to change LED mode and speed.
#
# =================================================

import wiringpi as piwiring
import time

SDI = 0
RCLK = 1
SRCLK = 2

# ===============   LED Mode Defne ================
#	You can define yourself, in binay, and convert it to Hex
#	8 bits a group, 0 means off, 1 means on
#	like : 0101 0101, means LED1, 3, 5, 7 are on.(from left to right)
#	and convert to 0x55.

LED0 = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]  # original mode
LED1 = [0x01, 0x03, 0x07, 0x0f, 0x1f, 0x3f, 0x7f, 0xff]  # blink mode 1
LED2 = [0x01, 0x05, 0x15, 0x55, 0xb5, 0xf5, 0xfb, 0xff]  # blink mode 2
LED3 = [0x02, 0x03, 0x0b, 0x0f, 0x2f, 0x3f, 0xbf, 0xff]  # blink mode 3


# =================================================

def print_msg():
	print('Program is running...')
	print('Please press Ctrl+C to end the program...')


def setup():
	piwiring.wiringPiSetup()
	piwiring.pinMode(SDI, piwiring.OUTPUT)
	piwiring.pinMode(RCLK, piwiring.OUTPUT)
	piwiring.pinMode(SRCLK, piwiring.OUTPUT)
	piwiring.digitalWrite(SDI, piwiring.LOW)
	piwiring.digitalWrite(RCLK, piwiring.LOW)
	piwiring.digitalWrite(SRCLK, piwiring.LOW)


def hc595_in(dat):
	for bit in range(0, 8):
		piwiring.digitalWrite(SDI, 0x80 & (dat << bit))
		piwiring.digitalWrite(SRCLK, piwiring.HIGH)
		time.sleep(0.001)
		piwiring.digitalWrite(SRCLK, piwiring.LOW)



def hc595_out():
	piwiring.digitalWrite(RCLK, piwiring.HIGH)
	time.sleep(0.001)
	piwiring.digitalWrite(RCLK, piwiring.LOW)


def loop():
	WhichLeds = LED0  # Change Mode, modes from LED0 to LED3
	sleeptime = 0.1  # Change speed, lower value, faster speed
	while True:
		for i in range(0, len(WhichLeds)):
			hc595_in(WhichLeds[i])
			hc595_out()
			time.sleep(sleeptime)

		for i in range(len(WhichLeds) - 1, -1, -1):
			hc595_in(WhichLeds[i])
			hc595_out()
			time.sleep(sleeptime)


def destroy():  # When program ending, the function is executed.
	piwiring.wiringPiSetup()


if __name__ == '__main__':  # Program starting from here
	print_msg()
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
