from Curso import app
from flask import render_template

@app.route('/')
@app.route('/index', defaults = {"nome":"usuario"})
@app.route('/index/<nome>/<profissao>/<github>')

def index(nome, profissao, github):
    dados = {"profissao": profissao, "github": github}
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')



