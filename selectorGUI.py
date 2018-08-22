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

import RPi.GPIO as GPIO
from flask import Flask, render_template,request
import time

app = Flask(__name__)
	
Channel1 = 17
Channel2 = 27
Channel3 = 22

def main():
	GPIO.setmode(GPIO.BCM)
	
	GPIO.setup(Channel1,GPIO.OUT)
	GPIO.setup(Channel2,GPIO.OUT)
	GPIO.setup(Channel3,GPIO.OUT)

	GPIO.output(Channel1,GPIO.HIGH)

	app.debug = True
	app.run(host="0.0.0.0",port=8080)

@app.route("/",methods=["GET","POST"])

def index():#ブラウザーからアクセスした時にGUI画面を返す
	if request.method == 'GET':
		return render_template("./index.html")
	else:#ラジオボタンから取得した文字列を抽出
		get_value = request.form["options"]
		if get_value is 'channel1':
			GPIO.output(Channel1,GPIO.HIGH)
			GPIO.output(Channel2,GPIO.LOW)
			GPIO.output(Channel3,GPIO.LOW)
		elif get_value is 'channel2':
			GPIO.output(Channel1,GPIO.LOW)
			GPIO.output(Channel2,GPIO.HIGH)
			GPIO.output(Channel3,GPIO.LOW)
		elif get_value is 'channel3':
			GPIO.output(Channel1,GPIO.LOW)
			GPIO.output(Channel2,GPIO.LOW)
			GPIO.output(Channel3,GPIO.HIGH)
		return 'success!'

if __name__ == '__main__':
	main()
	GPIO.cleanup()

