# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, CI/CD with GitHub Actions!"

if __name__ == '__main__':
    app.run()
