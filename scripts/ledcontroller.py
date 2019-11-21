#!/usr/bin/sudo /usr/bin/python

import RPi.GPIO as GPIO
import os
import time

hosts = ["8.8.8.8"] # Add other uav's IP later

def make_high(pinNum):

	GPIO.setmode(GPIO.BOARD)
	#GPIO.setwarnings(False)
	GPIO.setup(pinNum, GPIO.OUT)
	GPIO.output(pinNum, GPIO.HIGH)





def make_low(pinNum):

	GPIO.setmode(GPIO.BOARD)
	#GPIO.setwarnings(False)
	GPIO.setup(pinNum, GPIO.OUT)
	GPIO.output(pinNum, GPIO.LOW)


def main():

	global hosts
	response = None
	try:
		while True:
			positive_response_number = 0
			time.sleep(1)
			for host in hosts:
				response = os.system("ping -c 1 " + host)
                        	if response == 0:
					positive_response_number += 1
			time.sleep(1)
			if positive_response_number >= 1:
				make_low(16)	
				time.sleep(1)
				make_high(18)
				time.sleep(1)
			else:
				make_low(18)
				time.sleep(1)
				make_high(16)
				time.sleep(1)
	except KeyboardInterrupt:
		make_low(18)
		make_low(16)
		print("Interrupted")


main()




