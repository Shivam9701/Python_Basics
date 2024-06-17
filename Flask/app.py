from flask import Flask, request, jsonify

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/')
def welcome():
    return 'Welcome the API'

from controller import *