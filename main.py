from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/') #Atribui uma nova funcionalidade para a função abaixo, faz a função abaixo aparecer no site
def hello():
    return render_template('logins.html')

@app.route('/criar_conta')
def criar_conta():
    return render_template('criar_conta.html')

if __name__ == '__main__':
    app.run(debug=True)
