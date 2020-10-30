from flask import Flask

app = Flask(__name__)


@app.route('/')

def index():
    return "!!New ** Hello *** World!!"


@app.route('/marcos')

def marcos():
    return "!!***New  Hello Marcos Ataka***!!"