import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def redFlicker():
	GPIO.setup(18, GPIO.OUT)
	GPIO.output(18, GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(18, GPIO.LOW)
	

def greenFlicker():
	GPIO.setup(23, GPIO.OUT)
	GPIO.output(23, GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(23, GPIO.LOW)

GPIO.cleanup()
