function exibirConteudo(area, botao) {
    var conteudo = document.getElementById('conteudo');

    if (area === 'painel') {
        conteudo.innerHTML = '<div class="conteudo-centralizado"><h2>Conteúdo do Painel</h2></div>';
    } else if (area === 'treinamentos') {
        conteudo.innerHTML = `
            <div class="conteudo-centralizado">
                <h2>Conteúdo dos Treinamentos</h2>
                <div class="treinamento-form">
                    <div class="form-group">
                        <label for="nome-treinamento">Nome do Treinamento:</label>
                        <div class="input-wrapper">
                            <input type="text" name="nome-treinamento" id="nome-treinamento" required>
                        </div>
                    </div>

                    <div class="form-group">
                        <label for="nome-professor">Nome do Professor:</label>
                        <div class="input-wrapper">
                            <input type="text" name="nome-professor" id="nome-professor" required>
                        </div>
                    </div>

                    <div class="form-group">
                        <label for="setor-treinamento">Setor do Treinamento:</label>
                        <div class="input-wrapper">
                            <select name="setor-treinamento" id="setor-treinamento" required>
                                <option value="">Selecione um setor</option>
                                <option value="Produção">Produção</option>
                                <option value="Logística">Logística</option>
                                <option value="Armazenamento">Armazenamento</option>
                            </select>
                        </div>
                    </div>

                    <div class="form-group">
                        <label for="data-treinamento">Data do Treinamento:</label>
                        <div class="input-wrapper">
                            <input type="date" name="data-treinamento" id="data-treinamento" required>
                        </div>
                    </div>

                    <div class="form-group">
                        <label for="hora-treinamento">Hora do Treinamento:</label>
                        <div class="input-wrapper">
                            <input type="time" name="hora-treinamento" id="hora-treinamento" required>
                        </div>
                    </div>

                    <div class="form-group">
                        <input type="submit" value="Salvar">
                    </div>
                </div>
            </div>`;
    } else if (area === 'cadastro') {
        conteudo.innerHTML = `
            <div class="conteudo-centralizado">
                <h2>Conteúdo do Cadastro</h2>
                <form action="/cadastro" method="POST" class="cadastro-form">
                    <div class="form-group">
                        <label for="nome">Nome:</label>
                        <div class="input-wrapper">
                            <input type="text" name="nome" id="nome" required>
                        </div>
                    </div>

                    <div class="form-group">
                        <label for="re">RE:</label>
                        <div class="input-wrapper">
                            <input type="text" name="re" id="re" required>
                        </div>
                    </div>

                    <div class="form-group">
                        <label for="setor">Setor:</label>
                        <div class="input-wrapper">
                            <select name="setor" id="setor" required>
                                <option value="">Selecione um setor</option>
                                <option value="Produção">Produção</option>
                                <option value="Logística">Logística</option>
                                <option value="Armazenamento">Armazenamento</option>
                            </select>
                        </div>
                    </div>

                    <div class="form-group">
                        <label for="cargo">Cargo:</label>
                        <div class="input-wrapper">
                            <select name="cargo" id="cargo" required>
                                <option value="">Selecione um cargo</option>
                                <option value="Auxiliar de Produção">Auxiliar de Produção</option>
                                <option value="Conferente">Conferente</option>
                                <option value="Estoquista">Estoquista</option>
                            </select>
                        </div>
                    </div>

                    <div class="form-group">
                        <input type="submit" value="Cadastrar">
                    </div>
                </form>
            </div>`;
    } else if (area === 'sessao-download') {
        conteudo.innerHTML = '<div class="conteudo-centralizado"><h2>Conteúdo da Sessão de Download</h2></div>';
    }

    var botoes = document.getElementsByClassName('button');
    for (var i = 0; i < botoes.length; i++) {
        botoes[i].classList.remove('highlight');
    }
    botao.classList.add('highlight');
}

