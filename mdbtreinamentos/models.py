from mdbtreinamentos import database

class Pessoa(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String(100))
    re = database.Column(database.String(100))
    setor = database.Column(database.String(100))
    cargo = database.Column(database.String(100))
    numero_pessoal = database.Column(database.String(5))
    cadastros = database.relationship('Cadastro', backref='pessoa', lazy=True)

class Treinamento(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String(100))
    descricao = database.Column(database.Text)  # novo campo
    professor = database.Column(database.String(100))
    setor = database.Column(database.String(100))
    sala = database.Column(database.String(100))
    data = database.Column(database.String(100))  # novo campo
    hora = database.Column(database.String(100))
    tipo = database.Column(database.String(100))
    cadastros = database.relationship('Cadastro', backref='treinamento', lazy=True)

class Cadastro(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    pessoa_id = database.Column(database.Integer, database.ForeignKey('pessoa.id'))
    treinamento_id = database.Column(database.Integer, database.ForeignKey('treinamento.id'))
    frequencia = database.relationship('Frequencia', backref='cadastro', lazy=True)

class Frequencia(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    cadastro_id = database.Column(database.Integer, database.ForeignKey('cadastro.id'))
