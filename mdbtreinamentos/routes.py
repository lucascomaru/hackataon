from flask import render_template, redirect, url_for, flash, request, send_file
from mdbtreinamentos import app, database
from mdbtreinamentos.models import Treinamento, Pessoa, Cadastro
from mdbtreinamentos.forms import TreinamentoForm, CadastroForm
import pandas as pd
import os
import openpyxl

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/painel', methods=['GET'])
def painel():
    treinamentos = Treinamento.query.all()
    return render_template('painel.html', treinamentos=treinamentos)

@app.route('/detalhes_treinamento/<int:treinamento_id>', methods=['GET'])
def detalhes_treinamento(treinamento_id):
    treinamento = Treinamento.query.get_or_404(treinamento_id)
    return render_template('detalhes_treinamento.html', treinamento=treinamento)


@app.route('/treinamentos', methods=['GET', 'POST'])
def treinamentos():
    form = TreinamentoForm()
    if form.validate_on_submit():
        nome_treinamento = form.nome_treinamento.data
        nome_professor = form.nome_professor.data
        setor_treinamento = form.setor_treinamento.data
        sala_treinamento = form.sala_treinamento.data
        data_treinamento = form.data_treinamento.data
        hora_treinamento = form.hora_treinamento.data
        tipo_treinamento = form.tipo_treinamento.data

        treinamento = Treinamento(nome=nome_treinamento, professor=nome_professor, setor=setor_treinamento,
                                  sala=sala_treinamento, data=data_treinamento, hora=hora_treinamento, tipo=tipo_treinamento)

        database.session.add(treinamento)
        database.session.commit()

        flash('Treinamento criado com sucesso!', 'success')

        return redirect(url_for('homepage'))

    return render_template('treinamentos.html', form=form)


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = CadastroForm()
    form.treinamento.choices = [(t.id, t.nome) for t in Treinamento.query.all()]

    if form.validate_on_submit():
        nome = form.nome.data
        re = form.re.data
        setor = form.setor.data
        cargo = form.cargo.data
        treinamento_id = form.treinamento.data

        pessoa = Pessoa(nome=nome, re=re, setor=setor, cargo=cargo)

        cadastro = Cadastro(pessoa=pessoa, treinamento_id=treinamento_id)

        database.session.add(pessoa)
        database.session.add(cadastro)
        database.session.commit()

        treinamento = Treinamento.query.get(treinamento_id)
        atualizar_excel_frequencia(treinamento)

        flash('Cadastro criado com sucesso!', 'success')

        return redirect(url_for('homepage'))

    return render_template('cadastro.html', form=form)



def atualizar_excel_frequencia(treinamento):

    cadastros = Cadastro.query.filter_by(treinamento_id=treinamento.id).all()

    dados = []
    for cadastro in cadastros:
        dados.append({
            'Nome': cadastro.pessoa.nome,
            'RE': cadastro.pessoa.re,
            'Setor': cadastro.pessoa.setor,
            'Cargo': cadastro.pessoa.cargo,
        })

    df = pd.DataFrame(dados)

    nome_chave = treinamento.nome.replace(" ", "_")

    pasta_destino = r'C:\Users\lucas\OneDrive\Área de Trabalho\Treinamentos'
    nome_arquivo = f'frequencia_{nome_chave}.xlsx'
    caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)

    df.to_excel(caminho_arquivo, index=False)

    print(f"Arquivo Excel salvo em: {caminho_arquivo}")


