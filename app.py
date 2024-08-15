# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to Carl and Katelyn's Wedding Quiz</h1>"

if __name__ == '__main__':
    app.run()

