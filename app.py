from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/hostname")
def hostname():
    hostname = os.system("hostname")
    print(hostname)
    return "hostname"

if __name__ == '__main__':
   app.run()