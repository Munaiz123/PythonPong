import RPi.GPIO as GPIO
import time

def redFlicker():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(18, GPIO.OUT)
	GPIO.output(18, GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(18, GPIO.LOW)


	GPIO.cleanup 


def greenFlicker():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(23, GPIO.OUT)
	GPIO.output(23, GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(23, GPIO.LOW)


	GPIO.cleanup 
