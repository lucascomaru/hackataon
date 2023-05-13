from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/') #Atribui uma nova funcionalidade para a função abaixo, faz a função abaixo aparecer no site
def logins():
    return render_template('logins.html')

@app.route('/criar_conta')
def criar_conta():
    return render_template('criar_conta.html')
@app.route('/rh')
def rh():
    return render_template('rh.html')
@app.route('/colaborador')
def colaborador():
    return render_template('colaborador.html')
@app.route('/professor')
def professor():
    return render_template('professor.html')

@app.route('/adicionar_treinamento')
def adicionar_treinamento():
    return render_template('adicionar_treinamento.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')
@app.route('/lista_funcionarios')
def lista_funcionarios():
    funcionarios = [
        {'nome': 'João', 'matricula': '12345', 'setor': 'RH', 'cargo': 'Analista', 'treinamentos': 'Treinamento A'},
        {'nome': 'Maria', 'matricula': '67890', 'setor': 'Financeiro', 'cargo': 'Gerente',
         'treinamentos': 'Treinamento B'},

    ]

    return render_template('lista_funcionarios.html', funcionarios=funcionarios)

if __name__ == '__main__':
    app.run(debug=True)
