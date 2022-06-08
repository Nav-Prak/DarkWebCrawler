#Package import
from sys import stdout
from flask import Flask, render_template, send_file, make_response, url_for, Response, redirect, request
import base64
from io import BytesIO
import subprocess
import os

script_dir = os.path.dirname(__file__)

#initialise app
app = Flask(__name__)

#Decorator for homepage
@app.route('/' )
def index():
    return render_template('index.html',
                           PageTitle = "Dark Web Crawler")

if __name__ == '__main__':
	app.run(debug = True)

#Decorator for homepage in case of POST request
@app.route('/crawl', methods = ["POST", "GET"] )
def analyse():
	name = request.form.get('char_name')
	temp = ''.join(filter(str.isalnum, name))
	temp = "output/" + temp + ".txt"
	filename = os.path.join(script_dir, temp)
	f = open(filename,"a+")
	f.flush()
	c = subprocess.Popen(["./gotor", "-l", name], stdout=f, stderr=f)

	#f.close()

	return render_template('results.html', name=name)
