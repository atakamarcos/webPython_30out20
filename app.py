from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')

def index():
    return render_template('index.html')


@app.route('/marcos')

def marcos():
    return "!!***New  Hello Marcos Ataka***!!"

@app.route('/<nome>')

def ola_com_nome(nome):
    return render_template('index.html', nome_pessoa = nome)

# def ola_com_nome(nome):
#    return "Hello {nome} !" como funciona isso aqui, variavel??

#@app.route('/<nome>')