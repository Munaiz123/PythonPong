import RPi.GPIO as GPIO
import time

def flicker():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(18, GPIO.OUT)
	GPIO.output(18, GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(18, GPIO.LOW)


	GPIO.cleanup

def test():
	print('TESTING FROM LEDLIGHT.PY')
