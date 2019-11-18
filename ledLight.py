import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)



def redFlicker():
	GPIO.output(18, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(18, GPIO.LOW)
	

def greenFlicker():
	GPIO.output(23, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(23, GPIO.LOW)



#~ while True:
	#~ redFlicker()
	#~ greenFlicker()
	#~ time.sleep(.75)
	
#~ GPIO.cleanup()

