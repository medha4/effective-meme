# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import shout


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    props = {
        "title":"Day 8 of Fintech",
        "name":"Medha"
    }
    return render_template('index.html',props=props)

@app.route('/secret')
def secret():
    return "you found the secret"

@app.route('/sendBreakfast', methods = ['GET','POST'])
def sendBreakfast():
    if request.method == 'GET':
        return "you are getting"
    elif request.method == 'POST':
        props = request.form
        return render_template('results.html',props=props)
    else:
        "you've tried to do something outside the scope lol"


