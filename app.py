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

@app.route('/pagina')
def pagina():
    return render_template('pagina.html')

@app.route('/buscar/<item>')
def buscar(item):
    itens = ["maçã", "banana", "laranja", "uva", "morango"]

    encontrado = False
    for elemento in itens:
        if elemento == item:
            encontrado = True
            break
    
if encontrado:
        return f'Item "{item}" encontrado na lista.'
else:
        return f'Item "{item}" não encontrado na lista.'

if __name__ == '__main__':
    app.run(debug=True)