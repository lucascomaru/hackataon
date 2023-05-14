from main import database

class Treinamento(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String(100))
    professor = database.Column(database.String(100))
    setor = database.Column(database.String(100))
    data = database.Column(database.String(100))
    hora = database.Column(database.String(100))
    tipo = database.Column(database.String(100))

class Cadastro(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    pessoa = database.Column(database.String(100))
    treinamento_id = database.Column(database.Integer, database.ForeignKey('treinamento.id'))
    treinamento = database.relationship('Treinamento')

