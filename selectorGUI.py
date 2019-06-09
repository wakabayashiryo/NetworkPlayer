# index.html must put floder into templates
# Accessing URL is http://volumio.local:8080/ 
# neccessary packages:
# sudo apt-get install python3-rpi.gpio
# sudo apt-get install python3-flask
# sudo apt-get install python3-pip

# Raspberry PI pin(BCM) ---> selector channel
# No.17  ---> channel1
# No.27  ---> channel2
# No.22  ---> channel3

# Power button and control LED
# No.3   ---> SW
# No.4   ---> LED

import RPi.GPIO as GPIO
from flask import Flask, render_template,request
import time
import os

app = Flask(__name__)
	
Channel1 = 17
Channel2 = 27
Channel3 = 22

Switch = 3
Led    = 4

def buttonEvent(channel1):
    # sysytem shutdown with "Wake From Halt Function"
    os.system("sudo shutdown -h now")

def main():
	GPIO.setmode(GPIO.BCM)
	
	GPIO.setup(Channel1,GPIO.OUT)
	GPIO.setup(Channel2,GPIO.OUT)
	GPIO.setup(Channel3,GPIO.OUT)

	#default channel is 1
	GPIO.output(Channel1,GPIO.HIGH)
	# The led includ in SW
	GPIO.setup(Led,GPIO.OUT)
	GPIO.output(Led,GPIO.HIGH)

	#GPIO3(No.5) is input.
	GPIO.setup(Switch,GPIO.IN)
	GPIO.add_event_detect(Switch, GPIO.FALLING, callback=buttonEvent, bouncetime=300) 

	app.debug = True
	app.run(host="0.0.0.0",port=8080)

@app.route("/",methods=["GET","POST"])
def index():
	if request.method == 'GET':#get request is GET when browser accessed
		return render_template("./index.html")
	else:#get request is POST when radio button is changed
		channelNo = request.form["options"]
		if channelNo is '1':
			GPIO.output(Channel1,GPIO.HIGH)
			GPIO.output(Channel2,GPIO.LOW)
			GPIO.output(Channel3,GPIO.LOW)
		elif channelNo is '2':
			GPIO.output(Channel1,GPIO.LOW)
			GPIO.output(Channel2,GPIO.HIGH)
			GPIO.output(Channel3,GPIO.LOW)
		elif channelNo is '3':
			GPIO.output(Channel1,GPIO.LOW)
			GPIO.output(Channel2,GPIO.LOW)
			GPIO.output(Channel3,GPIO.HIGH)
		return 'success!'

if __name__ == '__main__':
	main()
	GPIO.cleanup()

