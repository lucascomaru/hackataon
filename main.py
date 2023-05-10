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

if __name__ == '__main__':
    app.run(debug=True)
