import RPi.GPIO as GPIO
import time
import ledLight

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#~ GPIO.cleanup()

TRIG = 2
ECHO = 21

RED = 18
GREEN = 23

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)



def getDistance():
	GPIO.output(TRIG,True)
	time.sleep(0.0001)
	GPIO.output(TRIG,False)
	
	while GPIO.input(ECHO) == False:
		start = time.time()
	
	while GPIO.input(ECHO) == True:
		end = time.time()
		
	totalTime = end - start
	
	inches = totalTime/ 0.000148
	cm = totalTime / 0.000058
	
	print('INCHES: {}, CM: {}'.format(inches,cm))
	
	return inches
	
	


while True:
	distance = getDistance()
	time.sleep(1)
	
	if distance < 6:
		#~ ledLight.redFlicker()
		GPIO.output(RED, GPIO.HIGH)
	elif distance > 6:
		GPIO.output(RED, GPIO.LOW)
		ledLight.greenFlicker()


GPIO.cleanup()
