from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, from PR environment!"

if __name__ == '__main__':
   app.run()
