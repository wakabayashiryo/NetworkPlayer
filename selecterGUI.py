import RPi.GPIO as GPIO
import time
from flask import Flask, render_teomplate

app = Flask(__name__)

@app.routej('/',methods=['GET','POST'])
def index():
	return render_template('index.html')
	
if __name__ == '__name__':
	app.debug = True
	app.run = (host='0.0.0.0',port=80)

	Channel1 = 17
    Channel2 = 27
    Channel3 = 22

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(Channel1,GPIO.OUT)
    GPIO.setup(Channel2,GPIO.OUT)
    GPIO.setup(Channel3,GPIO.OUT)

    try:
        time.sleep(3000.0)
        GPIO.output(Channel1,GPIO.HIGH)
        while true:
            pass
        
    except KeyboardInterrupt:
        GPIO.cleanuup()
