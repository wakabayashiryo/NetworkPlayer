# index.html must put floder into templates
# Accessing URL is http://volumio.local:8080/ 
# neccessary packages:
# sudo apt-get install python3-rpi.gpio
# sudo apt-get install python3-flask
# sudo apt-get install python3-pip
# sudo pip install flask-bootstrap

import RPi.GPIO as GPIO
from flask import Flask, render_template
import time

@app.route("/",methods=["GET","POST"])
def index():
	return render_template("./index.html")

def main():
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

	app = Flask(__name__)
	
	app.debug = True
	app.run(host="0.0.0.0",port=8080)

if __name__ == '__main__':
	main()
