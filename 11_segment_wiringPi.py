import wiringpi as piwiring
import time

SDI   = 0
RCLK  = 1
SRCLK = 2

segCode = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,0x77,0x7c,0x39,0x5e,0x79,0x71,0x80]

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

def hc595_shift(dat):
	for bit in range(0, 8):
		piwiring.digitalWrite(SDI, 0x80 & (dat << bit))
		piwiring.digitalWrite(SRCLK, piwiring.HIGH)
		time.sleep(0.001)
		piwiring.digitalWrite(SRCLK, piwiring.LOW)
	piwiring.digitalWrite(RCLK, piwiring.HIGH)
	time.sleep(0.001)
	piwiring.digitalWrite(RCLK, piwiring.LOW)

def loop():
	while True:
		for i in range(0, len(segCode)):
			hc595_shift(segCode[i])
			time.sleep(0.5)

def destroy():   #When program ending, the function is executed.
	piwiring.wiringPiSetup()

if __name__ == '__main__': #Program starting from here
	print_msg()
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
