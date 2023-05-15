from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_folder='static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mdbtreinamentos.db'

database = SQLAlchemy(app)

@app.route('/') #Atribui uma nova funcionalidade para a função abaixo, faz a função abaixo aparecer no site
def painel():
    return render_template('painel.html')

@app.route('/treinamentos')
def treinamentos():
    return render_template('treinamentos.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/sessao-download')
def sessao_download():
    return render_template('sessao-download.html')


if __name__ == '__main__':
    app.run(debug=True)
