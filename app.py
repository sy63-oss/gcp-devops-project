from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, Simple Flask application"
https://github.com/hediet/vscode-drawio/raw/HEAD/docs/demo.gif