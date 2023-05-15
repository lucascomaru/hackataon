from flask import render_template, url_for
from mdbtreinamentos import app
#from mdbtreinamentos.models import Treinamento, Cadastro

@app.route('/') #Atribui uma nova funcionalidade para a função abaixo, faz a função abaixo aparecer no site
def homepage():
    return render_template('homepage.html')



@app.route('/treinamentos')
def treinamentos():
    return render_template('treinamentos.html')
#criar o treinamento
#adicionar sessão
#commitar a sessão

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')
#criar o cadastro no treinamento
#adicionar sessão
#commitar a sessão



@app.route('/painel')
def painel():
    return render_template('painel.html')
@app.route('/sessao-download')
def sessao_download():
    return render_template('sessao-download.html')

