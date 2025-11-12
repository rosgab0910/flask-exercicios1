from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, Flask !!</h1>'
    
@app.route('/versao')
def versao():
    versao = "1.1.0"
    return f'App v{versao}'

@app.route('/saudar/<nome>')
def saudar(nome):
    nome_capitalizado = nome.capitalize()
    return f'Olá, {nome_capitalizado}!'

@app.route('/quadrado/<int:n>')
def quadrado(n):
    resultado = n ** 2
    return f'{n}² = {resultado}'

@app.route('/home')
def home():
    return redirect('/')    