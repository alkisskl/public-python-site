from flask import Flask
import sys
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/hostname")
def hostname():
    hostname = os.system("hostname")
    return hostname