from flask import Flask, render_template
import requests
import time

roku_path = 'http://10.0.1.88:8060'

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/Home')
def Home():
	requests.post(roku_path + '/keypress/Home')
	return render_template('index.html')

@app.route('/Netflix')
def Netflix():
	requests.post(roku_path + '/keypress/Home')
	requests.post(roku_path + '/launch/12')
	#time.sleep(30)
	#requests.post(roku_path + '/keypress/Search')
	#time.sleep(10)
	#requests.post(roku_path + '/keypress/Lit_N')
	#requests.post(roku_path + '/keypress/Lit_C')
	#requests.post(roku_path + '/keypress/Lit_I')
	#requests.post(roku_path + '/keypress/Lit_S')
	#requests.post(roku_path + '/keypress/Down')
	#requests.post(roku_path + '/keypress/Right')
	#requests.post(roku_path + '/keypress/Right')
	#requests.post(roku_path + '/keypress/Right')
	#requests.post(roku_path + '/keypress/Right')
	#requests.post(roku_path + '/keypress/Enter')

	return render_template('index.html')

@app.route('/Pandora')
def Pandora():
	requests.post(roku_path + '/launch/28')
	return render_template('index.html')

@app.route('/Hulu')
def Hulu():
	requests.post(roku_path + '/launch/2285')
	return render_template('index.html')

@app.route('/Vudu')
def Vudu():
	requests.post(roku_path + '/launch/13842')
	return render_template('index.html')

@app.route('/AmazonVideo')
def AmazonVideo():
	requests.post(roku_path + '/launch/13')
	return render_template('index.html')

@app.route('/AmazonMusic')
def AmazonMusic():
	requests.post(roku_path + '/launch/14362')
	return render_template('index.html')

@app.route('/Up')
def Up():
	requests.post(roku_path + '/keypress/Up')
	return render_template('index.html')

@app.route('/Down')
def Down():
	requests.post(roku_path + '/keypress/Down')
	return render_template('index.html')

@app.route('/Left')
def Left():
	requests.post(roku_path + '/keypress/Left')
	return render_template('index.html')

@app.route('/Ok')
def Ok():
	requests.post(roku_path + '/keypress/Select')
	return render_template('index.html')

@app.route('/Right')
def Right():
	requests.post(roku_path + '/keypress/Right')
	return render_template('index.html')

@app.route('/Play')
def Play():
	requests.post(roku_path + '/keypress/Play')
	return render_template('index.html')

@app.route('/Back')
def Back():
	requests.post(roku_path + '/keypress/Back')
	return render_template('index.html')


app.run()
