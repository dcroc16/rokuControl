from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def welcome():
    r = requests.post('http://10.0.1.88:8060/keypress/Home')
    return "Hello World"

@app.route('/Home')
def Home():
    r = requests.post('http://10.0.1.88:8060/keypress/Home')
    return "Hello World"

@app.route('/Netflix')
def Netflix():
	requests.post('http://10.0.1.88:8060/keypress/Home')
	requests.post('http://10.0.1.88:8060/launch/12')
	requests.post('http://10.0.1.88:8060/keypress/Down')
	requests.post('http://10.0.1.88:8060/keypress/Select')
	requests.post('http://10.0.1.88:8060/keypress/Lit_N')
	requests.post('http://10.0.1.88:8060/keypress/Lit_C')
	requests.post('http://10.0.1.88:8060/keypress/Lit_I')
	requests.post('http://10.0.1.88:8060/keypress/Lit_S')
        return "<img src='http://10.0.1.88:8060/query/icon/12' />"

@app.route('/Music')
def Music():
    r = requests.post('http://10.0.1.88:8060/launch/28')
    r.end()



    return "Hello World"


app.run()
