function exibirConteudo(area, botao) {
    var conteudo = document.getElementById('conteudo');

    if (area === 'painel') {
        fetch('/painel')
            .then(response => response.text())
            .then(html => {
                conteudo.innerHTML = html;
                botao.classList.add('highlight');
            })
            .catch(error => console.log(error));
    } else if (area === 'treinamentos') {
        fetch('/treinamentos')
            .then(response => response.text())
            .then(html => {
                conteudo.innerHTML = html;
                botao.classList.add('highlight');
            })
            .catch(error => console.log(error));
    } else if (area === 'cadastro') {
        fetch('/cadastro')
            .then(response => response.text())
            .then(html => {
                conteudo.innerHTML = html;
                botao.classList.add('highlight');
            })
            .catch(error => console.log(error));
    } else if (area === 'sessao-download') {
        fetch('/sessao-download')
            .then(response => response.text())
            .then(html => {
                conteudo.innerHTML = html;
                botao.classList.add('highlight');
            })
            .catch(error => console.log(error));
    }

    var botoes = document.getElementsByClassName('button');
    for (var i = 0; i < botoes.length; i++) {
        botoes[i].classList.remove('highlight');
    }
    botao.classList.add('highlight');
}
