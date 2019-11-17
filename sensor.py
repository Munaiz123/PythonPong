import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 2
ECHO = 21

RED = 18
GREEN = 23

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)



GPIO.output(TRIG,False)
time.sleep(1)

GPIO.output(TRIG,True)
time.sleep(0.0001)
GPIO.output(TRIG,False)

print('START')

try:
	while True:

		while GPIO.input(ECHO) == 0:
			start = time.time()
			
		while GPIO.input(ECHO) == 1:
			end = time.time()

		total = end - start


		cm = total/0.000058
		inches = total/0.000148
		
		print('inches: {} && cm: {}'.format(inches,cm))			
			
		if inches < 6:
			GPIO.output(RED, GPIO.HIGH)
			GPIO.output(GREEN, GPIO.LOW)
		if inches > 6:
			GPIO.output(RED, GPIO.LOW)
			#~ GPIO.output(GREEN, GPIO.LOW)
			GPIO.output(GREEN, GPIO.HIGH)
			
			
			
except KeyboardInterrupt:
	print('Cleaning Up')
	GPIO.cleanup()
