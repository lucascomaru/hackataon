from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from mdbtreinamentos.models import Treinamento

setores_disponiveis = [
    ('Todos', 'Todos os setores'),
    ('Produção', 'Produção'),
    ('Logística', 'Logística'),
    ('Departamento Pessoal', 'Departamento Pessoal'),
    ('Administrativo', 'Administrativo'),
    ('Armazenamento', 'Armazenamento')
]

class TreinamentoForm(FlaskForm):
    nome_treinamento = StringField('Nome do Treinamento', validators=[DataRequired()])
    descricao_treinamento = TextAreaField('Descrição do Treinamento')  # novo campo
    nome_professor = StringField('Nome do Professor', validators=[DataRequired()])
    setor_treinamento = SelectField('Setor do Treinamento', choices=setores_disponiveis, validators=[DataRequired()])
    sala_treinamento = SelectField('Sala do Treinamento', choices=[('B1', 'B1'), ('B2', 'B2'), ('B3', 'B3'), ('B4', 'B4'), ('B5', 'B5'), ('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A4'), ('A5', 'A5')], validators=[DataRequired()])
    data_treinamento = StringField('Data do Treinamento', validators=[DataRequired()])
    hora_treinamento = StringField('Hora do Treinamento', validators=[DataRequired()])
    tipo_treinamento = SelectField('Tipo de Treinamento', choices=[('Presencial', 'Presencial'), ('Online', 'Online')], validators=[DataRequired()])
    submit = SubmitField('Salvar')

class CadastroForm(FlaskForm):
    re = StringField('RE', validators=[DataRequired()])
    treinamento = SelectField('Treinamento', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Cadastrar')

    def __init__(self, *args, **kwargs):
        super(CadastroForm, self).__init__(*args, **kwargs)
        self.treinamento.choices = [(t.id, t.nome) for t in Treinamento.query.all()]
