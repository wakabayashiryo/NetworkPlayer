# index.html must put floder into templates
# Accessing URL is http://volumio.local:8080/ 
# neccessary packages:
# sudo apt-get install python3-rpi.gpio
# sudo apt-get install python3-flask
# sudo apt-get install python3-pip
# sudo pip install flask-bootstrap

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
	return render_template("./index.html")
	
if __name__ == "__main__":
	app.debug = True
	app.run(host="0.0.0.0",port=8080)
