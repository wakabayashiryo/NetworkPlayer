import RPi.GPIO as GPIO
import time

if __name__ == '__main__':
	Channel1 = 17
	Channel2 = 22
	Channel3 = 27

	GPIO.setmode(GPIO.BCM)

	GPIO.setup(Channel1,GPIO.OUT)
	GPIO.setup(Channel2,GPIO.OUT)
	GPIO.setup(Channel3,GPIO.OUT)

	GPIO.output(Channel2,GPIO.HIGH)

	time.sleep(5)     
	GPIO.cleanup()
