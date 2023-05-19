from flask import render_template, redirect, url_for, flash, request, send_file, Response
from mdbtreinamentos import app, database
from mdbtreinamentos.models import Treinamento, Pessoa, Cadastro
from mdbtreinamentos.forms import TreinamentoForm, CadastroForm
import pandas as pd
import os
import openpyxl
import io
import datetime


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/painel', methods=['GET'])
def painel():
    treinamentos = Treinamento.query.all()
    return render_template('painel.html', treinamentos=treinamentos)




@app.route('/treinamentos', methods=['GET', 'POST'])
def treinamentos():
    form = TreinamentoForm()
    if form.validate_on_submit():
        nome_treinamento = form.nome_treinamento.data
        descricao_treinamento = form.descricao_treinamento.data
        nome_professor = form.nome_professor.data
        setor_treinamento = form.setor_treinamento.data
        sala_treinamento = form.sala_treinamento.data
        data_treinamento = form.data_treinamento.data
        hora_treinamento = form.hora_treinamento.data
        tipo_treinamento = form.tipo_treinamento.data

        treinamento = Treinamento(nome=nome_treinamento, descricao=descricao_treinamento, professor=nome_professor,
                                  setor=setor_treinamento, sala=sala_treinamento,
                                  data=data_treinamento, hora=hora_treinamento, tipo=tipo_treinamento)

        database.session.add(treinamento)
        database.session.commit()

        flash('Treinamento criado com sucesso!', 'success')

        return redirect(url_for('homepage'))

    return render_template('treinamentos.html', form=form)


def obter_dados_excel():
    caminho_arquivo = os.path.join(app.root_path, 'static', 'planilhadadoss.xlsx')
    df = pd.read_excel(caminho_arquivo)
    df['RE'] = df['RE'].astype(str)
    print(df.columns)
    return df

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = CadastroForm()
    form.treinamento.choices = [(t.id, t.nome) for t in Treinamento.query.all()]

    if form.validate_on_submit():
        re = form.re.data
        print(re)
        treinamento_id = form.treinamento.data


        df = obter_dados_excel()


        linha = df.loc[df['RE'] == re]

        if linha.empty:
            flash('RE não encontrado no registro de funcionários.', 'danger')
            return redirect(url_for('homepage'))


        nome = linha['NOME'].values[0]
        setor = linha['SETOR'].values[0]
        cargo = linha['CARGO'].values[0]
        numero_pessoal = linha['NÚMERO PESSOAL'].values[0]

        pessoa = Pessoa(nome=nome, re=re, setor=setor, cargo=cargo, numero_pessoal=numero_pessoal)
        cadastro = Cadastro(pessoa=pessoa, treinamento_id=treinamento_id)

        database.session.add(pessoa)
        database.session.add(cadastro)
        database.session.commit()

        atualizar_excel_frequencia(treinamento_id)

        flash('Cadastro criado com sucesso!', 'success')

        return redirect(url_for('homepage'))

    return render_template('cadastro.html', form=form)


# def atualizar_excel_frequencia(treinamento):
#
#     cadastros = Cadastro.query.filter_by(treinamento_id=treinamento.id).all()
#
#     dados = []
#     for cadastro in cadastros:
#         dados.append({
#             'Nome': cadastro.pessoa.nome,
#             'RE': cadastro.pessoa.re,
#             'Setor': cadastro.pessoa.setor,
#             'Cargo': cadastro.pessoa.cargo,
#         })
#
#     df = pd.DataFrame(dados)
#
#     nome_chave = treinamento.nome.replace(" ", "_")
#
#     pasta_destino = r'C:\Users\lucas\OneDrive\Área de Trabalho\Treinamentos'
#     nome_arquivo = f'frequencia_{nome_chave}.xlsx'
#     caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)
#
#     df.to_excel(caminho_arquivo, index=False)
#
#     print(f"Arquivo Excel salvo em: {caminho_arquivo}")

@app.route('/sessao-download', methods=['GET'])
def sessao_download():
    treinamentos = Treinamento.query.all()
    return render_template('sessao-download.html', treinamentos=treinamentos)

@app.route('/iniciar-download', methods=['POST'])
def iniciar_download():
    id_treinamento = request.form.get('treinamento_id')
    return redirect(url_for('baixar_excel', id_treinamento=id_treinamento))


def atualizar_excel_frequencia(id_treinamento):
    treinamento = Treinamento.query.get(id_treinamento)
    cadastros = Cadastro.query.filter_by(treinamento_id=id_treinamento).all()

    dados = []
    for cadastro in cadastros:
        pessoa = cadastro.pessoa
        dados.append({
            'Nome': pessoa.nome,
            'RE': pessoa.re,
            'Setor': pessoa.setor,
            'Cargo': pessoa.cargo,
            'Data de Entrada': '',
            'Número Pessoal': pessoa.numero_pessoal
        })

    df = pd.DataFrame(dados)
    nome_chave = treinamento.nome.replace(" ", "_")
    nome_arquivo = f'frequencia_{nome_chave}.xlsx'


    caminho_arquivo_origem = os.path.join(app.root_path, 'static', 'planilhadadoss.xlsx')
    df_origem = pd.read_excel(caminho_arquivo_origem)


    df['Data de Entrada'] = pd.to_datetime(df_origem['DATA DE ENTRADA'], errors='coerce').dt.strftime('%d/%m/%Y')
    df['Número Pessoal'] = df_origem['NÚMERO PESSOAL']


    pasta_destino = os.path.join(app.root_path, 'static', 'ArquivosExcel')
    caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)
    df.to_excel(caminho_arquivo, index=False)

    print(f"Arquivo Excel salvo em: {caminho_arquivo}")

    return df, nome_arquivo



@app.route('/salvar_excel/<id_treinamento>', methods=['GET'])
def salvar_excel(id_treinamento):
    df, nome_arquivo = atualizar_excel_frequencia(id_treinamento)


    saida = io.BytesIO()


    with pd.ExcelWriter(saida, engine='xlsxwriter') as escritor:
        df.to_excel(escritor, sheet_name='Sheet1', index=False)


        worksheet = escritor.sheets['Sheet1']
        for col in worksheet.columns:
            max_length = 0
            column = col[0].column_letter
            for cell in col:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except TypeError:
                    pass
            adjusted_width = (max_length + 2) * 1.2
            worksheet.column_dimensions[column].width = adjusted_width

    saida.seek(0)


    response = Response(saida, mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response.headers["Content-Disposition"] = f"attachment; filename={nome_arquivo}"

    return response


@app.route('/baixar_excel/<id_treinamento>', methods=['GET'])
def baixar_excel(id_treinamento):
    df, nome_arquivo = atualizar_excel_frequencia(id_treinamento)

    saida = io.BytesIO()
    with pd.ExcelWriter(saida, engine='xlsxwriter') as escritor:
        df.to_excel(escritor, sheet_name='Sheet1')

    saida.seek(0)

    response = Response(saida, mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response.headers["Content-Disposition"] = f"attachment; filename={nome_arquivo}"

    return response








